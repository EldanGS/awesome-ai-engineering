# Mock Exam

Sixty original, scenario-based multiple-choice questions for the [AI Solutions Engineer course](README.md), weighted by the exam blueprint. Allow **120 minutes**. Each question has one best answer. Answers and a one-line explanation are hidden under each question.

> [!IMPORTANT]
> All questions are original and written for this course. They are not taken from any vendor exam. Never use leaked or real exam content, and never let a bot or agent take this or any other exam or course on your behalf. The point is to find out what you know.

## Contents

- [How to take the exam](#how-to-take-the-exam)
- [Blueprint](#blueprint)
- [Domain 1: LLM APIs and Model Capabilities](#domain-1-llm-apis-and-model-capabilities)
- [Domain 2: Prompt and Context Engineering](#domain-2-prompt-and-context-engineering)
- [Domain 3: Building RAG Solutions](#domain-3-building-rag-solutions)
- [Domain 4: Agents, Tool Use and MCP](#domain-4-agents-tool-use-and-mcp)
- [Domain 5: Evals, Testing and Observability](#domain-5-evals-testing-and-observability)
- [Domain 6: Discovery, Demos and Proofs of Concept](#domain-6-discovery-demos-and-proofs-of-concept)
- [Domain 7: Enterprise Integration and Deployment](#domain-7-enterprise-integration-and-deployment)
- [Domain 8: Trust, Security Reviews and Customer Success](#domain-8-trust-security-reviews-and-customer-success)
- [Scoring](#scoring)

## How to take the exam

1. Set a 120-minute timer. Use no notes, documentation or AI assistants.
2. Write your answers (for example `1-B, 2-A, ...`) on paper or in a text file before opening any answer.
3. When the time is up, open the answers and score yourself per domain with the [scoring table](#scoring).
4. For every wrong answer, re-read the matching section of the domain file and write one sentence on why the correct answer is better.

## Blueprint

| Domain | Weight | Questions | Numbers |
| --- | :-: | :-: | :-: |
| 1. LLM APIs and Model Capabilities | 12% | 7 | 1-7 |
| 2. Prompt and Context Engineering | 12% | 7 | 8-14 |
| 3. Building RAG Solutions | 14% | 8 | 15-22 |
| 4. Agents, Tool Use and MCP | 14% | 9 | 23-31 |
| 5. Evals, Testing and Observability | 12% | 7 | 32-38 |
| 6. Discovery, Demos and Proofs of Concept | 14% | 9 | 39-47 |
| 7. Enterprise Integration and Deployment | 10% | 6 | 48-53 |
| 8. Trust, Security Reviews and Customer Success | 12% | 7 | 54-60 |
| **Total** | **100%** | **60** | |

## Domain 1: LLM APIs and Model Capabilities

**1.** A retailer's assistant returns a JSON object that its order system parses. About 3% of responses fail to parse because fields are renamed or missing. What is the most robust fix?

- A. Add "RESPOND ONLY IN VALID JSON" in capital letters to the system prompt.
- B. Use schema-constrained structured outputs with the order schema.
- C. Increase the maximum output tokens.
- D. Switch to the provider's largest model.

<details><summary>Answer</summary>

**B.** Schema-constrained structured outputs make the response validate against the schema; prompt wording and bigger models only reduce the error rate.

</details>

**2.** A telecom customer is evaluating a voice support agent and says callers hang up if the agent pauses. Which measurement should you prioritise in the bake-off?

- A. Total tokens per month.
- B. Time to first token (or first audio) and its p95.
- C. Maximum context window size.
- D. The model's rank on a public reasoning benchmark.

<details><summary>Answer</summary>

**B.** Perceived responsiveness in voice is dominated by how quickly the first output arrives, especially at the tail.

</details>

**3.** Your monthly cost estimate for a support agent assumed one request per ticket. The pilot bill is 2.5 times higher. Each ticket triggers about six tool calls. What did the estimate most likely miss?

- A. The cost of output tokens in the final reply.
- B. Tool definitions, history and tool results being re-sent as input on every loop iteration.
- C. Embedding costs for the user's question.
- D. Image tokens from screenshots.

<details><summary>Answer</summary>

**B.** Every agent turn re-sends the growing conversation and tool definitions as input, so input tokens scale with the number of iterations.

</details>

**4.** An insurer needs to classify two million archived documents by next week. There is no interactive user. Which approach is most cost-effective?

- A. Stream each request to reduce latency.
- B. Submit the work through the provider's discounted batch API.
- C. Use the largest model at the highest reasoning effort for every document.
- D. Use a realtime voice endpoint for throughput.

<details><summary>Answer</summary>

**B.** Batch APIs trade latency for a significant discount and suit large offline jobs.

</details>

**5.** Generated compliance reports end mid-sentence, and the API reports a "max tokens" stop reason. What should you do?

- A. Retry the identical request until it completes.
- B. Lower the sampling temperature.
- C. Add more few-shot examples of complete reports.
- D. Raise the output limit (streaming long responses) or generate the report in shorter sections.

<details><summary>Answer</summary>

**D.** The output hit the token ceiling; give it room, stream to avoid timeouts, or split the work.

</details>

**6.** A hospital network asks which of three models to use for discharge summary drafting. One model tops a public leaderboard. What do you recommend?

- A. Choose the leaderboard leader.
- B. Choose the cheapest model and add human review.
- C. Run a small eval on de-identified representative samples, on platforms the customer can procure, measuring quality, latency and cost.
- D. Fine-tune all three models before comparing.

<details><summary>Answer</summary>

**C.** The customer's task, data and procurement constraints decide the right model; leaderboards do not measure them.

</details>

**7.** A developer asks: "Once we give the model a `query_customers` tool, can it connect to our database directly?" What is accurate?

- A. No. The model only returns a request to call the tool; your application executes it with its own credentials and permissions.
- B. Yes. The model connects using credentials placed in the tool description.
- C. Only if the tool is exposed through MCP.
- D. Only when streaming is enabled.

<details><summary>Answer</summary>

**A.** Tool use is a structured request; execution, credentials and authorisation stay in your code.

</details>

## Domain 2: Prompt and Context Engineering

**8.** Repeated requests with an identical 20,000-token handbook show zero cache reads. The system prompt begins with `Current time: {now}` followed by the handbook. What is the fix?

- A. Shorten the handbook below the caching minimum.
- B. Send the handbook as a user message instead.
- C. Move the timestamp and other per-request values after the stable handbook content.
- D. Switch to a model with a larger context window.

<details><summary>Answer</summary>

**C.** Caching matches an exact prefix, so volatile values at the start invalidate the cache on every request.

</details>

**9.** A customer's prompt has grown to 25 rules starting with "NEVER". The assistant now refuses many legitimate questions. What is the best first step?

- A. Add a rule telling it not to refuse.
- B. Consolidate the rules into clear positive instructions with reasons, and test against an eval set that includes legitimate requests.
- C. Switch to a different provider.
- D. Increase the temperature so it is more willing.

<details><summary>Answer</summary>

**B.** Consolidating and explaining rules reduces over-application, and the eval proves both the refusals and the original bugs are handled.

</details>

**10.** You are building Q&A over a single 80-page contract that fits in the context window. Where should the user's question go?

- A. Before the contract, so the model knows what to look for.
- B. In the middle of the contract, near the likely answer.
- C. In a separate request without the contract.
- D. After the contract, with the contract wrapped in clearly labelled tags.

<details><summary>Answer</summary>

**D.** Placing long documents first, in tagged sections, and the question last generally gives better long-context results.

</details>

**11.** A workflow must extract invoice fields, check them against purchasing rules, then draft an email to the supplier. Auditors want to inspect the extracted values before any email is drafted. Which design fits?

- A. A prompt chain: extract to a schema, validate with code or a checking step, then draft.
- B. One large prompt that does all three steps.
- C. An autonomous agent with all tools available.
- D. A fine-tuned model that outputs the email directly.

<details><summary>Answer</summary>

**A.** Chaining exposes a validated intermediate result that can be audited and tested on its own.

</details>

**12.** In long sessions, an assistant forgets decisions made early on, and per-request cost keeps rising. What is the most appropriate change?

- A. Move to a model with the largest available context window.
- B. Restart the session every ten turns with no memory.
- C. Summarise or compact older turns, pin key facts in a short structured block, and clear stale tool results.
- D. Increase the maximum output tokens.

<details><summary>Answer</summary>

**C.** Context management keeps important facts visible while controlling the size and cost of each request.

</details>

**13.** All five few-shot examples in a prompt are short, formal replies. The assistant now replies briefly and formally even to long, casual messages that need detail. What is the likely cause and fix?

- A. The model is too small; upgrade it.
- B. The examples are too uniform; use varied examples that cover the range of expected inputs and outputs.
- C. The examples should be removed and replaced with capitalised rules.
- D. The temperature is too low; raise it.

<details><summary>Answer</summary>

**B.** Models imitate surface features of similar examples; diverse examples teach the intended behaviour.

</details>

**14.** A product manager edited the production system prompt directly in a vendor console on Friday. On Monday, ticket routing accuracy had dropped and nobody could say what changed. Which practice would have prevented this?

- A. Writing prompts in a shared spreadsheet.
- B. Allowing only one person to edit the console.
- C. Using a larger model to absorb prompt changes.
- D. Storing prompts in version control with review, and running the eval suite before each change ships.

<details><summary>Answer</summary>

**D.** Treating prompts as code gives diffs, review, rollback and an eval gate against regressions.

</details>

## Domain 3: Building RAG Solutions

**15.** Engineers search the knowledge base for part numbers such as "PX-4410-B", and the assistant often retrieves the wrong manual. Retrieval is vector-only. What should you add first?

- A. A larger generation model.
- B. More few-shot examples in the prompt.
- C. Keyword (BM25) retrieval combined with vector search, then reranking.
- D. A longer chunk size.

<details><summary>Answer</summary>

**C.** Exact identifiers are matched far better by keyword search; hybrid retrieval combines both strengths.

</details>

**16.** In your traces, the passage that answers a question is usually retrieved, but around rank 30 of 50. Only the top five passages go to the model. What is the best improvement?

- A. Add a reranker that re-scores the top 50 candidates before selecting the top five.
- B. Send all 50 passages to the model on every request.
- C. Reduce the number of retrieved candidates to ten.
- D. Fine-tune the generation model.

<details><summary>Answer</summary>

**A.** A reranker is designed to promote truly relevant candidates from a larger pool into the small context set.

</details>

**17.** A prospect wants an assistant over SharePoint for 10,000 employees with very different access rights. Which requirement is non-negotiable in your design?

- A. A single shared index with a prompt instruction to hide restricted content.
- B. Removing restricted content from answers after generation.
- C. Indexing only public documents for now and adding permissions later.
- D. Capturing permissions as metadata at ingestion and filtering retrieval by the signed-in user's identity and groups.

<details><summary>Answer</summary>

**D.** Permissions must be enforced inside retrieval; prompts and post-filtering do not prevent the model from seeing restricted content.

</details>

**18.** Answers about a rate card are wrong. Inspecting the parsed text, you see table columns merged into a single run of numbers. What should you fix?

- A. The generation prompt's tone instructions.
- B. Parsing and chunking: use a layout-aware parser and table-aware chunks that keep headers with rows.
- C. The embedding model's dimensions.
- D. The reranker's threshold.

<details><summary>Answer</summary>

**B.** The information was corrupted before indexing; no later stage can recover it.

</details>

**19.** A logistics customer wants the assistant to answer "Where is shipment 88123 right now?" What should provide the answer?

- A. A RAG index of shipment records refreshed nightly.
- B. A fine-tuned model trained on last year's shipments.
- C. A read-only tool that queries the tracking system at request time.
- D. A long-context prompt containing all active shipments.

<details><summary>Answer</summary>

**C.** Live, transactional data belongs in a system-of-record query, not in a periodically refreshed index.

</details>

**20.** You want a single number showing how often your retriever puts at least one relevant passage in the context window. Which metric fits?

- A. Recall at k.
- B. Faithfulness.
- C. BLEU score.
- D. Time to first token.

<details><summary>Answer</summary>

**A.** Recall at k measures whether a relevant passage appears in the top k retrieved results.

</details>

**21.** Many chunks read like "This limit applies to all contractors" and retrieve poorly because they do not say which policy or limit they refer to. Which technique helps most?

- A. Lower the temperature during generation.
- B. Reduce the chunk overlap to zero.
- C. Store chunks without metadata to save space.
- D. Enrich each chunk with its document title, section heading and a short generated description of its context before indexing.

<details><summary>Answer</summary>

**D.** Contextual enrichment makes otherwise ambiguous chunks retrievable by both vector and keyword search.

</details>

**22.** HR deleted an outdated travel policy from SharePoint, but two weeks later the assistant still cites it. What is the most likely root cause?

- A. The model memorised the policy during pre-training.
- B. The connector's sync does not propagate deletions to the index, and there is no reconciliation.
- C. The reranker prefers older documents.
- D. The prompt does not mention the new policy.

<details><summary>Answer</summary>

**B.** Deletions and permission changes must flow to the index through incremental sync plus periodic reconciliation.

</details>

## Domain 4: Agents, Tool Use and MCP

**23.** A bank wants "an AI agent" to onboard business customers: collect documents, extract fields, run a fixed sanctions check and create the account. Every case follows the same steps. What do you propose?

- A. A fully autonomous agent with access to all onboarding systems.
- B. A multi-agent system with one agent per step.
- C. A workflow with fixed steps, structured extraction, deterministic checks and human review of exceptions.
- D. A fine-tuned model that outputs account records.

<details><summary>Answer</summary>

**C.** When the path is known, a workflow is cheaper, more predictable and easier to evaluate than an agent.

</details>

**24.** In an MCP server for a CRM, you want account managers to pick a reusable "prepare QBR summary" template from a menu. Which MCP primitive fits?

- A. A prompt.
- B. A tool.
- C. A resource.
- D. A sampling request.

<details><summary>Answer</summary>

**A.** Prompts are user-controlled templates; tools are model-controlled actions and resources are application-controlled data.

</details>

**25.** You are deploying a shared MCP server for the company's CRM, used by hundreds of employees from different hosts. Which setup is appropriate?

- A. stdio transport with a shared admin API key.
- B. stdio transport launched separately on each laptop with a copy of the database.
- C. Streamable HTTP with no authentication behind the VPN.
- D. Streamable HTTP with OAuth-based authorisation so each request carries the user's token.

<details><summary>Answer</summary>

**D.** Remote, multi-user servers use the HTTP transport, and the specification's OAuth-based authorisation preserves per-user permissions.

</details>

**26.** A research agent sometimes calls the same search tool 40 times in a row and runs up a large bill. Which combination addresses this?

- A. Increase the maximum output tokens.
- B. Enforce step and token limits in the loop, and improve the tool's description and error messages so the agent knows when results are sufficient or why a call failed.
- C. Remove the system prompt to reduce input tokens.
- D. Switch the agent to stdio transport.

<details><summary>Answer</summary>

**B.** Hard limits bound the cost, and better tool design removes the confusion that causes repeated calls.

</details>

**27.** The model returns three tool-use blocks in one response. How should your loop return the results?

- A. Send each result in its own separate message, one per turn.
- B. Send only the first result and ignore the rest.
- C. Send all three results together in the next message, each referencing its matching tool call ID, including an error result for any that failed.
- D. Concatenate the outputs into a plain text message without IDs.

<details><summary>Answer</summary>

**C.** Results must map to their call IDs, and returning them together supports parallel tool use; failures are returned as errors, not dropped.

</details>

**28.** An executive assistant agent can read the user's inbox, browse the web and send email. Security is worried. What is the most effective mitigation?

- A. Require explicit human approval for every outbound email, or remove the send capability for this use case.
- B. Add a sentence to the prompt telling the agent to ignore malicious instructions.
- C. Use a larger model that is harder to trick.
- D. Log outbound emails for weekly review.

<details><summary>Answer</summary>

**A.** Private data plus untrusted content plus an external channel enables exfiltration; breaking or gating one leg is the reliable control.

</details>

**29.** A support assistant needs to look up orders. A developer proposes exposing a single `execute_sql(query)` tool against the production database "for flexibility". What do you recommend?

- A. Accept it, but tell the model in the prompt to write only SELECT statements.
- B. Accept it if the database is a replica.
- C. Use the tool only during the POC.
- D. Replace it with focused, read-only tools such as `get_order(order_id)` that call an API with the user's permissions.

<details><summary>Answer</summary>

**D.** Narrow, task-shaped tools limit blast radius and are easier for the model to use correctly.

</details>

**30.** Policy says refunds above 100 EUR require a supervisor. Where must this rule be enforced?

- A. In the system prompt, with an example of a refused refund.
- B. In the billing service or MCP server that executes the refund, using the authenticated user's role.
- C. In the front end, by hiding the refund button for agents.
- D. In a weekly audit of refund logs.

<details><summary>Answer</summary>

**B.** Business rules are enforced where the action executes; prompts and UI hints are not controls.

</details>

**31.** An agent must research 12 independent suppliers and compare them. With one agent, the context fills with raw web pages and quality drops. What design change fits best?

- A. Use a single agent with a larger context window.
- B. Remove the web search tool.
- C. An orchestrator that delegates each supplier to a sub-agent with a clean context and receives concise summaries back.
- D. Ask the user to research half of the suppliers.

<details><summary>Answer</summary>

**C.** Independent, parallelisable work with context overload is the case where sub-agents earn their extra cost.

</details>

## Domain 5: Evals, Testing and Observability

**32.** Your LLM judge rates answers for correctness. A sceptical evaluator asks why they should trust it. What is the strongest response?

- A. Show agreement between the judge and expert human labels on a sample, with the rubric used.
- B. Explain that the judge is the provider's largest model.
- C. Show that the judge's average score is high.
- D. Point to the judge model's benchmark results.

<details><summary>Answer</summary>

**A.** Measured agreement with human labels is the evidence that a judge's verdicts mean something.

</details>

**33.** A team tuned prompts on 50 cases and reported 96% accuracy. In the pilot, accuracy is 81%. What is the most likely explanation?

- A. The model provider changed the model.
- B. Pilot users are asking unfair questions.
- C. The temperature setting differs in the pilot.
- D. The prompts were overfitted to the cases used for tuning, and no held-out or representative set was used.

<details><summary>Answer</summary>

**D.** Reporting on the tuning set inflates results; held-out, representative data gives an honest estimate.

</details>

**34.** How should you report an agent's success on a scenario set, given that its behaviour varies between runs?

- A. Run each scenario once and report pass or fail.
- B. Run each scenario several times and report the pass rate, alongside outcome and trajectory checks.
- C. Report only the best run for each scenario.
- D. Set the temperature to zero and assume determinism.

<details><summary>Answer</summary>

**B.** Repeated runs reveal flakiness, and outcome plus trajectory checks show whether the agent did the right things.

</details>

**35.** A prompt change raises overall correctness from 86% to 90%, but one critical safety case (disclosing another customer's data) now fails. What should the CI gate do?

- A. Pass, because the average improved.
- B. Pass, and open a ticket to fix the safety case later.
- C. Block the change until the critical case passes again.
- D. Remove the safety case from the suite.

<details><summary>Answer</summary>

**C.** Critical safety cases are blocking gates, independent of aggregate scores.

</details>

**36.** Which grading method fits a ticket-routing step that outputs one of eight team labels?

- A. Exact match against the expected label, with per-class recall.
- B. An LLM judge scoring each label from 1 to 10.
- C. Human review of every case.
- D. Embedding similarity between labels.

<details><summary>Answer</summary>

**A.** Closed-set outputs are best graded deterministically, and per-class metrics expose weak categories.

</details>

**37.** A customer's VP forwards a screenshot of one bad answer and asks why it happened. What capability lets you answer within minutes?

- A. A monthly usage report.
- B. A larger eval set.
- C. A model with more parameters.
- D. Request tracing that records retrieval, tool calls and model calls per request, linked to user feedback.

<details><summary>Answer</summary>

**D.** Traces let you replay exactly what the system saw and did for that request.

</details>

**38.** The customer says success means "fewer hallucinations". Which is the best measurable version?

- A. "Users report feeling more confident in the answers."
- B. "At most 2% of answers on the 150-question eval set contain claims unsupported by the retrieved sources, as graded by a calibrated judge."
- C. "The model is newer than the current one."
- D. "Answers are longer and more detailed."

<details><summary>Answer</summary>

**B.** It names the metric, dataset, grading method and threshold.

</details>

## Domain 6: Discovery, Demos and Proofs of Concept

**39.** An account executive books a 45-minute first meeting with a prospect's operations director and asks you to "show them everything we have". What is the best plan?

- A. A complete feature tour so nothing is missed.
- B. Send a recorded demo instead of meeting.
- C. Open with discovery questions about their pain and process, then demo two or three scenarios tied to what you heard.
- D. Present the product roadmap.

<details><summary>Answer</summary>

**C.** Discovery first makes the demo relevant and memorable; feature tours rarely connect to value.

</details>

**40.** A champion is enthusiastic and requests a POC, but has no contact with whoever controls the budget and cannot describe how purchases are approved. In MEDDICC terms, which gaps are most important to close before committing significant POC effort?

- A. Economic buyer and decision process.
- B. Competition and metrics.
- C. Champion and pain.
- D. Paper process only.

<details><summary>Answer</summary>

**A.** Without access to the budget holder and a known decision path, a technical win may never turn into a decision.

</details>

**41.** Which is the best POC success criterion?

- A. "The assistant gives accurate and helpful answers."
- B. "Users like the assistant."
- C. "The solution is enterprise-ready."
- D. "On 120 real billing tickets from last quarter, at least 85% of drafted replies are approved by agents with no or minor edits, with p95 latency under 6 seconds."

<details><summary>Answer</summary>

**D.** It is specific, measurable, tied to real data and has thresholds both sides can verify.

</details>

**42.** A prospect wants six use cases proven in a three-week POC with one part-time contact. What is the best response?

- A. Agree, and work weekends to deliver.
- B. Prioritise one or two use cases by value and feasibility, put the rest explicitly out of scope, and confirm the people and data needed.
- C. Decline the POC entirely.
- D. Build generic demos of all six with synthetic data.

<details><summary>Answer</summary>

**B.** A bounded POC with committed resources ends in a decision; spreading effort across six usually ends in none.

</details>

**43.** During a live demo, the assistant gives a noticeably weaker answer than in rehearsal. What is the best reaction?

- A. Refresh the page and hope the next answer is better.
- B. Claim the answer is correct and move on quickly.
- C. Acknowledge it, explain why outputs vary and how the production design handles it (grounding, evals, review), show the citations or trace, then continue or switch to the recorded backup.
- D. End the demo early.

<details><summary>Answer</summary>

**C.** Honest narration backed by design safeguards preserves, and often increases, credibility.

</details>

**44.** What is the main purpose of a mutual action plan?

- A. A shared, dated plan from evaluation to go-live, with owners on both sides, including security review, legal and procurement steps.
- B. An internal forecast for the sales team.
- C. A technical design document for the POC.
- D. A list of product features the customer requested.

<details><summary>Answer</summary>

**A.** It makes the whole path, including paper process, visible and jointly owned.

</details>

**45.** A lender proposes, as its first AI use case, fully automated loan denials with no human review. Errors would be irreversible and regulated. What do you do?

- A. Agree, since the volume is high.
- B. Agree, but add a disclaimer to each decision.
- C. Ask for a larger budget to cover the risk.
- D. Explain the risk and steer toward a human-in-the-loop design or a lower-risk first use case such as document intake and summarisation for underwriters.

<details><summary>Answer</summary>

**D.** Good first use cases have catchable, reversible errors; steering builds credibility and a safer reference.

</details>

**46.** A technical evaluator says, "These models hallucinate, so this cannot work for us." What is the strongest response?

- A. "Our model does not hallucinate."
- B. Acknowledge the concern, ask what acceptable looks like, then show grounding with citations, the abstention behaviour and eval results on their own data.
- C. Offer a discount.
- D. Promise that the next model version will fix it.

<details><summary>Answer</summary>

**B.** Evidence on the customer's data, plus design controls, answers the objection; claims do not.

</details>

**47.** In discovery, a prospect says "our support process is slow". What is the best follow-up?

- A. "Would an AI agent help?"
- B. "Our product makes support faster. Shall I show you?"
- C. "Walk me through the last ticket that took too long. How many like it do you get each week, and what does the delay cost?"
- D. "What is your budget?"

<details><summary>Answer</summary>

**C.** Concrete stories and numbers turn vague pain into measurable success criteria.

</details>

## Domain 7: Enterprise Integration and Deployment

**48.** A manufacturer has a large AWS commitment and requires inference in eu-central-1. What should you recommend for the POC?

- A. Deliver through Amazon Bedrock in that region, after checking that the required models and features are available there.
- B. Use the first-party API in any region, because it is faster to set up.
- C. Self-host the largest open-weight model on rented GPUs.
- D. Ask the customer to waive the region requirement for the POC.

<details><summary>Answer</summary>

**A.** Using the customer's cloud and region reuses their contract and controls, and surfaces feature gaps early.

</details>

**49.** A prototype's front end calls the model API directly from the browser with an API key. What should change before a pilot?

- A. Obfuscate the key in the JavaScript bundle.
- B. Rotate the key weekly.
- C. Restrict the key to the company's IP range.
- D. Route calls through a backend or gateway that holds the key and enforces authentication, quotas and logging.

<details><summary>Answer</summary>

**D.** Client-side keys are always extractable; the key and controls belong server-side.

</details>

**50.** A support assistant's tool must read tickets as the signed-in support employee, with that employee's permissions. Which pattern is correct?

- A. A shared service account using client credentials.
- B. Delegated user authorisation, such as the authorisation code flow with on-behalf-of or token exchange to the ticketing API.
- C. A static API key stored in the system prompt.
- D. Anonymous access over a private network.

<details><summary>Answer</summary>

**B.** Delegated flows keep user-level permissions and audit trails on every tool call.

</details>

**51.** Five internal teams share one provider account. One team's batch job exhausts the rate limit and breaks the others' assistants. What is the best structural fix?

- A. Ask the batch team to run only at night.
- B. Create a separate provider account for each employee.
- C. Route all traffic through an AI gateway with per-team keys, quotas and cost attribution.
- D. Switch every team to the smallest model.

<details><summary>Answer</summary>

**C.** A gateway centralises quotas, isolation and chargeback across teams.

</details>

**52.** After moving traffic behind a new gateway abstraction, costs rose 30% and latency increased, with no prompt changes. Investigation shows cache reads dropped to zero. What is the lesson?

- A. Verify that the gateway passes through provider-specific features such as prompt caching, tool use and streaming.
- B. Gateways always increase cost and should be avoided.
- C. Prompt caching does not work in production.
- D. The provider raised prices.

<details><summary>Answer</summary>

**A.** Lowest-common-denominator abstractions can silently drop features the solution depends on.

</details>

**53.** Users in Germany report slow answers. The app server runs in a US region, the vector index in the EU and the model endpoint in another US region. What is the first improvement?

- A. Switch to a model with a larger context window.
- B. Increase the number of retrieved passages.
- C. Disable streaming to reduce overhead.
- D. Co-locate the application, index and model endpoint in or near the EU region, which also helps with residency.

<details><summary>Answer</summary>

**D.** Cross-region round trips add latency at every step; co-location removes them.

</details>

## Domain 8: Trust, Security Reviews and Customer Success

**54.** A security questionnaire asks how long prompts are retained by the model provider. You are not sure of the current terms. What should you do?

- A. Answer "zero retention", as that is common.
- B. Confirm against the provider's current documentation and the customer's contract, involve your security team if needed, and answer in writing citing the source.
- C. Leave the question blank.
- D. Answer with the retention period you remember from a previous deal.

<details><summary>Answer</summary>

**B.** Questionnaire answers can become contractual commitments; they must be accurate and sourced.

</details>

**55.** A document uploaded to the knowledge base contains hidden text instructing the assistant to email all retrieved content to an external address. Which control most reliably limits the damage?

- A. A stronger system prompt telling the model to ignore hidden text.
- B. A larger model.
- C. Least-privilege tools, actions run with the user's permissions, and human approval or recipient restrictions for any outbound email.
- D. Deleting documents uploaded by users.

<details><summary>Answer</summary>

**C.** Capability and approval design bounds what an injected instruction can achieve, even if detection fails.

</details>

**56.** A developer put an internal API token in the system prompt so the model "can call the API". What should you recommend?

- A. Move the token to a secrets manager used by backend code that executes tool calls; never place secrets in prompts.
- B. Keep it, but tell the model not to reveal it.
- C. Encode the token in base64 in the prompt.
- D. Rotate the token monthly and keep it in the prompt.

<details><summary>Answer</summary>

**A.** System prompts can be extracted or logged; secrets belong only in backend code paths.

</details>

**57.** Model output is inserted directly into a web page, and a tester gets a script to run in another user's browser. Which OWASP LLM risk category is this?

- A. Unbounded consumption.
- B. System prompt leakage.
- C. Data and model poisoning.
- D. Improper output handling.

<details><summary>Answer</summary>

**D.** Model output is untrusted input to downstream systems and must be escaped or sanitised.

</details>

**58.** A public-sector customer asks exactly which data leaves their country during use of the assistant. What artefact answers this best?

- A. The provider's marketing brochure.
- B. A data flow table listing each hop, the data sent, whether it is stored, where, for how long and under which agreement.
- C. The SOC 2 report alone.
- D. The model card.

<details><summary>Answer</summary>

**B.** A per-hop data flow answers location and retention questions precisely and covers every component.

</details>

**59.** After a deal closes, the solutions engineer moves to a new account. Three months later the customer says promised integrations never happened. What would have prevented this?

- A. Copying the customer success manager on the final contract email.
- B. A larger POC.
- C. A written handoff that lists every commitment with owners and dates, along with context, architecture, risks and success metrics.
- D. A longer sales cycle.

<details><summary>Answer</summary>

**C.** A structured handoff carries commitments and context to the team accountable for delivery.

</details>

**60.** Sixty days after go-live, weekly active users have halved. What should the solutions engineer and customer success manager do first?

- A. Analyse usage by team, feedback, traces and eval trends, and interview users and champions to find the cause before choosing fixes.
- B. Upgrade to the newest model immediately.
- C. Offer a discount at renewal.
- D. Send all users a reminder email.

<details><summary>Answer</summary>

**A.** Diagnose before acting: the cause may be quality, workflow fit, integrations or training, and each needs a different fix.

</details>

## Scoring

Count your correct answers per domain and compare with the passing standard: **70% overall (42 of 60)** and **at least 60% in every domain**.

| Domain | Questions | Correct | Domain score | 60% threshold |
| --- | :-: | :-: | :-: | :-: |
| 1. LLM APIs and Model Capabilities | 7 | | | 5 |
| 2. Prompt and Context Engineering | 7 | | | 5 |
| 3. Building RAG Solutions | 8 | | | 5 |
| 4. Agents, Tool Use and MCP | 9 | | | 6 |
| 5. Evals, Testing and Observability | 7 | | | 5 |
| 6. Discovery, Demos and Proofs of Concept | 9 | | | 6 |
| 7. Enterprise Integration and Deployment | 6 | | | 4 |
| 8. Trust, Security Reviews and Customer Success | 7 | | | 5 |
| **Total** | **60** | | | **42 overall** |

| Score | Next step |
| --- | --- |
| Below 60% | Work through the full [10-week plan](study-plan.md) before retaking. |
| 60% to 69% | Revisit the domains below threshold and redo their labs. |
| 70% to 79% | Pass. Strengthen weak domains, then start the [capstone](capstone.md). |
| 80% or higher | Ready for the capstone and a vendor exam from [certifications.md](../certifications.md). |
