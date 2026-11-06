# Domain 2: Prompt and Context Engineering

**Weight: 12%.** Core question: *what does the model need to see, in what order, to do this reliably?*

Prompt engineering is writing clear instructions. Context engineering is the wider job of deciding everything that enters the model's window on each call: instructions, examples, retrieved documents, conversation history, tool definitions, tool results and memory. In customer work, most "the model is not good enough" complaints turn out to be context problems: missing business rules, contradictory instructions, irrelevant retrieved text or a history that has grown until the important part is buried.

## Contents

- [Learning objectives](#learning-objectives)
- [Core concepts](#core-concepts)
- [Patterns and anti-patterns](#patterns-and-anti-patterns)
- [Reading list](#reading-list)
- [Free credentials](#free-credentials)
- [Hands-on lab: prompt rescue](#hands-on-lab-prompt-rescue)
- [Review questions](#review-questions)

## Learning objectives

- [ ] Write a system prompt with role, task, context, constraints, output format and examples that a colleague could maintain.
- [ ] Explain why clear, direct instructions with reasons beat capitalised warnings and long lists of prohibitions.
- [ ] Use few-shot examples well: diverse, representative, and separated from the instructions.
- [ ] Structure long inputs with delimiters (for example XML-style tags) and put documents before the question.
- [ ] Decompose a complex task into a prompt chain and explain when chaining beats one big prompt.
- [ ] Design the context budget for a long conversation or agent: what to keep, summarise, retrieve or drop.
- [ ] Use prompt caching by ordering stable content first and volatile content last.
- [ ] Version, review and test prompts like code.

## Core concepts

### Prompt engineering versus context engineering

| | Prompt engineering | Context engineering |
| --- | --- | --- |
| Unit of work | One instruction block | Everything the model sees on every call |
| Typical artefacts | System prompt, few-shot examples, output format | Retrieval results, tool definitions, memory, history management, summaries |
| Failure mode | Ambiguous or contradictory instructions | Too much, too little or the wrong information in the window |
| Where it matters most | Single-call tasks: extraction, classification, drafting | Multi-turn assistants, RAG and long-running agents |

Treat the context window as a scarce budget. Every token should earn its place, because irrelevant content costs money, slows responses and can distract the model.

### Anatomy of a maintainable system prompt

Write prompts for a smart new colleague who has never seen the customer's business. State what to do and why.

| Section | Purpose | Example content |
| --- | --- | --- |
| Role and audience | Sets voice and expertise | "You help claims handlers at a regional insurer. They are experts in policy but not in IT." |
| Task | What success looks like | "Draft a reply that confirms receipt, lists missing documents and gives the next step." |
| Context and rules | Business knowledge the model cannot guess | Coverage rules, escalation thresholds, tone guide, product names. |
| Constraints with reasons | Boundaries the model should respect | "Do not promise payment dates, because only the adjuster can commit to them." |
| Output format | What the downstream program or person needs | Headings, length, a JSON schema, or a template. |
| Examples | Shows rather than tells | Two to five varied input and output pairs in their own tagged section. |
| Uncertainty behaviour | What to do when information is missing | "If the policy number is missing, ask for it rather than guessing." |

A compact example:

```text
You draft first replies to inbound claim emails for Northshore Mutual's claims team.
Handlers review every draft before it is sent, so prefer accuracy over completeness.

<rules>
- Confirm receipt and restate the claim type in one sentence.
- List any missing documents from the checklist below. If none are missing, say so.
- Never state whether a claim is covered. Coverage decisions belong to the adjuster,
  and premature statements create legal risk.
- If the email mentions injury, add the line "ESCALATE: injury" at the top, because
  injury claims have a 24-hour response requirement.
</rules>

<checklist>
Motor: photos of damage, police report number if applicable, repair estimate.
Property: photos, proof of ownership for items over 1,000 EUR.
</checklist>

Write in plain, warm English under 150 words. Use the customer's name if present.
```

Notice the reasons attached to rules. Models generalise better from "why" than from bare commands, and future maintainers know which rules are load-bearing.

### Techniques and when to use them

| Technique | What it is | Use when | Watch out for |
| --- | --- | --- | --- |
| Clear, direct instructions | Say exactly what you want, in order | Always | Vague goals such as "make it good". |
| Few-shot examples | Input and output pairs | Format, tone or edge-case handling is hard to describe | Examples that are too similar; the model copies surface features. |
| Delimiters and tags | Wrap documents, examples and data in named sections | Long or mixed inputs | Inconsistent tag names across the prompt. |
| Documents first, question last | Put long material above the instructions that use it | Long-context tasks | Burying the actual question in the middle. |
| Ask for reasoning before the answer | Let the model work through steps, or enable thinking | Multi-step analysis | Extra latency and tokens; parse only the final answer. |
| Prompt chaining | Split a task into sequential calls | Distinct sub-tasks (extract, then analyse, then draft) | More calls to orchestrate and evaluate. |
| Grounding with quotes | Ask the model to cite or quote supporting text first | Document Q&A, compliance | Quotes must be checked, not just requested. |
| Explicit "I do not know" path | Give permission and a format for uncertainty | Any factual task | Without it, models tend to fill gaps. |
| Structured outputs | Constrain the output to a schema | Program-consumed output | A valid schema does not mean correct content. |

Some techniques from older models are now counter-productive or unsupported. For example, several current APIs no longer accept a pre-filled assistant turn, and recent models follow instructions closely enough that SHOUTING or repeating rules can make them over-apply the rule. Prefer calm, specific instructions and structured outputs.

### Prompt chaining versus one prompt

| Signal | One prompt | Chain of prompts |
| --- | --- | --- |
| Task has one clear output | Yes | |
| Sub-tasks need different models, tools or temperatures of creativity | | Yes |
| You need to inspect or approve an intermediate result | | Yes |
| Latency budget is tight | Yes | |
| One sub-task fails often and needs its own eval | | Yes |

A useful customer pattern is **extract, verify, act**: one call extracts facts into a schema, code or a second call checks them against rules, and only then does a call draft the customer-facing output.

### Managing context over long conversations and agents

As conversations and agent loops grow, history and tool results crowd out what matters. Options, from simplest to most involved:

| Strategy | How it works | Trade-off |
| --- | --- | --- |
| Sliding window | Keep the last N turns | Loses early facts such as the customer's account number. |
| Pinned facts | Extract key facts into a short structured block kept at the top | Needs an extraction step and a schema. |
| Summarisation or compaction | Replace older turns with a summary | Detail loss; summaries must be evaluated. Some APIs offer server-side compaction. |
| Clearing old tool results | Drop bulky tool outputs once used | The model cannot re-read them without calling the tool again. |
| External memory | Store notes in a file or database the agent can read and write | More moving parts; must be scoped per user for privacy. |
| Just-in-time retrieval | Keep references (IDs, paths) and fetch content only when needed | More tool calls, much smaller context. |
| Sub-agents | Delegate a sub-task to a fresh context and return only a summary | Coordination overhead (see Domain 4). |

### Prompt caching and ordering

Caching works on an exact **prefix** of the request. Any change early in the prompt invalidates everything after it. Order content from most stable to most volatile:

1. Tool definitions (keep the set and order deterministic).
2. System prompt and long reference material.
3. Few-shot examples.
4. Conversation history.
5. The new user message, timestamps, request IDs and per-user data.

```python
import anthropic

client = anthropic.Anthropic()
POLICY_HANDBOOK = open("handbook.md").read()  # tens of thousands of tokens, rarely changes

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    system=[
        {"type": "text", "text": "You answer questions about the Northshore claims handbook."},
        {"type": "text", "text": POLICY_HANDBOOK, "cache_control": {"type": "ephemeral"}},
    ],
    messages=[{"role": "user", "content": "What documents does a motor claim need?"}],
)
print(response.usage.cache_creation_input_tokens, response.usage.cache_read_input_tokens)
```

If `cache_read_input_tokens` stays at zero on repeat calls, something in the prefix is changing: a timestamp in the system prompt, unsorted JSON, or a tool list built in random order. OpenAI applies caching automatically to long repeated prefixes; the same ordering rules apply.

### Prompts as code

| Practice | Why |
| --- | --- |
| Store prompts in version control, not in a notebook cell or a vendor console only | Diffs, reviews and rollbacks. |
| Use templates with named variables | Clear separation of fixed instructions and per-request data. |
| Pair every prompt change with an eval run | Prevents fixing one case while breaking ten others (Domain 5). |
| Keep a changelog of why each rule exists | New team members, and the customer's team after handoff, can maintain it. |
| Separate customer-specific content from the generic prompt | Reuse across accounts without leaking one customer's rules to another. |

### Using the model to improve prompts

Models are good at critiquing and rewriting prompts. Give a model the prompt, a handful of failing examples and the expected outputs, and ask it to propose a revision and explain each change. Always validate the revision against the full eval set: a rewrite that fixes three failures can break others.

## Patterns and anti-patterns

| Pattern | Why it works |
| --- | --- |
| Instructions with reasons | The model generalises the intent to unseen cases. |
| Tagged sections for documents, rules and examples | Clear boundaries; easier to reference and to cache. |
| A defined "missing information" behaviour | Reduces fabricated details. |
| Extract, verify, act chains | Each step is testable; risky actions are gated. |
| Stable-first ordering | High cache hit rates, lower cost and latency. |
| Customer glossary in context | Product names, acronyms and internal jargon get interpreted correctly. |

| Anti-pattern | What goes wrong |
| --- | --- |
| The "mega prompt" that grew one rule per bug | Contradictions, over-application of rules, nobody knows which rules matter. |
| Only negative instructions ("never", "do not") | The model does not know what to do instead. |
| Examples that all look alike | The model copies the pattern too literally. |
| Timestamps or user IDs at the top of the system prompt | Every request misses the cache. |
| Treating prompt tweaks as the fix for missing data | No prompt can supply facts the model was never given; fix retrieval or tools. |
| Editing the production prompt in a console with no review | Silent regressions and no audit trail. |

## Reading list

- [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial): a hands-on prompt engineering course in notebooks.
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) and its site [promptingguide.ai](https://www.promptingguide.ai): broad survey of techniques and papers.
- [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks): prompt caching, chaining and long-document recipes.
- [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy): programmatic prompt optimisation against a metric.
- [567-labs/instructor](https://github.com/567-labs/instructor): structured outputs with Pydantic across many providers.
- [Claude prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) and [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).
- [OpenAI prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering) and [OpenAI prompt caching](https://platform.openai.com/docs/guides/prompt-caching).
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (Anthropic Engineering).
- [Patterns for building LLM-based systems and products](https://eugeneyan.com/writing/llm-patterns/) (Eugene Yan).

## Free credentials

| Credential | Provider | Why it fits this domain |
| --- | --- | --- |
| [AI Fluency for builders](https://academy.claude.com/courses/ai-fluency-for-builders) | Anthropic Academy | Delegation, description and discernment when building with models. |
| [AI Fluency: Framework and foundations](https://academy.claude.com/courses/ai-fluency-framework-foundations) | Anthropic Academy | A vocabulary for explaining good human-AI collaboration to customers. |
| [Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api) | Anthropic Academy | Prompt evaluation, caching and prompt workflows modules. |
| [Prompt Fundamentals](https://trailhead.salesforce.com/content/learn/modules/prompt-fundamentals) | Salesforce Trailhead | Prompt basics in a business application context. |

## Hands-on lab: prompt rescue

**Goal:** take a messy, real-looking prompt and make it reliable, measurable and cache-friendly.

1. Start from this "inherited" prompt: `You are a helpful assistant. ALWAYS be polite!!! Answer customer questions about our SaaS billing. NEVER make things up. Don't talk about competitors. Use the docs. Today is {date}. User: {user_id}.` Put it in a file under version control.
2. Write 30 test questions about a fictional SaaS billing policy (refunds, proration, seat changes, tax, failed payments), including eight with no answer in the docs and four that mention competitors. Write a short billing policy document (two to three pages) to serve as the reference.
3. Run the original prompt with the policy appended and record: correct answers, fabricated answers, refusals that should have been answers, and cache read tokens on repeated calls.
4. Rewrite the prompt: role and audience, task, rules with reasons, policy in tags, an explicit "not in the policy" response, output format, and two or three varied examples. Move the date and user ID to the end of the request.
5. Re-run the same 30 questions. Compare accuracy, fabrication rate and cache hits.
6. Split one complex question type (for example "why was I charged this amount?") into a two-step chain: extract the relevant billing events, then explain. Compare against the single prompt on those questions.
7. Ask a model to critique your rewritten prompt using the remaining failures, apply the changes you agree with, and re-run once more.

**Deliverable:** `prompt-rescue.md` with the before and after prompts, a results table for each run, the cache hit rate before and after, and three rules you deliberately removed and why.

## Review questions

1. A customer's prompt contains 40 rules added one bug at a time, and the model now refuses many legitimate requests. What do you do?

    <details><summary>Answer</summary>

    Build or reuse an eval set that includes both the original bug cases and legitimate requests, then consolidate the prompt: group rules by purpose, remove duplicates and contradictions, rewrite prohibitions as positive instructions with reasons, and move examples into a tagged section. Re-run the eval to confirm the refusals drop while the original bugs stay fixed.

    </details>

2. Repeated requests with a long, unchanged system prompt show zero cache reads. Name two likely causes.

    <details><summary>Answer</summary>

    Something in the prefix changes per request, such as a timestamp, user ID or request ID in the system prompt, or tool definitions built in a non-deterministic order. Other causes include a prefix below the provider's minimum cacheable length or a cache breakpoint placed after volatile content. Move volatile data after the cached section and make the tool list deterministic.

    </details>

3. When should you split a task into a prompt chain instead of one prompt?

    <details><summary>Answer</summary>

    When the task has distinct sub-tasks with different needs (extraction versus drafting), when you need to inspect, validate or approve an intermediate result, when one step fails often and needs its own eval, or when steps benefit from different models. Keep one prompt when the task is simple and latency is tight.

    </details>

4. Why should rules include reasons, for example "Do not promise payment dates, because only the adjuster can commit to them"?

    <details><summary>Answer</summary>

    Reasons let the model generalise the intent to cases the rule does not literally cover (such as implying a date without stating one), reduce over-application of the rule to harmless cases, and tell future maintainers which rules are load-bearing.

    </details>

5. What is the difference between prompt engineering and context engineering, in one sentence each?

    <details><summary>Answer</summary>

    Prompt engineering is writing clear instructions and examples for a task. Context engineering is deciding everything that enters the model's window on each call (instructions, retrieved data, tool definitions and results, history, memory) and managing that budget as conversations and agent runs grow.

    </details>

6. An agent forgets the customer's account number after 30 turns. Propose two fixes.

    <details><summary>Answer</summary>

    Pin key facts in a short structured block that is always kept in context, or store them in external memory the agent can read. Also apply summarisation or compaction to older turns and clear bulky tool results, so the history does not push important facts out of the window.

    </details>

7. A prospect asks you to "just fix the prompt" so the assistant knows their latest price list. What is the real fix?

    <details><summary>Answer</summary>

    Prices are changing data, not instructions. Provide them at request time through retrieval or a tool call to the pricing system, so answers stay current without editing the prompt. Use the prompt to tell the model how to use the retrieved prices and what to do when a price is missing.

    </details>
