# Capstone: End-to-End Proof of Concept

The capstone is a complete proof of concept, run as if for a real customer: from discovery notes to a working demo, an eval report, a rehearsed demo script and a security one-pager. It pulls together every domain of the [AI Solutions Engineer course](README.md). A peer plays the customer and grades your work with the rubric at the end.

> [!IMPORTANT]
> Build and present the capstone yourself. AI coding assistants are fine for writing code, as they would be on the job, but the discovery, decisions, analysis and readout must be your own work. Never let a bot or agent complete courses, exams or this capstone on your behalf.

## Contents

- [Outcome](#outcome)
- [Choose a scenario](#choose-a-scenario)
- [Ground rules](#ground-rules)
- [Deliverables](#deliverables)
- [Step-by-step](#step-by-step)
- [Readout format](#readout-format)
- [Grading rubric](#grading-rubric)
- [Submission checklist](#submission-checklist)

## Outcome

By the end you will have a public (or shareable) repository that shows a hiring manager or customer exactly how you work: how you listen, how you scope, how you build, how you prove quality and how you earn trust.

## Choose a scenario

Pick one scenario or propose your own with similar scope. Your peer reviewer receives the hidden brief for the scenario you choose (they should invent the details in the "hidden" column before your discovery call, without showing you).

| Scenario | Customer | Problem | Hidden details your peer invents |
| --- | --- | --- | --- |
| A. Claims intake copilot | Regional insurer, 1,200 staff | Claim emails and attachments are triaged by hand; 2-day backlog | Volumes, a residency rule, a sceptical claims director, the system of record |
| B. IT service desk agent | 5,000-employee manufacturer | Repetitive tickets (access, devices, VPN) swamp the service desk | Ticket mix, identity provider, which actions are allowed, change-management concerns |
| C. Contract review assistant | Mid-size law or procurement team | Reviewing supplier contracts against a playbook takes days | Playbook rules, confidentiality limits, approved cloud, who signs off |
| D. Sales knowledge assistant | B2B SaaS company, 300 sellers | Sellers cannot find answers in product docs, past RFPs and pricing | Content sources, permissions by region, pricing sensitivity, CRM |
| E. Patient communications drafting | Outpatient clinic network | Staff draft replies to patient portal messages | De-identified data only, clinical safety rules, required human review |

## Ground rules

- Use only public, synthetic or properly licensed data. Never use real personal data or confidential material.
- The solution must include **retrieval over documents** and **at least one tool** (via MCP or direct tool use) that reads from or writes to a simulated system of record.
- At least one action must require **human approval**.
- Use any model provider or platform. Record model identifiers and settings in configuration.
- Budget: keep total API spend modest (set a provider spending limit). Use small or local models where they meet the bar.
- Time box: about 20 to 25 hours across weeks 9 and 10 of the [study plan](study-plan.md).

## Deliverables

| # | Deliverable | File | What it proves |
| :-: | --- | --- | --- |
| 1 | Discovery notes and qualification | `01-discovery.md` | You can uncover pain, numbers, constraints and the decision path. |
| 2 | Success criteria and POC plan | `02-success-criteria.md` | You can turn pain into measurable, agreed criteria and a bounded plan. |
| 3 | Working demo | `app/` plus `README.md` run instructions | You can build a grounded, tool-using solution that runs. |
| 4 | Eval report | `04-eval-report.md` plus eval code and data | You can prove quality with honest, reproducible evidence. |
| 5 | Demo script and recording | `05-demo-script.md` plus a video link or file | You can tell the customer's story and handle surprises. |
| 6 | Security one-pager | `06-security-one-pager.md` | You can earn a security team's trust. |
| 7 | Handoff note (short) | `07-handoff.md` | You can set customer success up to win. |

## Step-by-step

### 1. Discovery notes

Run a 30-minute discovery call with your peer playing the customer. Then write `01-discovery.md`:

- Company context and stakeholders (names can be fictional), with roles.
- Pain in the customer's words, quantified: volumes, time, cost, error rates.
- Current process, step by step, with systems involved.
- Data: sources, formats, quality, sensitivity, access.
- Constraints: identity provider, approved cloud and region, residency, regulatory points.
- A MEDDICC table with evidence and gaps for each element.
- Use-case fit scores (value, feasibility, data readiness, measurability, risk, integration) and your recommendation.
- Open questions and how you will close them.

### 2. Success criteria and POC plan

Write `02-success-criteria.md` and get your peer to "sign off" in writing (a comment or a reply is enough):

| Criterion | Metric | Measurement method | Threshold | Agreed by |
| --- | --- | --- | --- | --- |
| Example: draft quality | Share of drafts approved with no or minor edits | Two reviewers grade 60 held-out cases | At least 80% | Claims operations lead |

Include at least five criteria covering quality, safety (for example correct abstention or zero permission leaks), latency, cost per task and one business outcome proxy. Add the POC scope (in and out), data handling, environment, timeline, roles and a short mutual action plan to a go or no-go decision.

### 3. Working demo

Build the solution in `app/`. Minimum technical requirements:

- [ ] Retrieval with hybrid search (vector plus keyword) and citations shown in the UI.
- [ ] Document-level permission filtering for at least two simulated user roles.
- [ ] At least one tool, preferably an MCP server, against a simulated system of record.
- [ ] Human approval for at least one write action, enforced server-side.
- [ ] Streaming responses.
- [ ] Structured outputs for any machine-consumed step.
- [ ] Tracing with token usage, latency and cost per request.
- [ ] Model identifiers and key settings in configuration; no secrets in code.
- [ ] A `README.md` with one-command or few-command setup.

### 4. Eval report

Write `04-eval-report.md` with the eval code and data alongside:

- Dataset: size (at least 60 cases), sources, categories, how labels were produced, held-out split.
- Graders: deterministic checks, the judge rubric, and judge agreement with your hand labels.
- Results against every success criterion, on the held-out set, with per-category breakdown.
- Retrieval metrics (recall at k, MRR) separate from answer metrics.
- Agent or tool scenarios run multiple times, with pass rates.
- A red-team section: at least 15 attacks (direct and indirect injection, permission bypass, prompt extraction) and outcomes.
- Failure analysis: categories, counts, examples, root causes and fixes, with before and after numbers for at least one fix.
- Cost per task and a monthly projection at the customer's volume.
- A three-sentence executive summary and a go, change-scope or stop recommendation.

### 5. Demo script

Write `05-demo-script.md` for a 15-minute demo to a mixed audience (economic buyer, champion, technical evaluator, security lead):

- Opening: the customer's pain and the agreed success criteria, in their words (one minute).
- Three scenarios tied to the top pains, each in tell, show, tell form, including one messy input and one "not in the sources" response.
- A moment that makes it observable: citations, a trace or the approval step.
- The eval headline numbers and one honest failure category with its fix.
- Planned responses to three likely objections.
- A recovery plan for model surprises and a recorded backup.
- Close: proposed next steps from the mutual action plan.

Record the demo (screen recording is fine) and link it.

### 6. Security one-pager

Write `06-security-one-pager.md` for the customer's CISO, on a single page:

- Architecture and data flow diagram.
- Data flow table: hop, data, stored or not, location, retention, controls.
- Identity and access: SSO, roles, delegated tool permissions, approvals.
- Model provider data handling: training use, retention, region, with links to the provider's documentation.
- Prompt injection and agent safety controls, mapped to the relevant OWASP Top 10 for LLM Applications items.
- Logging, audit and incident contacts.
- Known limitations and items "not currently supported", with mitigations.

### 7. Handoff note

Write a short `07-handoff.md` (one to two pages): business context, what was proven, commitments made, risks, adoption plan, success metrics for 30, 60 and 90 days, and two expansion use cases.

## Readout format

Hold a 45-minute session with your peer reviewer playing the customer's team:

| Segment | Time | Content |
| --- | :-: | --- |
| Recap | 5 min | Pain, success criteria, what you built. |
| Live demo | 15 min | Follow your demo script. |
| Results | 10 min | Eval report highlights against criteria, failures and fixes, cost. |
| Security and trust | 5 min | Walk through the one-pager. |
| Questions and objections | 10 min | Your peer asks at least three hard questions or objections. |

## Grading rubric

Your peer scores each row from 1 to 4. Multiply by the weight. Maximum score is 100. **Pass: 70 or more, with no row scored 1.**

| Criterion | Weight | 1: Not yet | 2: Developing | 3: Proficient | 4: Exemplary |
| --- | :-: | --- | --- | --- | --- |
| Discovery and qualification | 3 | Generic notes; no numbers; MEDDICC missing | Some pain and constraints; several MEDDICC gaps unacknowledged | Quantified pain, process, data, constraints; MEDDICC with gaps and plans | Uncovers the hidden constraint and sceptic; steers to the best first use case with clear reasoning |
| Success criteria and POC plan | 3 | Vague goals | Some measurable criteria; scope unclear | Five or more measurable criteria with thresholds, agreed; bounded scope; MAP | Criteria tied directly to business value and the eval design; MAP includes paper process with owners |
| Working demo: grounding and retrieval | 3 | Breaks or answers without sources | Runs; vector-only retrieval; citations inconsistent | Hybrid retrieval, citations in UI, correct abstention | Reranking, contextual enrichment or parent-child retrieval with measured gains |
| Working demo: tools, permissions and approvals | 3 | No tool or permissions | Tool works; permissions only in the prompt | MCP or tool with server-side permissions and approval for writes | Delegated identity, least privilege, clear tool design, injection cases handled by design |
| Eval rigour | 4 | Anecdotes only | Small set; judge uncalibrated; no held-out set | Representative set, held-out results, calibrated judge, retrieval and answer metrics, repeated agent runs | Failure taxonomy with before and after fixes; CI gate; red-team results integrated |
| Engineering quality | 2 | Hard-coded secrets; cannot run | Runs with effort; little configuration | Clean setup, config for models, tracing with cost and latency | Production-minded: gateway or fallback, tests, clear structure |
| Demo delivery | 3 | Feature tour; loses the audience | Some tailoring; weak story | Outcome-led, tailored scenarios, observable moment, objections handled | Handles a live surprise gracefully; audience leaves with clear next steps |
| Security one-pager and trust | 2 | Missing or marketing claims | Partial data flow; vague controls | Complete data flow, accurate provider terms with sources, OWASP mapping | Precise, honest limitations; would pass a first CISO review |
| Handoff and customer success | 2 | Missing | Context only | Commitments, risks, adoption plan, metrics | Value review plan and expansion paths with sponsors |

Weights add to 25; with a maximum of 4 points per row, the maximum score is 100.

## Submission checklist

- [ ] Repository contains all seven deliverables and the app runs from the README.
- [ ] No real personal data, secrets or confidential material anywhere in the repository or its history.
- [ ] Success criteria sign-off from your peer is recorded.
- [ ] Eval code and data are included and reproducible.
- [ ] Demo recording is linked.
- [ ] Peer rubric scores are recorded in the repository `README.md`.
- [ ] Mock exam passed at 70% overall and 60% per domain.
- [ ] Completion badge added to your profile, linking to the capstone repository:

```markdown
[![AI Solutions Engineer Prep](https://img.shields.io/badge/AI%20Solutions%20Engineer-Prep%20Complete-5f3dc4)](https://github.com/EldanGS/awesome-ai-engineering/tree/main/course)
```
