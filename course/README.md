# AI Solutions Engineer Certification Prep Course

A free, open, self-paced course that prepares you for the **AI Solutions Engineer** role: the pre-sales builder who runs discovery, designs and ships proofs of concept, demos live systems to technical and executive buyers, and earns the trust of security reviewers. It also prepares you for the vendor exams and free credentials that test the same skills (Anthropic, OpenAI, Microsoft, Google Cloud, AWS, LangChain, Hugging Face). It combines:

- **8 domains** with learning objectives, core concepts, decision frameworks, short code snippets and curated reading from GitHub and official docs.
- **Hands-on labs** you can run on a laptop with free tiers or a small API budget.
- **Free credentials** mapped to each domain from the [Free AI Certifications Tracker](../free-certifications/README.md).
- **Review questions** per domain, a **60-question mock exam** and a **capstone** proof of concept you could show a real customer.

> [!IMPORTANT]
> This is a study course, not an exam dump. All questions are original. Never use real exam content, and never let a bot or agent take a course, quiz or exam on your behalf. Using automation to earn credentials breaks most providers' terms, can get your account and credentials revoked, and defeats the purpose: customers and interviewers test the skill, not the badge.

## Contents

- [Who this is for](#who-this-is-for)
- [What makes this role different](#what-makes-this-role-different)
- [Exam blueprint](#exam-blueprint)
- [Study plans](#study-plans)
- [Domains](#domains)
- [How to use this course](#how-to-use-this-course)
- [Earn the completion badge](#earn-the-completion-badge)

## Who this is for

| You are | Start at |
| --- | --- |
| Software engineer moving into a customer-facing role | Domain 1, then follow the 10-week plan. Spend extra time on Domains 6 and 8. |
| Traditional sales engineer or solutions consultant new to LLMs | Domains 1 to 5 first; you already know half of Domain 6. |
| ML or data engineer who wants to work with customers | Skim Domains 1 and 3, start properly at Domain 4, then 6 to 8. |
| Already running AI proofs of concept | Take the [mock exam](mock-exam.md) first and study your weakest domains. |

Prerequisites: comfort with Python, HTTP and JSON APIs, Git, a terminal, and explaining technical ideas out loud. You need an API key for at least one model provider (most offer free or low-cost trial credit) and optionally a local model runtime such as Ollama.

## What makes this role different

An AI Solutions Engineer sits between the account executive, the customer's engineers and your own product team. Compared with an AI Solution Architect, the role is closer to the keyboard and closer to the deal:

| Dimension | AI Solution Architect | AI Solutions Engineer |
| --- | --- | --- |
| Primary output | Target architecture, ADRs, reference designs | Working POC, live demo, integration code, eval report |
| Time horizon | Quarters to years | Days to weeks per opportunity |
| Success measured by | Design quality, long-term fit | Technical win, agreed success criteria met, smooth handoff |
| Key audiences | Enterprise architects, CIO staff | Developers, champions, security reviewers, economic buyers |
| Typical failure | Over-designing before value is proven | Shipping a demo that cannot survive real data or a security review |

The course is built around that loop: **qualify, discover, define success, build, evaluate, demo, secure, hand off.**

## Exam blueprint

The mock exam and the review questions follow this weighting. It mirrors what vendor AI engineering exams and solutions-engineering interview loops emphasize in late 2026: building grounded and agentic systems quickly, proving them with evals, and getting them through enterprise procurement.

| # | Domain | Weight | Core question a solutions engineer must answer |
| :-: | --- | :-: | --- |
| 1 | [LLM APIs and Model Capabilities](01-llm-apis-and-models.md) | 12% | Which model and API features fit this workload, and what will it cost? |
| 2 | [Prompt and Context Engineering](02-prompt-and-context-engineering.md) | 12% | What does the model need to see, in what order, to do this reliably? |
| 3 | [Building RAG Solutions](03-rag-solutions.md) | 14% | How do we ground answers in the customer's own data, with citations? |
| 4 | [Agents, Tool Use and MCP](04-agents-tools-and-mcp.md) | 14% | When does this need an agent, and how do we connect it to real systems safely? |
| 5 | [Evals, Testing and Observability](05-evals-and-observability.md) | 12% | How do we prove it works, and keep proving it after go-live? |
| 6 | [Discovery, Demos and Proofs of Concept](06-discovery-demos-and-pocs.md) | 14% | Is this a real opportunity, what does winning look like, and how do we show it? |
| 7 | [Enterprise Integration and Deployment](07-enterprise-integration.md) | 10% | How does this run inside the customer's identity, network, cloud and budget? |
| 8 | [Trust, Security Reviews and Customer Success](08-trust-security-and-success.md) | 12% | Will security sign off, and will the customer still be using it in a year? |

Passing standard for the mock exam: **70%** overall and at least **60%** in every domain.

## Study plans

| Plan | Hours per week | Schedule |
| --- | :-: | --- |
| Sprint | 15-20 | 4 weeks: two domains per week, mock exam and capstone in week 4. |
| Standard | 8-10 | 10 weeks: see [study-plan.md](study-plan.md). |
| Part-time | 4-5 | 16 weeks: one domain every two weeks. |

## Domains

Each domain file has the same structure:

1. **Learning objectives** you can check off.
2. **Core concepts** with tables, decision frameworks and short code snippets.
3. **Patterns and anti-patterns** from real customer engagements.
4. **Reading list** from GitHub and official documentation.
5. **Free credentials** to earn for this domain.
6. **Hands-on lab** with a concrete deliverable.
7. **Review questions** with hidden answers.

After the domains:

- [Mock exam](mock-exam.md): 60 scenario questions, 120 minutes.
- [Capstone](capstone.md): an end-to-end proof of concept with discovery notes, success criteria, a working demo, an eval report, a demo script and a security one-pager, graded with a rubric.
- [Vendor certifications](../certifications.md): which paid exam to take next and how this course maps to it.

## How to use this course

1. Fork the repository so you can tick checkboxes and keep notes.
2. Take the [mock exam](mock-exam.md) cold to find your baseline. Do not look at the answers yet.
3. Work through the domains in order. Do every lab: solutions engineers who have built the thing give better demos and better answers in the room.
4. Earn the free credentials listed in each domain as you go. Do the work yourself.
5. Practise out loud. Each domain's review questions are also good mock discovery or objection-handling prompts; answer them to a peer in under two minutes.
6. Retake the mock exam. Aim for 80% before booking a vendor exam or a customer-facing interview loop.
7. Complete the [capstone](capstone.md) and ask a peer to play the customer and grade it with the rubric.

## Earn the completion badge

When you pass the mock exam and complete the capstone, add this badge to your profile README and link it to your capstone repository:

```markdown
[![AI Solutions Engineer Prep](https://img.shields.io/badge/AI%20Solutions%20Engineer-Prep%20Complete-5f3dc4)](https://github.com/EldanGS/awesome-ai-engineering/tree/main/course)
```

The badge is a self-declared record of study, not a vendor certification. Pair it with a vendor exam from [certifications.md](../certifications.md) for a recognized credential.
