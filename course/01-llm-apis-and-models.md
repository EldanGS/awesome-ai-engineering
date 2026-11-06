# Domain 1: LLM APIs and Model Capabilities

**Weight: 12%.** Core question: *which model and API features fit this workload, and what will it cost?*

Customers rarely ask "which model is best". They ask "can it read our contracts", "how fast is it", "what will this cost at our volume" and "why did it work in your demo but not for us". A solutions engineer answers those questions with numbers from a quick experiment, not with a leaderboard screenshot. This domain gives you the working vocabulary of model APIs across the major providers and a repeatable way to pick and size a model.

## Contents

- [Learning objectives](#learning-objectives)
- [Core concepts](#core-concepts)
- [Patterns and anti-patterns](#patterns-and-anti-patterns)
- [Reading list](#reading-list)
- [Free credentials](#free-credentials)
- [Hands-on lab: model bake-off](#hands-on-lab-model-bake-off)
- [Review questions](#review-questions)

## Learning objectives

- [ ] Explain tokens, context windows, output limits and how they drive cost and latency.
- [ ] Map the request anatomy of the Anthropic Messages API, the OpenAI Responses API and the Gemini API to each other.
- [ ] Implement streaming and explain time to first token versus total latency.
- [ ] Implement a tool-use (function-calling) round trip and explain who executes the tool.
- [ ] Choose between schema-constrained structured outputs, JSON mode and free text.
- [ ] Send images and PDFs to a model and state the practical limits.
- [ ] Explain reasoning or "thinking" controls and when extra reasoning is worth the latency.
- [ ] Select a model tier with a written rationale covering quality, latency, cost, deployment and data constraints.
- [ ] Estimate monthly cost for a workload from traffic, token counts, caching and batch assumptions.

## Core concepts

### Tokens, context windows and limits

A **token** is the unit a model reads and writes: a word fragment, punctuation mark or byte sequence. Every provider bills and limits by tokens, and every provider tokenizes differently, so the same document can cost a different number of tokens on two models. English prose is roughly 0.75 words per token; code, JSON, non-Latin scripts and tables are usually denser in tokens. Always measure with the provider's token-counting endpoint or tokenizer rather than guessing.

| Term | What it means | Why the customer cares |
| --- | --- | --- |
| Context window | Maximum input plus output tokens the model can attend to in one request. | Decides whether a 300-page contract fits in one call or needs retrieval. |
| Max output tokens | Ceiling on generated tokens for one response. | Long reports or code files can be truncated mid-sentence. |
| Input tokens | System prompt, conversation history, documents, tool definitions, tool results. | Usually the largest share of the bill in RAG and agent workloads. |
| Output tokens | Generated text, tool calls and (on reasoning models) thinking tokens. | Priced several times higher than input; dominates latency. |
| Cached input tokens | Prompt prefix reused from a recent request. | Much cheaper and faster; the main lever for long system prompts. |
| Rate limits | Requests, input tokens and output tokens per minute per organization or project. | A pilot that works for five users can fail at fifty. |

Rules of thumb you can say out loud in a meeting:

- A bigger context window is not free memory. Cost and latency grow with input size, and recall of details buried in the middle of very long inputs can degrade. Put only what the task needs in the window.
- Output tokens drive latency. A response of 1,500 tokens at 60 tokens per second takes 25 seconds no matter how fast the first token arrives.
- Tool definitions and tool results count as input on every turn of a conversation.

### Request anatomy across providers

The three most common commercial APIs look different but share the same building blocks. Learn the mapping once and you can demo on whichever platform the customer has approved.

| Concept | Anthropic Messages API | OpenAI Responses API | Gemini API (google-genai SDK) |
| --- | --- | --- | --- |
| Endpoint | `POST /v1/messages` | `POST /v1/responses` | `models.generateContent` |
| Instructions | `system` parameter | `instructions` parameter or a developer message | `system_instruction` in config |
| Conversation | `messages` list of user and assistant turns, sent every time | `input` list, or chain with `previous_response_id` for server-side state | `contents` list, or a chat session helper |
| Tools | `tools` with `name`, `description`, `input_schema` | `tools` with `type: "function"`, `name`, `parameters`, plus hosted tools | `tools` with function declarations |
| Tool call in response | `tool_use` content block; `stop_reason == "tool_use"` | `function_call` output item with `call_id` | `function_call` part |
| Tool result | `tool_result` block in the next user message | `function_call_output` input item | `function_response` part |
| Structured output | `output_config` format, or `client.messages.parse()` with a Pydantic model | `text.format` JSON schema, or `client.responses.parse()` with `text_format` | `response_schema` with `response_mime_type="application/json"` |
| Streaming | Server-sent events; SDK `messages.stream()` helper | `stream=True`; typed events such as `response.output_text.delta` | `generate_content_stream` |
| Reasoning control | Adaptive thinking plus `effort` in `output_config` | `reasoning` effort setting on reasoning models | Thinking configuration on thinking-capable models |

Open-weight models (Llama, Mistral, Qwen, Gemma, DeepSeek and others) are usually served behind an OpenAI-compatible endpoint by runtimes such as vLLM or Ollama, or by managed hosts. "Compatible" covers the basics; advanced features such as structured outputs, parallel tool calls and caching vary by server and model, so test them.

### A minimal request, streamed

Streaming makes a demo feel fast, keeps long generations from hitting HTTP timeouts, and lets the UI show progress. Measure **time to first token (TTFT)** and **total time** separately.

```python
import time
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY

start = time.perf_counter()
first_token_at = None

with client.messages.stream(
    model="claude-opus-5-5",
    max_tokens=2000,
    system="You are a concise assistant for a logistics company.",
    messages=[{"role": "user", "content": "Summarize the main causes of late deliveries."}],
) as stream:
    for text in stream.text_stream:
        if first_token_at is None:
            first_token_at = time.perf_counter()
        print(text, end="", flush=True)
    final = stream.get_final_message()

print(f"\nTTFT {first_token_at - start:.2f}s, total {time.perf_counter() - start:.2f}s")
print(final.usage)  # input_tokens, output_tokens, cache read and write counts
```

The equivalent with the OpenAI Responses API:

```python
import os
from openai import OpenAI

client = OpenAI()  # reads OPENAI_API_KEY
model = os.environ.get("OPENAI_MODEL", "gpt-5")  # pick a current model from the provider's models page

stream = client.responses.create(
    model=model,
    instructions="You are a concise assistant for a logistics company.",
    input="Summarize the main causes of late deliveries.",
    stream=True,
)
for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
```

Model identifiers change frequently. Keep them in configuration, not in code, and check the provider's models page before every customer engagement.

### Tool use in one round trip

With tool use (also called function calling), the model does not run anything. It returns a structured request to call a tool; **your code** executes it and sends the result back. That single fact answers many security questions: the model only reaches systems your code exposes.

1. Send the user request plus tool definitions (name, description, JSON Schema for inputs).
2. The model replies with a tool call (name plus arguments) instead of, or alongside, text.
3. Your code validates the arguments, executes the call with the end user's permissions, and returns the result.
4. The model uses the result to answer or to request another call.

Domain 4 builds this into full agent loops and MCP servers.

### Structured outputs

Most integrations need machine-readable output: a JSON object for a CRM, a classification label for a router, extracted fields for a form. There are three levels of reliability.

| Approach | Guarantee | Use when |
| --- | --- | --- |
| Free text plus "respond in JSON" in the prompt | None; parse errors and missing fields happen | Quick prototypes only. |
| JSON mode | Valid JSON, but not necessarily your schema | Legacy models without schema support. |
| Schema-constrained structured outputs | Output validates against your JSON Schema | Production extraction, classification, routing, UI rendering. |

```python
from pydantic import BaseModel
from openai import OpenAI

class Ticket(BaseModel):
    category: str
    priority: int  # 1 (urgent) to 4 (low)
    summary: str
    needs_human: bool

client = OpenAI()
response = client.responses.parse(
    model="gpt-5",
    input="Customer: our invoices have shown the wrong VAT rate since Monday and finance is blocked.",
    text_format=Ticket,
)
ticket = response.output_parsed
print(ticket.category, ticket.priority, ticket.needs_human)
```

The Anthropic SDK has the same shape: `client.messages.parse(..., output_format=Ticket)` returns `response.parsed_output`. A schema guarantees shape, not truth: a field can be valid and wrong, so you still evaluate content (Domain 5).

### Multimodal inputs

| Input | Typical support | Practical notes |
| --- | --- | --- |
| Images | All major frontier models | Screenshots, charts, photos of forms. Resolution limits apply; very small text may be missed. Images cost tokens. |
| PDFs | Native PDF input on several APIs; otherwise convert pages to text plus images | Native support reads both text and layout. Page and request size limits apply. |
| Audio | Speech-to-text and realtime voice models | Often a separate endpoint or model; latency budgets are tight for voice agents. |
| Video | Some models accept video or frame sequences | Expensive in tokens; sample frames for most business uses. |
| Generated images or audio | Separate generation models | Check licensing and content policies before demoing to marketing teams. |

In discovery, ask for **real samples**: scanned faxes, rotated photos, multi-column PDFs and spreadsheets pasted as images are where demos break.

### Reasoning models and effort

Many current models can spend extra tokens reasoning before they answer. Providers expose this as adaptive thinking, reasoning effort or a thinking budget. More reasoning generally improves multi-step analysis, planning, math and code, and increases latency and output-token cost.

| Workload | Suggested starting point |
| --- | --- |
| Classification, routing, short extraction, chat replies | Lowest effort or a small model; measure first. |
| Customer-facing Q&A over retrieved documents | Low to medium effort; quality usually depends more on retrieval than on reasoning. |
| Multi-step agents, code generation, complex analysis | Medium to high effort on a capable model. |
| Rare, high-stakes reviews (contract risk, incident analysis) | Highest effort, often asynchronously or in batch. |

Tune effort per route with an eval set, not globally by feel.

### Model selection framework

Pick models with the customer's constraints, then confirm with a small experiment.

| Question | Why it matters | Typical answer pattern |
| --- | --- | --- |
| What is the hardest task in the workflow? | Sets the minimum capability tier. | Use a frontier model for the hard step, smaller models for easy steps. |
| What latency does the user tolerate? | Voice and autocomplete need sub-second TTFT; reports can take minutes. | Smaller or faster tiers for interactive paths; batch for offline. |
| What volume and budget? | Determines whether per-token cost or fixed hosting cost wins. | API pricing for spiky or modest volume; dedicated capacity or open weights at very high steady volume. |
| Where must data and inference live? | Residency, sovereignty and procurement rules. | First-party API, the customer's cloud marketplace (Bedrock, Azure AI Foundry, Vertex AI) or self-hosted open weights. |
| Which features are required? | Not every model or platform has every feature. | Check tool use, structured outputs, caching, batch, PDF input and regional availability on the target platform. |
| How will we know? | Leaderboards do not measure the customer's task. | A 30 to 100 example eval on the customer's own data (Domain 5). |

Model tiers in practice:

| Tier | Strengths | Trade-offs | Example uses |
| --- | --- | --- | --- |
| Frontier (largest proprietary models) | Best reasoning, coding, long-context and agentic reliability | Highest cost and latency | Agents, complex analysis, hard extraction, evaluation judges |
| Mid tier | Strong quality at lower cost and latency | Slightly weaker on the hardest tasks | Most customer-facing assistants and RAG |
| Small or fast tier | Very low cost and latency | Weaker on nuance and long instructions | Routing, classification, PII detection, sub-agents |
| Open weights (self-hosted or managed) | Control, data locality, fine-tuning, fixed cost at scale | You own serving, scaling, safety and upgrades | Air-gapped environments, very high steady volume, specialised fine-tunes |

### Estimating cost

Use a simple, explicit formula and show your assumptions. With illustrative prices (replace with the current price sheet):

```text
requests_per_month = 20,000 users x 6 requests/day x 22 days = 2,640,000
input_tokens       = 6,000 per request (system prompt 2,000 + retrieved context 3,500 + question 500)
output_tokens      = 400 per request

uncached input cost  = 2.64M x 6,000 / 1M x $3.00  = $47,520
output cost          = 2.64M x   400 / 1M x $15.00 = $15,840
total (no caching)   = $63,360 per month

with prompt caching on the 2,000-token system prompt at 10% of input price:
  cached part        = 2.64M x 2,000 / 1M x $0.30  = $1,584
  uncached part      = 2.64M x 4,000 / 1M x $3.00  = $31,680
  total              = $49,104 per month (about 22% lower)
```

Then ask which requests could move to a smaller model, which could run in a discounted batch API overnight, and whether retrieved context can shrink. Present a range (low, expected, high) rather than a single number.

### Errors, retries and limits

| Signal | Meaning | Correct handling |
| --- | --- | --- |
| HTTP 429 | Rate limit exceeded | Exponential backoff with jitter; respect `retry-after`; request a limit increase before a pilot. |
| HTTP 5xx or overloaded | Provider-side issue | Retry with backoff; consider a fallback model or region. |
| HTTP 400 | Invalid request (bad parameter, too many tokens, unsupported feature) | Do not retry; fix the request. |
| Stop reason "max tokens" | Output was truncated | Raise the limit, stream, or ask for shorter output. |
| Refusal | Model or safety system declined | Log, show a graceful message, review the prompt and use case. |

Official SDKs already retry transient errors a small number of times; configure timeouts and retries rather than writing your own wrappers.

## Patterns and anti-patterns

| Pattern | Why it works |
| --- | --- |
| Model router: a small model classifies, a larger model handles hard cases | Cuts cost and latency while keeping quality where it matters. |
| Model IDs and parameters in config, with an eval run before any change | Lets you upgrade models safely and quickly. |
| Measure TTFT, total latency, tokens and cost on every demo request | You can answer "how fast" and "how much" with data. |
| Provider abstraction only at the boundary (a thin client or gateway) | Keeps the option to switch without hiding provider-specific features you need. |
| Structured outputs for anything a program reads | Removes a whole class of parsing bugs. |

| Anti-pattern | What goes wrong |
| --- | --- |
| Choosing a model from a public leaderboard alone | The customer's task, data and language differ from the benchmark. |
| Stuffing the whole knowledge base into a long context "because it fits" | High cost, slow responses and missed details; retrieval is usually better. |
| Hard-coding one provider's quirks deep in business logic | Migration and multi-cloud procurement become painful. |
| Ignoring output tokens in cost estimates | Output is priced higher and dominates latency. |
| Demoing on a model or region the customer cannot buy | The technical win evaporates in procurement. |

## Reading list

- [anthropics/anthropic-sdk-python](https://github.com/anthropics/anthropic-sdk-python): official Python SDK for the Claude API.
- [openai/openai-python](https://github.com/openai/openai-python): official Python SDK, including the Responses API helpers.
- [googleapis/python-genai](https://github.com/googleapis/python-genai): Google Gen AI SDK for the Gemini API and Vertex AI.
- [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks): runnable notebooks for tool use, PDFs, vision, caching and more.
- [openai/openai-cookbook](https://github.com/openai/openai-cookbook): examples and guides for the OpenAI API.
- [google-gemini/cookbook](https://github.com/google-gemini/cookbook): Gemini API examples.
- [vllm-project/vllm](https://github.com/vllm-project/vllm) and [ollama/ollama](https://github.com/ollama/ollama): serve open-weight models behind OpenAI-compatible endpoints.
- [BerriAI/litellm](https://github.com/BerriAI/litellm): a unified client and proxy across many providers.
- Claude docs: [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview), [Streaming](https://platform.claude.com/docs/en/build-with-claude/streaming), [Tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview), [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs), [Vision](https://platform.claude.com/docs/en/build-with-claude/vision), [PDF support](https://platform.claude.com/docs/en/build-with-claude/pdf-support), [Token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting), [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows), [Rate limits](https://platform.claude.com/docs/en/api/rate-limits).
- OpenAI docs: [Text generation](https://platform.openai.com/docs/guides/text), [Responses API reference](https://platform.openai.com/docs/api-reference/responses), [Structured outputs](https://platform.openai.com/docs/guides/structured-outputs), [Function calling](https://platform.openai.com/docs/guides/function-calling), [Latency optimization](https://platform.openai.com/docs/guides/latency-optimization).
- Gemini docs: [Gemini API](https://ai.google.dev/gemini-api/docs), [Function calling](https://ai.google.dev/gemini-api/docs/function-calling), [Structured output](https://ai.google.dev/gemini-api/docs/structured-output), [Long context](https://ai.google.dev/gemini-api/docs/long-context).
- [Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers/index): call many open-weight models through one API.
- [Artificial Analysis](https://artificialanalysis.ai): independent latency, throughput and price comparisons (use alongside your own evals).

## Free credentials

| Credential | Provider | Why it fits this domain |
| --- | --- | --- |
| [Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api) | Anthropic Academy | Messages API, tool use, structured outputs, multimodal input. |
| [Claude Platform 101](https://academy.claude.com/courses/claude-platform-101) | Anthropic Academy | Platform features, models and workspace setup. |
| [AI capabilities and limitations](https://academy.claude.com/courses/ai-capabilities-and-limitations) | Anthropic Academy | Vocabulary for setting realistic customer expectations. |
| [Optimize AI Application Performance](https://academy.openai.com/public/courses/optimize-ai-application-performance-1k50h) | OpenAI Academy | Latency, cost and quality trade-offs. |
| [Applied AI Foundations](https://academy.openai.com/public/courses/applied-ai-foundations-szsmv) | OpenAI Academy | Practical model capabilities. |
| [Introduction to Large Language Models](https://www.skills.google/course_templates/539) | Google Skills | LLM fundamentals and Google Cloud context. |

Browse the full [Free AI Certifications Tracker](../free-certifications/README.md) for more.

## Hands-on lab: model bake-off

**Goal:** produce a one-page, data-backed model recommendation for a realistic workload.

**Scenario:** a mid-size insurer wants an assistant that reads inbound claim emails, extracts structured fields and drafts a reply.

1. Create 25 synthetic claim emails with a mix of easy, messy and adversarial cases (missing policy numbers, two claims in one email, a non-English email, an angry customer, an attachment description only). Write the expected extracted fields for each.
2. Define a Pydantic schema with at least six fields (policy number, claim type, incident date, amount, urgency, needs human review).
3. Write one script that runs every email through at least three models: two tiers from one provider and one model from a second provider or a local open-weight model through Ollama or vLLM.
4. Use schema-constrained structured outputs where the API supports it. For each call record: model, TTFT, total latency, input tokens, output tokens, schema-valid (yes or no) and field-level accuracy against your expected values.
5. Stream one reply draft per model and record TTFT.
6. Compute cost per 1,000 emails from current public prices, and a monthly projection for 40,000 emails.
7. Repeat the best model with a lower and a higher reasoning effort setting, if available, and note the quality and latency change.

**Deliverable:** `model-selection.md` with a results table, a recommendation (primary model, fallback, router opportunity), cost range, and three risks you would raise with the customer. Commit the script and raw results as CSV.

## Review questions

1. A customer says, "The new model has a one-million-token context window, so we will skip retrieval and send all 4,000 policy documents every time." What is your response?

    <details><summary>Answer</summary>

    Explain the trade-offs: the documents may not fit, and even if they do, every request pays for and waits on all those input tokens, and recall of specific details in very long inputs can be weaker than with targeted retrieval. Propose retrieval to select the relevant passages, use long context for genuinely whole-document tasks (one long contract), and cache any stable prefix. Back it up with a quick latency and cost measurement on their data.

    </details>

2. In a tool-use flow, who executes the tool, and why does that matter in a security review?

    <details><summary>Answer</summary>

    The application executes the tool. The model only emits a structured request with a tool name and arguments. That means the model can only reach systems the application exposes, the application can validate arguments, enforce the end user's permissions, log every call and require human approval for risky actions. The security boundary is your code, not the model.

    </details>

3. Your demo streams the first words in 0.6 seconds, but users complain the assistant is slow. Responses average 1,800 output tokens. What is happening and what do you change?

    <details><summary>Answer</summary>

    TTFT is fine; total latency is dominated by output length. At typical generation speeds, 1,800 tokens takes many seconds. Reduce output length (tighter instructions, structured or bulleted output, progressive disclosure), use a faster tier for this route, lower reasoning effort if it is enabled, and keep streaming so users see progress.

    </details>

4. A CRM integration occasionally fails because the model returns a field named `prio` instead of `priority`. Which fix is most robust?

    <details><summary>Answer</summary>

    Use schema-constrained structured outputs (for example `responses.parse` with a Pydantic model or the Claude structured outputs feature) so the response must validate against the schema. Prompt instructions and JSON mode reduce but do not eliminate shape errors. Still validate field values, since a schema guarantees shape, not correctness.

    </details>

5. A bank must keep all inference inside its existing AWS account and region. It has an enterprise agreement with AWS. How does this change your model selection?

    <details><summary>Answer</summary>

    Restrict the candidate list to models available on the bank's approved platform (for example Amazon Bedrock in its region) or open-weight models it can host itself. Check feature parity on that platform (tool use, structured outputs, caching, batch, PDF input) and regional availability. Run the eval on the platform the bank will actually buy through, so the technical win survives procurement.

    </details>

6. You estimate cost at $60,000 per month and the economic buyer says the budget is $25,000. Name four levers before you suggest a cheaper model across the board.

    <details><summary>Answer</summary>

    Prompt caching for stable prefixes; trimming retrieved context and conversation history; routing easy requests to a smaller model and keeping the large model for hard ones; moving non-interactive work to a discounted batch API; lowering reasoning effort where evals show no quality loss; shortening outputs. Re-run the eval after each change to prove quality holds.

    </details>

7. Why should model identifiers live in configuration and be paired with an eval run?

    <details><summary>Answer</summary>

    Providers release and retire models frequently, and behaviour changes between versions. Configuration makes swaps a deployment change rather than a code change, and an eval run before each change shows whether quality, latency and cost moved, which protects the customer from silent regressions.

    </details>
