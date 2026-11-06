# Domain 6: Discovery, Demos and Proofs of Concept

**Weight: 14%.** Core question: *is this a real opportunity, what does winning look like, and how do we show it?*

This is the domain that separates a solutions engineer from a developer. Technical brilliance spent on an unqualified opportunity, a vague POC or a demo that answers questions nobody asked is wasted. Here you learn to run discovery, qualify, define success criteria with the customer, scope a POC that ends in a decision, and give demos that make the buyer's problem feel solved.

## Contents

- [Learning objectives](#learning-objectives)
- [Core concepts](#core-concepts)
- [Patterns and anti-patterns](#patterns-and-anti-patterns)
- [Reading list](#reading-list)
- [Free credentials](#free-credentials)
- [Hands-on lab: discovery to POC plan](#hands-on-lab-discovery-to-poc-plan)
- [Review questions](#review-questions)

## Learning objectives

- [ ] Plan and run a technical discovery call that uncovers pain, current process, data, constraints and decision process.
- [ ] Qualify an AI opportunity with a MEDDICC-style framework and spot missing elements.
- [ ] Assess AI use-case fit: value, feasibility, data readiness, risk and measurability.
- [ ] Write success criteria that are specific, measurable and agreed in writing.
- [ ] Scope a POC with timeline, data, environment, roles, exit criteria and a decision date.
- [ ] Build and maintain a mutual action plan with the customer.
- [ ] Design and deliver a demo that leads with the outcome, uses the customer's context and recovers gracefully from model surprises.
- [ ] Handle common technical objections during discovery and demos.

## Core concepts

### The solutions engineer's deal loop

```text
qualify -> discover -> align on success criteria -> tailored demo -> scoped POC
       -> readout against criteria -> security and procurement -> close -> handoff to success
```

You will often move back a step: a demo reveals a new stakeholder, a POC surfaces a data problem. That is normal; the mutual action plan keeps it visible.

### Running discovery

Discovery is not a questionnaire. It is a structured conversation that leaves both sides understanding the problem better. Prepare a hypothesis, ask open questions, then dig.

| Area | Example questions | What you are listening for |
| --- | --- | --- |
| Business pain | "What happens today when a claim email arrives? Where does it hurt?" | A quantified, owned problem, not curiosity. |
| Current process | "Walk me through the last time this went wrong." | Steps, systems, hand-offs, volumes, exceptions. |
| Impact | "What does a day of delay cost? How many people do this?" | Numbers you can use for value and success criteria. |
| Users | "Who would use this daily? How technical are they?" | UX needs, change management, champions. |
| Data | "Where does the information live? Can we see ten real examples?" | Formats, quality, access, sensitivity, ownership. |
| Systems and integration | "Which systems must it read from or write to? What identity provider?" | Integration scope, SSO, network constraints. |
| Constraints | "Any rules on where data can be processed? Approved clouds?" | Residency, procurement path, security review. |
| Prior attempts | "Have you tried to solve this before? What happened?" | Hidden objections and political history. |
| Decision | "Who else needs to be comfortable before this goes ahead? How have you bought similar tools?" | Economic buyer, process, paperwork, timeline. |
| Success | "Six months after launch, what would make you say this worked?" | The raw material for success criteria. |

Techniques that work:

- **Ask for artefacts.** Real (sanitised) emails, documents, screenshots and ticket exports reveal more than any description.
- **Quantify.** Every pain should end in a number: volume, time, cost, error rate, revenue at risk.
- **Summarise back.** End the call with "Here is what I heard..." and send it in writing the same day.
- **Separate wants from needs.** "We want an agent" is a solution request; find the outcome underneath.

### Qualifying with MEDDICC

MEDDICC is a widely used enterprise qualification framework. Solutions engineers own or contribute to several of its elements.

| Letter | Element | What it means for an AI opportunity | SE contribution |
| --- | --- | --- | --- |
| M | Metrics | Quantified business outcome (hours saved, resolution rate, revenue) | Translate pain into measurable success criteria and eval metrics. |
| E | Economic buyer | Person with budget authority who can say yes | Prepare an executive-level readout they will care about. |
| D | Decision criteria | Technical, security, commercial requirements used to choose | Shape criteria toward what the solution does well; make them testable. |
| D | Decision process | Steps and people from evaluation to signature | Map technical steps: POC, security review, architecture board. |
| I | Identify pain | The business problem and its cost | Validate the pain with data and real examples. |
| C | Champion | Insider with influence who sells for you | Equip them with demo recordings, eval results and answers for their peers. |
| C | Competition | Alternatives, including "build it ourselves" and "do nothing" | Differentiate with evidence, not claims. |

Many teams add **P for paper process** (legal, procurement and security paperwork), which for AI deals often includes data processing agreements and AI-specific security questionnaires (Domain 8). Missing elements are not a reason to stop; they are a to-do list. A POC without an economic buyer or decision process is a red flag.

### Is it a good AI use case?

| Dimension | Strong signal | Weak signal |
| --- | --- | --- |
| Value | Large volume, expensive manual work, clear owner | Nice to have, no budget owner |
| Feasibility | Task is language or document heavy, tolerant of review | Requires perfect accuracy with no human check |
| Data readiness | Accessible, representative samples available now | "We will have the data next quarter" |
| Measurability | Historical outcomes exist to compare against | No baseline, subjective success |
| Risk | Errors are catchable and reversible | Errors cause irreversible harm or legal exposure |
| Integration | Clear entry and exit points in existing workflow | Requires replacing core systems first |

Score each dimension and discuss the weak ones openly. Steering a customer toward a better first use case builds more credibility than agreeing to a poor one.

### Writing success criteria

Success criteria turn a POC from an open-ended experiment into a decision. Write them with the customer, get them agreed in writing, and design your eval (Domain 5) to measure them.

| Weak | Strong |
| --- | --- |
| "Accurate answers" | "At least 90% of answers rated correct by two HR specialists on a 100-question set drawn from last quarter's tickets." |
| "Fast" | "p95 response time under 5 seconds for single-turn questions in the pilot environment." |
| "Secure" | "Passes the information security review using the standard AI vendor questionnaire; no customer data retained by the model provider beyond the agreed period." |
| "Users like it" | "At least 70% of 20 pilot agents rate it useful after two weeks; median handling time for billing tickets down 20%." |
| "Integrates with our systems" | "Reads tickets from the helpdesk API and writes internal notes; SSO via the corporate identity provider." |

### Scoping a POC

A good POC is short, bounded and ends in a decision.

| Element | Guidance |
| --- | --- |
| Objective | One or two business questions the POC must answer. |
| Scope | In-scope use cases, documents, systems and users. Explicitly list what is out of scope. |
| Success criteria | The agreed table above, with how each will be measured. |
| Data | What samples, how they are provided, how they are protected and deleted. |
| Environment | Your sandbox, the customer's cloud tenant, or a marketplace deployment. Decide early; it drives security approvals. |
| Timeline | Typically two to six weeks, with weekly check-ins and a fixed readout date. |
| Roles | Customer champion, data owner, technical contact, security contact; your SE, AE and any specialists. |
| Exit | A readout meeting with the economic buyer and a decision: proceed, change scope, or stop. |

A POC that is "free, open-ended and with whoever is available" usually becomes a science project. Ask for commitment in return for your effort: data access, named people, a decision date. A paid pilot is often the better path when the scope is large.

### The mutual action plan

A mutual action plan (MAP) is a shared, dated list of steps from today to go-live, owned by both sides. It exposes the paper process early and keeps momentum.

| Date | Milestone | Owner (customer) | Owner (vendor) | Status |
| --- | --- | --- | --- | --- |
| Week 1 | Discovery summary and success criteria agreed | Champion | SE | Done |
| Week 1 | Sample data delivered under NDA | Data owner | SE | In progress |
| Week 2 | Security questionnaire sent | Security lead | SE | Not started |
| Week 3 | Mid-POC check-in with live demo | Champion | SE | Not started |
| Week 4 | Readout to economic buyer | Economic buyer | AE and SE | Not started |
| Week 5 | Commercial proposal and DPA review | Procurement and legal | AE | Not started |
| Week 7 | Pilot start with 20 users | Operations lead | SE and CSM | Not started |

### Demo craft

A demo is a story about the customer's problem being solved, not a feature tour.

| Principle | In practice |
| --- | --- |
| Lead with the outcome | Show the end result first ("here is the reply drafted, policy cited, in 4 seconds"), then how it works. |
| Use their world | Their terminology, document types, sample data and systems, even if mocked. |
| Tell, show, tell | Say what you will show and why it matters, show it, then summarise the value. |
| Fewer, deeper moments | Three scenarios tied to the top pains beat twelve features. |
| Show the hard case | Include one messy input and one "I do not know" response; it builds trust. |
| Make it observable | Show citations, tool calls or a trace so technical evaluators see it is real. |
| Stop and ask | Check reactions after each scenario; let them drive. |

Non-determinism is the special risk of AI demos. Prepare for it:

- Rehearse every scenario many times and know the failure modes.
- Pin model versions and settings for the demo environment; record which you used.
- Keep a recorded backup of each scenario and fixed sample data.
- Use caching and pre-warmed environments to keep latency predictable.
- If the model surprises you live, narrate it: explain why it happened and how the production design handles it (evals, guardrails, review). Handled well, this often increases credibility.

### Handling technical objections

Use a simple structure: **acknowledge, clarify, respond with evidence, confirm.**

| Objection | Clarify | Respond with |
| --- | --- | --- |
| "It hallucinates." | "Where have you seen that, and what would acceptable look like?" | Grounding with citations, abstention behaviour, eval results on their data, human review design. |
| "We will build it ourselves." | "What would your team need, and by when?" | Time to value, maintenance burden (evals, model upgrades, connectors), and offer to support their build if that is the right answer. |
| "Our data cannot leave our environment." | "Is that a cloud region rule, a tenant rule, or no third-party processing at all?" | Deployment options (cloud marketplace in their region, private networking, open-weight self-hosting), data retention terms. |
| "It is too expensive." | "Compared with what baseline?" | Cost per task against the cost of the manual process; levers such as routing, caching and batch. |
| "Competitor X scored higher on a benchmark." | "Which tasks matter most for you?" | A side-by-side on their eval set. |

## Patterns and anti-patterns

| Pattern | Why it works |
| --- | --- |
| Written discovery summary within 24 hours | Shows listening, corrects misunderstandings early, arms the champion. |
| Success criteria signed off before building | The POC ends in a decision, not a debate. |
| Two-week POC sprints with a demo at each check-in | Momentum and early course correction. |
| Steering to a feasible first use case | Credibility and a reference customer. |
| Mutual action plan shared in a common document | Paper process and blockers surface early. |
| A recorded demo the champion can forward | Your story reaches people who were not in the room. |

| Anti-pattern | What goes wrong |
| --- | --- |
| Demoing before discovery | Generic demo, no connection to pain, easy to forget. |
| Open-ended free POC with no exit criteria | Months of work, no decision. |
| Building on synthetic data only | The real data breaks it in the pilot. |
| Over-promising roadmap features to win | Trust collapses at implementation. |
| Ignoring the security team until the end | A late security review delays or kills the deal. |
| Feature tours ("and here is another setting...") | The buyer cannot connect features to value. |

## Reading list

- [MEDDICC](https://meddicc.com): the qualification framework and its terminology.
- [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/define-success) (Claude docs): writing measurable criteria.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): useful for steering prospects from "agents" to the simplest working pattern.
- [Anthropic customer stories](https://www.anthropic.com/customers): reference patterns by industry for discovery hypotheses.
- [streamlit/streamlit](https://github.com/streamlit/streamlit) ([docs](https://docs.streamlit.io)) and [gradio-app/gradio](https://github.com/gradio-app/gradio) ([docs](https://www.gradio.app/docs)): fast demo front ends in Python.
- [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts): starter apps to adapt into tailored demos.
- [openai/openai-realtime-agents](https://github.com/openai/openai-realtime-agents): a reference for voice agent demos.
- Books worth finding in a library: *The Great Demo!* by Peter Cohan and *Mastering Technical Sales* by John Care and Aron Bohlig.

## Free credentials

| Credential | Provider | Why it fits this domain |
| --- | --- | --- |
| [Scope AI Solutions](https://academy.openai.com/public/courses/scope-ai-solutions-kjplw) | OpenAI Academy | Scoping AI use cases and defining value. |
| [Deploying Claude Enterprise with confidence](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence) | Anthropic Academy | The decisions enterprise buyers make during rollout. |
| [Create business value with AI](https://learn.microsoft.com/en-us/training/modules/create-business-value/) | Microsoft Learn | Framing AI value for business stakeholders. |
| [Leverage AI tools and resources for your business](https://learn.microsoft.com/en-us/training/modules/leverage-ai-tools/) | Microsoft Learn | Use-case identification. |
| [Discovering High-Value Opportunities for Agentic AI](https://learning.sap.com/courses/discovering-high-value-opportunities-for-agentic-ai) | SAP Learning | Prioritising agentic use cases. |
| [Change Management for AI Implementation](https://trailhead.salesforce.com/content/learn/modules/change-management-for-ai-implementation) | Salesforce Trailhead | Adoption planning that starts in discovery. |

## Hands-on lab: discovery to POC plan

**Goal:** run a realistic discovery and produce the documents that start a POC. Work with a partner who plays the customer.

1. Your partner picks a company profile (for example a 2,000-person logistics firm, a regional hospital network, or a B2B SaaS company) and privately writes a hidden brief: real pain, volumes, data situation, a hidden constraint (such as a data residency rule) and a sceptical stakeholder.
2. Prepare a one-page call plan: hypothesis, ten open questions, artefacts to request.
3. Run a 30-minute discovery call. Record it with consent, or take notes.
4. Within 24 hours, send a discovery summary: pain and impact with numbers, current process, users, data, systems, constraints, stakeholders, open questions.
5. Fill in a MEDDICC table with evidence and gaps for each element.
6. Score the use case on value, feasibility, data readiness, measurability, risk and integration. Recommend a first use case.
7. Write the success criteria table (at least five criteria) and a POC scope (objective, in and out of scope, data, environment, timeline, roles, exit).
8. Draft a mutual action plan to go-live.
9. Build a 10-minute demo for the top pain using a quick front end and sample data, deliver it to your partner, and ask them to raise two objections.

**Deliverable:** `discovery-summary.md`, `meddicc.md`, `poc-plan.md` (including success criteria and MAP) and a short recording or script of the demo. Your partner scores the call using the capstone rubric's discovery row.

## Review questions

1. A director asks for a POC next week "to see what AI can do for us". There is no defined use case, data owner or budget. What do you do?

    <details><summary>Answer</summary>

    Do not start building. Propose a short discovery workshop to identify and prioritise use cases with business owners, quantify pain, check data availability and identify the economic buyer and decision process. Offer a tailored demo of a likely use case to keep momentum, and scope a POC only once success criteria, data and a decision path exist.

    </details>

2. Rewrite "the assistant should be accurate" as a POC success criterion.

    <details><summary>Answer</summary>

    For example: "On a 100-question evaluation set drawn from last quarter's real HR tickets, at least 90% of answers are rated correct by two HR specialists, and the assistant correctly declines at least 90% of questions not covered by the policy documents."

    </details>

3. In MEDDICC, what is the difference between decision criteria and decision process?

    <details><summary>Answer</summary>

    Decision criteria are the requirements the customer uses to choose (accuracy thresholds, security requirements, cost, integration). Decision process is the sequence of steps and people involved in reaching and executing the decision (POC, security review, architecture board, procurement, signature).

    </details>

4. During a live demo, the model gives a different and weaker answer than in rehearsal. How do you respond?

    <details><summary>Answer</summary>

    Stay calm and narrate: acknowledge the variation, explain why models can vary and how the production design handles it (grounding, evals, guardrails, human review), and if useful show the trace or citations. Then move on, or switch to the recorded backup. Afterward, add the case to the eval set and investigate.

    </details>

5. Why ask for a decision date and named customer contacts before agreeing to a free POC?

    <details><summary>Answer</summary>

    It tests whether the opportunity is real and gives the POC an end point. Without committed people, data access and a decision meeting, POCs drift, consume the SE team's time and rarely convert. Mutual commitment is a qualification signal.

    </details>

6. A prospect insists "We will build this ourselves with open-source tools." How do you handle it?

    <details><summary>Answer</summary>

    Acknowledge it as a legitimate option and clarify their team's capacity, timeline and what they would need to maintain (evals, connectors, security, model upgrades, support). Compare time to value and total cost of ownership with evidence. If building is genuinely right for them, offer to help with the platform pieces they would still use; credibility is worth more than a forced deal.

    </details>

7. What belongs in a mutual action plan beyond technical milestones?

    <details><summary>Answer</summary>

    The paper process and people: security questionnaire and review, legal and data processing agreement review, procurement steps, the economic buyer readout, budget approval, pilot user onboarding and handoff to customer success, each with an owner on both sides and a date.

    </details>

8. Name three ways to make an AI demo resilient to non-determinism.

    <details><summary>Answer</summary>

    Rehearse each scenario repeatedly and know its failure modes; pin model versions and settings in the demo environment with fixed sample data; keep recorded backups; pre-warm caches and environments for predictable latency; and include a planned "I do not know" case so variation is framed as designed behaviour.

    </details>
