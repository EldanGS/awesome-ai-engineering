# 10-Week Study Plan

The standard plan for the [AI Solutions Engineer course](README.md): 8 to 10 hours per week, one domain per week for eight weeks, then two weeks for the capstone and the final mock exam. Each week mixes reading, building and speaking practice, because the role demands all three.

> [!IMPORTANT]
> Do the work yourself. Never use bots or AI agents to take courses, quizzes or exams on your behalf. Using AI tools to help you build labs is fine and expected; letting them earn your credentials is not.

## Contents

- [Before you start](#before-you-start)
- [Weekly rhythm](#weekly-rhythm)
- [Plan at a glance](#plan-at-a-glance)
- [Week by week](#week-by-week)
- [Progress tracker](#progress-tracker)
- [Adjusting the plan](#adjusting-the-plan)

## Before you start

- [ ] Fork the repository and create a private notes file or folder for your labs.
- [ ] Get API access to at least one model provider and set a monthly spending limit. Optionally install Ollama for local models.
- [ ] Set up Python 3.11 or later, Git, and a code editor.
- [ ] Find a study partner who can play the customer in discovery and demo practice (weeks 6, 9 and 10).
- [ ] Take the [mock exam](mock-exam.md) cold, in 120 minutes, without looking at answers. Record your score per domain.

## Weekly rhythm

| Block | Time | Activity |
| --- | :-: | --- |
| Read | 2-3 h | Core concepts and two or three items from the reading list. |
| Build | 4-5 h | The domain's hands-on lab. |
| Credential | 1 h | One free credential from the domain list. |
| Speak | 30 min | Answer three review questions out loud, as if to a customer, in under two minutes each. Record yourself once a week. |
| Review | 30 min | Review questions in writing; note weak spots for the next mock exam. |

## Plan at a glance

| Week | Focus | Lab deliverable | Checkpoint |
| :-: | --- | --- | --- |
| 0 | Baseline | Mock exam score per domain | Know your weakest domains |
| 1 | [Domain 1: LLM APIs and Model Capabilities](01-llm-apis-and-models.md) | `model-selection.md` | Explain TTFT, tokens and cost to a non-engineer |
| 2 | [Domain 2: Prompt and Context Engineering](02-prompt-and-context-engineering.md) | `prompt-rescue.md` | Cache hit rate above zero on repeat calls |
| 3 | [Domain 3: Building RAG Solutions](03-rag-solutions.md) | `rag-report.md` | Hybrid retrieval beats vector-only on your set; zero permission leaks |
| 4 | [Domain 4: Agents, Tool Use and MCP](04-agents-tools-and-mcp.md) | `agent-design.md` | Injected ticket handled safely |
| 5 | [Domain 5: Evals, Testing and Observability](05-evals-and-observability.md) | `eval-report.md` | Judge agreement measured; CI gate working |
| 6 | [Domain 6: Discovery, Demos and Proofs of Concept](06-discovery-demos-and-pocs.md) | Discovery summary, MEDDICC, POC plan | Partner rates your discovery call |
| 7 | [Domain 7: Enterprise Integration and Deployment](07-enterprise-integration.md) | `deployment.md` | Fallback test passes; cost projection done |
| 8 | [Domain 8: Trust, Security Reviews and Customer Success](08-trust-security-and-success.md) | `security-pack/`, `handoff.md` | Red-team findings fixed by design changes |
| 9 | [Capstone](capstone.md) build | Working demo, eval report | Success criteria measured |
| 10 | Capstone readout and final [mock exam](mock-exam.md) | Recorded demo, all capstone artefacts | 70% overall, 60% per domain; peer rubric score |

## Week by week

### Week 1: LLM APIs and model capabilities

- [ ] Read Domain 1 core concepts and the request anatomy table until you can map the three APIs from memory.
- [ ] Make a streamed call and a structured-output call with two providers.
- [ ] Complete the model bake-off lab.
- [ ] Credential: Building with the Claude API or Optimize AI Application Performance.
- [ ] Speaking drill: "Why not just send everything in the long context window?"

### Week 2: Prompt and context engineering

- [ ] Read Domain 2 and the context engineering article in the reading list.
- [ ] Complete the prompt rescue lab, including the prompt chain experiment.
- [ ] Verify prompt caching with usage fields.
- [ ] Credential: AI Fluency for builders or the Google Skills *Prompt Design in Agent Platform* skill badge.
- [ ] Speaking drill: "The customer wants you to just fix the prompt."

### Week 3: Building RAG solutions

- [ ] Read Domain 3 and the contextual retrieval article.
- [ ] Complete the grounded policy assistant lab with hybrid retrieval, reranking and ACL filtering.
- [ ] Inspect parser output for five difficult pages before indexing.
- [ ] Credential: Introduction to retrieval-augmented generation concepts or Google Skills *Vector Search and Embeddings*.
- [ ] Speaking drill: "Should we fine-tune on our knowledge base instead?"

### Week 4: Agents, tool use and MCP

- [ ] Read Domain 4 and the building effective agents article.
- [ ] Build the two MCP servers and test them with the MCP Inspector.
- [ ] Complete the support triage agent lab with approvals and step limits.
- [ ] Credential: Introduction to Model Context Protocol or Microsoft Applied Skills *Integrate model context protocol tools with agents in Microsoft Foundry*.
- [ ] Speaking drill: "Do we need an autonomous agent for this?"

### Week 5: Evals, testing and observability

- [ ] Read Domain 5 and two of the eval articles in the reading list.
- [ ] Complete the eval harness lab: calibrated judge, traces, CI gate.
- [ ] Retake the mock exam questions for Domains 1 to 5 only; compare with week 0.
- [ ] Credential: Google Skills *Machine Learning Operations (MLOps) for Generative AI* or AWS MLOps Demonstrated.
- [ ] Speaking drill: present your eval results in three minutes to an "executive".

### Week 6: Discovery, demos and proofs of concept

- [ ] Read Domain 6.
- [ ] Run the discovery call with your partner and send the summary within 24 hours.
- [ ] Write the MEDDICC table, success criteria, POC plan and mutual action plan.
- [ ] Deliver a 10-minute demo and handle two objections.
- [ ] Credential: Scope AI Solutions or Create business value with AI.

### Week 7: Enterprise integration and deployment

- [ ] Read Domain 7.
- [ ] Complete the gateway and cloud deployment lab; tear down resources afterwards.
- [ ] Credential: Claude with Amazon Bedrock, Claude with Google Cloud's Vertex AI, or a Microsoft Learn module for your target cloud.
- [ ] Speaking drill: "Our data cannot leave our AWS account."

### Week 8: Trust, security reviews and customer success

- [ ] Read Domain 8 and the OWASP Top 10 for LLM Applications.
- [ ] Complete the security pack lab, including the red-team exercise and two design fixes.
- [ ] Write the customer success handoff document.
- [ ] Credential: Microsoft Applied Skills *Secure AI solutions in the cloud* or Google Skills *Security in the World of AI*.
- [ ] Speaking drill: "Will you train on our data?" and "What if someone hijacks it with a prompt?"

### Week 9: Capstone build

- [ ] Choose a capstone scenario and write discovery notes and success criteria (with your partner as the customer).
- [ ] Build the working demo, reusing your lab code.
- [ ] Build the eval set and run the eval; fix the top failure category.
- [ ] Draft the security one-pager.

### Week 10: Capstone readout and final exam

- [ ] Write the demo script and rehearse it three times; record a backup.
- [ ] Deliver the readout to your partner or a peer and have them score it with the [capstone rubric](capstone.md#grading-rubric).
- [ ] Take the full [mock exam](mock-exam.md) under timed conditions. Target 80% or higher.
- [ ] Add the completion badge to your profile and link it to your capstone repository.
- [ ] Choose a vendor exam from [certifications.md](../certifications.md) and book it.

## Progress tracker

| Domain | Baseline mock (%) | Week 5 mock (%) | Final mock (%) | Lab done | Credential earned |
| --- | :-: | :-: | :-: | :-: | :-: |
| 1. LLM APIs and Model Capabilities | | | | [ ] | [ ] |
| 2. Prompt and Context Engineering | | | | [ ] | [ ] |
| 3. Building RAG Solutions | | | | [ ] | [ ] |
| 4. Agents, Tool Use and MCP | | | | [ ] | [ ] |
| 5. Evals, Testing and Observability | | | | [ ] | [ ] |
| 6. Discovery, Demos and Proofs of Concept | n/a | | | [ ] | [ ] |
| 7. Enterprise Integration and Deployment | n/a | | | [ ] | [ ] |
| 8. Trust, Security Reviews and Customer Success | n/a | | | [ ] | [ ] |

Fill in the baseline column for all domains in week 0; the "n/a" cells only apply to the week 5 partial retake.

## Adjusting the plan

| Situation | Adjustment |
| --- | --- |
| Strong engineering background, new to customer-facing work | Compress weeks 1 to 4 into three weeks; give Domain 6 two weeks and add extra mock discovery calls. |
| Experienced sales engineer, new to LLMs | Give Domains 3 to 5 extra time; skim the discovery material in Domain 6 and focus on AI-specific success criteria and demo risks. |
| Limited API budget | Use small or local models for most lab runs and the large model only for final comparisons; set provider spend limits. |
| Falling behind | Keep the labs, drop optional reading. The labs feed the capstone. |
