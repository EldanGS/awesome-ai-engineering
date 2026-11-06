# Domain 7: Enterprise Integration and Deployment

**Weight: 10%.** Core question: *how does this run inside the customer's identity, network, cloud and budget?*

A POC that runs on your laptop with a personal API key proves the model works. It does not prove the solution can be deployed. Enterprise customers ask how users sign in, how the assistant reaches SharePoint without copying everything, whether traffic stays on a private network, which cloud contract pays for it, and who gets the bill. This domain gives you the integration patterns and vocabulary to answer those questions and to design a POC that is already halfway to production.

## Contents

- [Learning objectives](#learning-objectives)
- [Core concepts](#core-concepts)
- [Patterns and anti-patterns](#patterns-and-anti-patterns)
- [Reading list](#reading-list)
- [Free credentials](#free-credentials)
- [Hands-on lab: gateway and cloud deployment](#hands-on-lab-gateway-and-cloud-deployment)
- [Review questions](#review-questions)

## Learning objectives

- [ ] Explain SSO (SAML, OIDC), SCIM provisioning and OAuth flows, and choose the right one for users, services and agents.
- [ ] Design data connectors for common enterprise sources with permission sync and incremental updates.
- [ ] Explain the role of an AI or API gateway: authentication, routing, quotas, logging, caching and fallbacks.
- [ ] Compare first-party model APIs with cloud marketplace access (Amazon Bedrock, Azure AI Foundry, Google Cloud Vertex AI).
- [ ] Describe private networking options and data residency controls on each major cloud.
- [ ] Engineer latency: streaming, model choice, caching, parallelism, region placement.
- [ ] Build a cost model with budgets, chargeback, quotas and monitoring.
- [ ] Plan a production rollout: environments, CI/CD, canary releases, fallbacks and incident response.

## Core concepts

### Reference integration architecture

```text
Users (browser, Teams or Slack, CRM sidebar)
   |  SSO via the customer's identity provider (OIDC or SAML)
   v
Application backend (customer cloud or vendor SaaS)
   |-- authorisation: user identity, groups, tenant
   |-- retrieval: vector + keyword index, filtered by ACL
   |-- tools / MCP servers: CRM, ticketing, ERP (on-behalf-of user tokens)
   |-- conversation store and memory (encrypted, retention policy)
   v
AI gateway (keys, routing, quotas, logging, caching, fallback)
   v
Model endpoint: first-party API | Bedrock | Azure AI Foundry | Vertex AI | self-hosted open weights
   (private networking where required, region pinned for residency)

Cross-cutting: secrets manager, observability (traces, cost), audit log, CI/CD with eval gates
```

Sketch this diagram with the customer early. It is the map for the security review, the integration work and the cost model.

### Identity and access

| Need | Standard or pattern | Notes |
| --- | --- | --- |
| Users sign in with corporate accounts | SSO with OIDC or SAML through Entra ID, Okta, Google Workspace, Ping and similar | Required by almost every enterprise. Enforce MFA through the identity provider. |
| Accounts created and removed automatically | SCIM provisioning | Offboarding must revoke access quickly. |
| Groups drive permissions | Group claims in tokens, synced to the app | Needed for document ACL filtering and role-based features. |
| App calls an API as the user | OAuth 2.0 authorisation code flow, on-behalf-of or token exchange | Keeps the user's permissions on every tool call. |
| Service calls an API as itself | OAuth client credentials, managed identities, workload identity federation | Use for background jobs; scope tightly. Avoid long-lived static keys. |
| Agent or MCP server reaches a protected resource | OAuth 2.1 based authorisation in the MCP specification, protected resource metadata | Tokens are scoped to the user and the server. |
| Secrets for model APIs | Secrets manager (AWS Secrets Manager, Azure Key Vault, Google Secret Manager, Vault), rotation | Never in code, notebooks, or front-end bundles. |

### Data connectors

| Source type | Examples | Integration considerations |
| --- | --- | --- |
| Document stores | SharePoint, OneDrive, Google Drive, Box, Confluence | Permission sync (including inherited and link-shared items), incremental change feeds, deleted items, file formats. |
| Ticketing and CRM | ServiceNow, Zendesk, Jira, Salesforce, HubSpot | Prefer live API tools for current records; index only stable content such as knowledge articles. |
| Data warehouses | Snowflake, BigQuery, Databricks, Redshift | Text-to-SQL or semantic layer tools with read-only roles, row-level security, query limits. |
| Communication | Email, Slack, Teams | High sensitivity; strict scoping, retention and consent. Treat content as untrusted input. |
| Line-of-business APIs | ERP, billing, internal services | Wrap as tools or MCP servers with narrow scopes and clear owners. |

Build versus buy: many platforms ship managed connectors (including MCP-based connectors and cloud services such as Bedrock Knowledge Bases or Azure AI Search indexers). Use them for the POC when permissions and sync behaviour meet requirements; custom connectors are justified for unusual systems or strict control needs.

### AI gateways

An AI gateway sits between applications and model endpoints. Large customers often already run an API gateway and will expect to route AI traffic through it.

| Capability | Why the customer wants it |
| --- | --- |
| Central key management | Applications never hold provider keys; keys rotate centrally. |
| Authentication and per-team quotas | Prevents one team exhausting shared rate limits or budget. |
| Routing and fallbacks | Route by model alias; fail over to another region or provider on errors. |
| Logging and cost attribution | Token usage per app, team and tenant for chargeback. |
| Policy enforcement | PII redaction, content filters, allowed models list. |
| Caching | Response caching for repeated identical requests (separate from provider prompt caching). |

Options include open-source proxies such as LiteLLM, cloud API management products (for example Azure API Management's generative AI gateway features), and commercial AI gateways. A minimal LiteLLM proxy configuration with a fallback:

```yaml
model_list:
  - model_name: assistant-default
    litellm_params:
      model: anthropic/claude-opus-5-5
      api_key: os.environ/ANTHROPIC_API_KEY
  - model_name: assistant-fallback
    litellm_params:
      model: bedrock/<model-or-inference-profile-id>  # replace with an ID enabled in your account
      aws_region_name: eu-central-1

router_settings:
  fallbacks:
    - assistant-default: ["assistant-fallback"]
```

Check that the gateway passes through the provider features you rely on (tool use, structured outputs, prompt caching, streaming). Lowest-common-denominator abstractions can silently drop them.

### Cloud marketplaces and model platforms

Many enterprises buy models through their existing cloud provider because it reuses their contract, committed spend, IAM, networking and compliance approvals.

| Dimension | First-party API | Amazon Bedrock | Azure AI Foundry | Google Cloud Vertex AI |
| --- | --- | --- | --- | --- |
| Billing | Direct contract with the model provider | AWS bill; can count toward AWS commitments | Azure bill or Microsoft Marketplace | Google Cloud bill |
| Identity | Provider API keys or workload identity | AWS IAM roles and policies | Entra ID, Azure RBAC | Google Cloud IAM, service accounts |
| Private networking | Varies by provider | VPC endpoints (PrivateLink) | Private endpoints, virtual network integration | Private Service Connect, VPC Service Controls |
| Model catalogue | That provider's models | Many providers (Anthropic, Meta, Mistral, Amazon and others) | OpenAI, Anthropic, open-weight and Microsoft models | Gemini, Anthropic, open-weight models |
| Platform extras | Newest features first | Knowledge Bases, Agents, Guardrails | AI Search, Agent Service, content safety | Vector Search, Agent Builder, grounding |

Feature availability and release timing differ between a provider's own API and each cloud. Before you promise a feature, check the cloud's documentation for that model and region. Calling a model through a cloud uses that cloud's SDK or a provider SDK with a cloud-specific client:

```python
import os
import boto3

bedrock = boto3.client("bedrock-runtime", region_name="eu-central-1")
response = bedrock.converse(
    modelId=os.environ["BEDROCK_MODEL_ID"],  # a model or inference profile enabled in this account
    messages=[{"role": "user", "content": [{"text": "Summarise this claim in two sentences: ..."}]}],
    inferenceConfig={"maxTokens": 512},
)
print(response["output"]["message"]["content"][0]["text"])
print(response["usage"])
```

```python
from anthropic import AnthropicVertex

client = AnthropicVertex(project_id="acme-ai-prod", region="europe-west1")
message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=512,
    messages=[{"role": "user", "content": "Summarise this claim in two sentences: ..."}],
)
```

### Latency engineering

| Lever | Effect | Notes |
| --- | --- | --- |
| Streaming | Lower perceived latency | Always for user-facing text. |
| Smaller or faster model for the route | Lower TTFT and total time | Validate quality with evals. |
| Lower reasoning effort | Fewer thinking tokens | Per-route tuning. |
| Shorter outputs | Lower total time | Output length is the largest latency driver. |
| Prompt caching | Lower TTFT on long prefixes | Stable-first prompt ordering (Domain 2). |
| Parallel calls | Lower wall-clock for independent steps | Retrieval, classification and lookups in parallel. |
| Region placement | Lower network round trips; residency | Keep app, data and model in the same region where possible. |
| Precomputation | No model call at request time | Summaries, embeddings and classifications done in batch. |
| Speculative UI | Show retrieved sources or a plan while the answer generates | Perceived speed and transparency. |

### Cost management

| Practice | Implementation |
| --- | --- |
| Budget per environment and team | Provider spend limits, cloud budgets and alerts, gateway quotas. |
| Unit economics | Track cost per task (per ticket, per document), not just monthly spend. |
| Chargeback | Tag requests with app, team and tenant at the gateway; report monthly. |
| Optimisation levers | Caching, routing, batch for offline work, context trimming, output limits, effort tuning. |
| Capacity planning | Request rate-limit increases or provisioned throughput before pilots; load test. |
| Price change watch | Re-run the cost model when prices or models change. |

### From POC to production

| Stage | What changes |
| --- | --- |
| POC | Vendor or sandbox environment, sample data, a few users, manual deployment. |
| Pilot | Customer tenant or approved cloud, SSO, real data with permissions, monitoring, 10 to 100 users, support process. |
| Production | Infrastructure as code, separate dev, staging and prod, CI/CD with eval gates, canary or percentage rollouts, runbooks, on-call, SLOs. |

Reliability patterns: retries with backoff, timeouts, fallback models or regions, graceful degradation (for example "search results only" mode when generation is unavailable), idempotent tool actions, and clear user messaging during incidents. Plan model upgrades as releases: run the eval suite, canary, then switch the alias.

## Patterns and anti-patterns

| Pattern | Why it works |
| --- | --- |
| Run the POC in the cloud and region the customer will buy through | Feature and procurement surprises surface early. |
| Route all model traffic through one gateway | Central control of keys, quotas, logging and cost. |
| On-behalf-of tokens for tools | Permissions and audit trails remain intact. |
| Live tools for transactional data, indexes for documents | Freshness without copying systems of record. |
| Model aliases in config, upgrades through CI with evals | Safe, fast model changes. |
| Cost per task on the dashboard from day one | Budget conversations are grounded in data. |

| Anti-pattern | What goes wrong |
| --- | --- |
| Personal API keys in a shared POC repo | Key leakage; no attribution or control. |
| Front-end code calling the model API directly with a key | Anyone can extract and abuse the key. |
| Nightly full copy of the CRM into a vector index | Stale data, permission drift, unnecessary data exposure. |
| A gateway abstraction that strips tool use or caching | Quality or cost regressions nobody notices. |
| Designing on a feature that is not available in the customer's cloud region | Rework or a lost deal at deployment. |
| No rate-limit planning before a pilot launch | Errors on day one with all pilot users watching. |

## Reading list

- [aws-samples/amazon-bedrock-samples](https://github.com/aws-samples/amazon-bedrock-samples): Bedrock examples, including RAG, agents and guardrails.
- [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai): Vertex AI notebooks and samples.
- [Azure-Samples/azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo): enterprise RAG on Azure with authentication and access control.
- [BerriAI/litellm](https://github.com/BerriAI/litellm) and [docs](https://docs.litellm.ai): open-source AI gateway and SDK.
- [vllm-project/vllm](https://github.com/vllm-project/vllm) ([docs](https://docs.vllm.ai)): self-hosted serving for open-weight models.
- [What is Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), [Azure AI Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/), [Generative AI on Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/overview).
- Claude on clouds: [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), [Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai), [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry); and [Claude partner models on Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude) (Google Cloud docs).
- [Azure API Management generative AI gateway capabilities](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).
- [AWS Well-Architected Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html).
- [Microsoft identity platform: OAuth 2.0 client credentials flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-client-creds-grant-flow), [OAuth 2.0 overview](https://oauth.net/2/) and [RFC 9728: OAuth 2.0 Protected Resource Metadata](https://www.rfc-editor.org/rfc/rfc9728).
- [Claude pricing](https://platform.claude.com/docs/en/about-claude/pricing), [batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing) and [OpenAI latency optimization](https://platform.openai.com/docs/guides/latency-optimization).

## Free credentials

| Credential | Provider | Why it fits this domain |
| --- | --- | --- |
| [Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock) | Anthropic Academy | Building on Claude through AWS. |
| [Claude with Google Cloud's Vertex AI](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai) | Anthropic Academy | Building on Claude through Google Cloud. |
| [Introduction to generative AI and agents](https://learn.microsoft.com/en-us/training/modules/fundamentals-generative-ai/) | Microsoft Learn | Azure generative AI and agent concepts. |
| [Scale AI in your organization](https://learn.microsoft.com/en-us/training/modules/scale-ai/) | Microsoft Learn | Organisational rollout considerations. |

## Hands-on lab: gateway and cloud deployment

**Goal:** move the Domain 3 or Domain 4 POC from a laptop to an enterprise-shaped deployment.

1. Put a LiteLLM proxy (or your cloud's API management gateway) in front of all model calls. Define a model alias, a fallback, a per-key budget and request logging. Remove provider keys from the application.
2. Add SSO to the demo front end with a free developer tenant of an identity provider (Entra ID, Okta or Auth0 developer accounts) using OIDC. Pass group claims to the retriever for ACL filtering.
3. Deploy the backend to one cloud using a managed container service, with secrets in the cloud secrets manager. Call a model through that cloud's model platform (Bedrock, Azure AI Foundry or Vertex AI) in a region of your choice.
4. Measure p50 and p95 latency for 50 requests from the deployed environment with and without prompt caching, and with streaming on.
5. Force the primary model to fail (invalid model name or a blocked region) and confirm the fallback works and is logged.
6. Build a cost dashboard or report: cost per request and per user from the gateway logs, and a projection for 500 users.

**Deliverable:** an architecture diagram, `deployment.md` describing identity, network, secrets, gateway, region and fallback choices, a latency table, the failover test result and the cost projection. Tear down cloud resources afterwards to avoid charges.

## Review questions

1. A customer has a large committed-spend agreement with one cloud provider and strict procurement rules. Why does this affect your deployment recommendation?

    <details><summary>Answer</summary>

    Buying model access through that cloud's marketplace or model platform can draw down existing commitments, reuse the approved vendor relationship, IAM, networking and compliance controls, and avoid a new procurement cycle. Check that the required models and features are available there in the needed region, and run the POC on that platform.

    </details>

2. Why is calling the model API directly from browser JavaScript with an API key unacceptable?

    <details><summary>Answer</summary>

    The key is exposed to anyone who opens the page, allowing abuse and cost exposure, and there is no server-side place to enforce authentication, permissions, quotas, logging or content policies. Calls must go through a backend or gateway that holds the key securely.

    </details>

3. Which OAuth pattern should a support agent tool use to read a customer's tickets as the signed-in support employee?

    <details><summary>Answer</summary>

    A delegated, user-context flow: the user signs in via the authorisation code flow, and the backend uses the user's token or an on-behalf-of or token exchange flow to call the ticketing API. This preserves the employee's permissions and audit trail. Client credentials are for service-level background jobs, not user actions.

    </details>

4. Name four capabilities an AI gateway gives an enterprise.

    <details><summary>Answer</summary>

    Central key management and rotation; per-team authentication, quotas and budgets; routing with model aliases and fallbacks; logging and cost attribution for chargeback; policy enforcement such as PII redaction and allowed model lists; optional response caching.

    </details>

5. The POC used a feature from the provider's own API, but the customer will deploy through a cloud marketplace. What do you check?

    <details><summary>Answer</summary>

    Whether that feature, model version and region are available on the customer's cloud platform, any differences in API shape, limits or pricing, and whether their gateway passes the feature through. Re-run the eval and latency tests on the target platform before the readout.

    </details>

6. Users in Frankfurt see slow responses. Name three latency levers to investigate.

    <details><summary>Answer</summary>

    Region placement (run the app, data and model endpoint in or near the EU region), streaming, a faster model or lower reasoning effort for the route, shorter outputs, prompt caching for long prefixes and parallelising retrieval and lookups.

    </details>
