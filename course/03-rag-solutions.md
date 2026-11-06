# Domain 3: Building RAG Solutions

**Weight: 14%.** Core question: *how do we ground answers in the customer's own data, with citations?*

Retrieval-augmented generation (RAG) is the most common first production use case a solutions engineer will build: an assistant that answers from policies, manuals, tickets, contracts or a knowledge base. RAG demos are easy; RAG that survives the customer's real documents, permissions and edge cases is not. Most failures are retrieval failures, so this domain spends as much time on ingestion and search as on generation.

## Contents

- [Learning objectives](#learning-objectives)
- [Core concepts](#core-concepts)
- [Patterns and anti-patterns](#patterns-and-anti-patterns)
- [Reading list](#reading-list)
- [Free credentials](#free-credentials)
- [Hands-on lab: grounded policy assistant](#hands-on-lab-grounded-policy-assistant)
- [Review questions](#review-questions)

## Learning objectives

- [ ] Decide between long context, RAG, tools over live systems and fine-tuning for a given knowledge problem.
- [ ] Build an ingestion pipeline: parse, clean, chunk, enrich with metadata, embed, index, refresh.
- [ ] Choose chunking strategies for prose, tables, code and semi-structured documents.
- [ ] Combine dense (vector) and sparse (keyword, BM25) retrieval and add a reranker.
- [ ] Enforce document-level permissions at retrieval time.
- [ ] Generate answers with citations and a defined behaviour when the answer is not in the sources.
- [ ] Diagnose a bad answer as a retrieval, context or generation problem.
- [ ] Measure retrieval quality (recall, precision, MRR) and answer quality (faithfulness, relevance).

## Core concepts

### Which knowledge pattern fits?

| Situation | Best fit | Why |
| --- | --- | --- |
| A few documents that fit comfortably in the window, asked about repeatedly | Long context plus prompt caching | Simplest; no index to maintain. |
| Large or growing document collection; answers need citations | RAG | Selects relevant passages; scales; cites sources. |
| Data lives in a system of record and changes constantly (orders, inventory, tickets) | Tools or API calls (Domain 4) | Query live data rather than copying it into an index. |
| Structured analytics questions ("revenue by region last quarter") | Text-to-SQL or a semantic layer tool | Numbers must come from the database, not from text chunks. |
| The model needs a new skill, format or tone, not new facts | Prompting first; fine-tuning only with evidence | Fine-tuning teaches behaviour, not reliable recall of changing facts. |
| Relationships across many entities ("which suppliers share a parent company") | Graph-enhanced retrieval | Vector similarity alone misses multi-hop relationships. |

Many real solutions combine these: RAG for policy text, a tool for live account data, and long context for the single contract the user uploaded.

### The RAG pipeline

```text
Ingestion (offline, scheduled or event-driven)
  sources -> connectors -> parse -> clean -> chunk -> enrich metadata -> embed -> index
                                                                           |
Query time (online)                                                        v
  question -> rewrite or expand -> retrieve (vector + keyword, filtered by ACL) -> rerank
           -> assemble context (top passages + metadata) -> generate with citations -> verify
```

Every arrow is a place where quality can be lost. When a customer reports a bad answer, walk the pipeline backwards: was the right passage in the index, was it retrieved, did it survive reranking and context assembly, and did the model use it correctly?

### Parsing and chunking

Parsing is underrated. PDFs with columns, headers, footers, tables and scanned pages produce garbage text if parsed naively. Use layout-aware parsers (such as Docling or Unstructured) or a model with native PDF input for difficult files, and inspect the output by eye before you embed anything.

| Strategy | How it works | Good for | Risk |
| --- | --- | --- | --- |
| Fixed size with overlap | Split every N tokens with some overlap | Quick baseline | Cuts sentences, tables and sections mid-way. |
| Structure-aware | Split on headings, sections, list items, paragraphs | Manuals, policies, documentation | Uneven chunk sizes; very long sections need a second split. |
| Semantic | Split where topic similarity drops | Long unstructured prose | More compute; harder to debug. |
| Table-aware | Keep a table whole, or one row per chunk with headers repeated | Price lists, specs, rate cards | Large tables exceed chunk limits. |
| Parent-child (small-to-big) | Retrieve small chunks, return the larger parent section to the model | Precise matching with enough context to answer | More storage and indexing logic. |
| Contextual enrichment | Prepend a short, generated description of where the chunk sits in the document | Chunks that are ambiguous out of context ("the limit is 30 days") | Ingestion cost; caching the source document helps. |

Always attach **metadata** to each chunk: source URI, title, section path, last modified date, owner, document type, language, and the access control list (ACL) or group IDs. Metadata powers filtering, citations, freshness and permissions.

### Embeddings and indexes

An embedding model turns text into a vector so that similar meanings are close together. Choices that matter in a POC:

| Decision | Guidance |
| --- | --- |
| Embedding model | Pick one that supports the customer's languages and domain; compare two on a small retrieval eval. Changing it later means re-embedding everything. |
| Vector store | Use what the customer already runs if it is good enough (pgvector in Postgres, OpenSearch, Azure AI Search, Vertex AI Vector Search, MongoDB Atlas). Dedicated stores (Qdrant, Weaviate, Chroma, LanceDB) are fine for POCs and many productions. |
| Dimensions and quantisation | Smaller or quantised vectors cut cost and memory at some recall loss; measure. |
| Index refresh | Decide how deletions and updates propagate. Stale or deleted documents in the index are a compliance risk. |

### Hybrid retrieval and reranking

Vector search is good at meaning; keyword search is good at exact terms such as product codes, error numbers, names and acronyms. Hybrid retrieval runs both and merges the results (for example with reciprocal rank fusion). A **reranker** (a cross-encoder or a model-based scorer) then re-orders the top 20 to 100 candidates by true relevance before you keep the top few.

```python
def reciprocal_rank_fusion(result_lists, k=60):
    """Merge several ranked lists of document IDs into one ranking."""
    scores = {}
    for results in result_lists:
        for rank, doc_id in enumerate(results):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank + 1)
    return sorted(scores, key=scores.get, reverse=True)

dense_ids = vector_search(query, top_k=50, filter={"groups": user.groups})
sparse_ids = bm25_search(query, top_k=50, filter={"groups": user.groups})
candidates = reciprocal_rank_fusion([dense_ids, sparse_ids])[:40]
top_passages = rerank(query, candidates)[:6]
```

Note the `filter` on both searches: permissions are applied **inside** retrieval, not after generation.

### Query transformation

| Technique | When it helps |
| --- | --- |
| Query rewriting | Conversational follow-ups ("what about for contractors?") need the earlier context folded in. |
| Multi-query expansion | Vague questions benefit from several phrasings retrieved in parallel. |
| Decomposition | Compound questions ("compare the EU and US refund policies") need one retrieval per part. |
| Metadata extraction | "Policies updated this year for Germany" becomes a filter, not just text. |
| Hypothetical answer embedding | Embedding a draft answer can match documents better than a short question; test before relying on it. |

### Generation with citations

The generation prompt must tell the model to answer only from the provided sources, cite them, and say clearly when the sources do not contain the answer.

```python
import anthropic

client = anthropic.Anthropic()

documents = [
    {
        "type": "document",
        "source": {"type": "text", "media_type": "text/plain", "data": p.text},
        "title": p.title,
        "citations": {"enabled": True},
    }
    for p in top_passages
]

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    system=(
        "Answer employee HR questions using only the provided documents. "
        "If the documents do not answer the question, say so and suggest contacting HR."
    ),
    messages=[{"role": "user", "content": [*documents, {"type": "text", "text": question}]}],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
        for c in block.citations or []:
            print("  source:", c.document_title, "|", c.cited_text[:80])
```

Native citation features return the exact cited span, which you can show in the UI and verify. Where they are not available, ask for passage IDs in a structured output and check that every cited ID was actually provided.

### Permissions, freshness and data hygiene

| Requirement | Implementation |
| --- | --- |
| Users see only what they are allowed to see | Store ACLs or group IDs with each chunk; filter at query time with the user's identity from SSO. Never rely on the prompt to hide content. |
| Deleted or revoked documents disappear | Incremental sync that handles deletes; periodic full reconciliation; test it in the POC. |
| Answers reflect the latest version | Last-modified metadata, freshness boosts, de-duplication of old versions. |
| Sensitive data is handled correctly | Classify at ingestion; redact or exclude restricted fields; log what was indexed. |

### Diagnosing bad answers

| Symptom | Likely layer | First check |
| --- | --- | --- |
| Answer is wrong and the right document exists | Retrieval | Is the right chunk in the top 20? Try hybrid search, better chunking, query rewriting. |
| Right chunk retrieved but answer still wrong | Context or generation | Was the chunk cut off, buried among many others, or contradicted by an old version? |
| Confident answer with no support | Generation | Strengthen the "answer only from sources" and "not found" instructions; check citations. |
| Answer correct but cites the wrong source | Citation mapping | Verify passage IDs; use native citations. |
| Works in English, fails in German | Embeddings or parsing | Multilingual embedding model; language metadata; test set per language. |
| User sees content they should not | Permissions | ACL filtering at retrieval; this is a stop-ship issue. |

### Measuring RAG quality

| Metric | Layer | Question it answers |
| --- | --- | --- |
| Recall at k | Retrieval | Is at least one relevant passage in the top k? |
| Precision at k | Retrieval | How much of what we retrieved is relevant? |
| Mean reciprocal rank (MRR) | Retrieval | How high does the first relevant passage rank? |
| Faithfulness or groundedness | Generation | Is every claim in the answer supported by the retrieved context? |
| Answer relevance and correctness | End to end | Does the answer address the question and match the reference? |
| Correct abstention rate | End to end | When the answer is not in the sources, does the system say so? |
| Citation accuracy | End to end | Do cited passages actually support the claims? |

Build a labelled set of 50 to 200 questions with the passages that answer them. Domain 5 covers how to grade them.

## Patterns and anti-patterns

| Pattern | Why it works |
| --- | --- |
| Look at parsed text before embedding | Catches the majority of quality problems early and cheaply. |
| Hybrid retrieval plus reranking as the default | Handles both meaning and exact identifiers. |
| ACL filtering inside the retriever | Permissions hold regardless of prompt behaviour. |
| Parent-child retrieval | Precise matching, complete context. |
| A retrieval eval separate from the answer eval | Tells you which layer to fix. |
| Show citations in the UI | Users can verify; trust and adoption rise. |

| Anti-pattern | What goes wrong |
| --- | --- |
| "Chunk everything into 500 tokens and hope" | Broken tables and sections; poor recall. |
| Indexing a full SharePoint export with no permission model | Data leakage; the security review ends the deal. |
| Filtering restricted content after generation | The model has already seen it; fragments leak. |
| Judging RAG only by reading a few answers | No idea whether changes help; regressions go unnoticed. |
| Fine-tuning to teach the model the knowledge base | Expensive, stale on the next update, no citations. |
| One index for all customers in a multi-tenant SaaS without tenant filters | Cross-tenant leakage. |

## Reading list

- [run-llama/llama_index](https://github.com/run-llama/llama_index): data framework for ingestion, indexing and retrieval.
- [langchain-ai/langchain](https://github.com/langchain-ai/langchain): loaders, splitters, retrievers and integrations.
- [docling-project/docling](https://github.com/docling-project/docling) and [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured): layout-aware document parsing.
- [pgvector/pgvector](https://github.com/pgvector/pgvector), [qdrant/qdrant](https://github.com/qdrant/qdrant), [chroma-core/chroma](https://github.com/chroma-core/chroma), [weaviate/weaviate](https://github.com/weaviate/weaviate), [lancedb/lancedb](https://github.com/lancedb/lancedb): vector stores.
- [huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers): open embedding and cross-encoder reranking models.
- [microsoft/graphrag](https://github.com/microsoft/graphrag): graph-based retrieval for multi-hop questions.
- [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas) and [docs](https://docs.ragas.io): RAG evaluation metrics.
- [Azure-Samples/azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo): an end-to-end enterprise RAG reference with document-level access control.
- [Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval) (Anthropic Engineering): chunk enrichment plus hybrid search and reranking.
- [Claude citations](https://platform.claude.com/docs/en/build-with-claude/citations) and [Claude embeddings guidance](https://platform.claude.com/docs/en/build-with-claude/embeddings).
- [OpenAI embeddings](https://platform.openai.com/docs/guides/embeddings) and [OpenAI file search](https://platform.openai.com/docs/guides/tools-file-search).
- [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard): compare embedding models, then test on your own data.
- [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html): managed RAG on AWS.

## Free credentials

| Credential | Provider | Why it fits this domain |
| --- | --- | --- |
| [Introduction to retrieval-augmented generation concepts](https://learn.microsoft.com/en-us/training/modules/rag-fundamentals/) | Microsoft Learn | RAG concepts and Azure patterns. |
| [Data Fundamentals for AI](https://trailhead.salesforce.com/content/learn/modules/data-fundamentals-for-ai) | Salesforce Trailhead | Data quality and preparation for AI. |
| [Skill badge: Inspect Rich Documents with Gemini Multimodality and Multimodal RAG](https://www.skills.google/course_templates/981) | Google Skills | Multimodal RAG over real documents. |
| [Vector Search and Embeddings](https://www.skills.google/course_templates/939) | Google Skills | Embeddings and vector search on Google Cloud. |
| [AWS Databases for Agentic AI Demonstrated (microcredential)](https://skillbuilder.aws/learn/2MHE4K7STM/aws-databases-for-agentic-ai-demonstrated/NYCNC3CU6X) | AWS Skill Builder | Vector stores and memory for agents, assessed in a live lab. |

## Hands-on lab: grounded policy assistant

**Goal:** build a permission-aware RAG assistant with citations and a retrieval eval, the core of many first POCs.

1. Collect 30 to 60 public documents of mixed formats on one theme (for example a government agency's HR policies, a product's public docs, or open standards), including at least five PDFs with tables and two scanned pages. Assign each document to one of three groups: `all-staff`, `managers`, `hr-only`.
2. Parse with two approaches (a naive text extractor and a layout-aware parser). Inspect five difficult pages side by side and write down what broke.
3. Chunk with structure-aware splitting plus parent-child retrieval. Store metadata: title, section, URI, modified date, group.
4. Index in pgvector or a local vector store, plus a BM25 index. Implement hybrid retrieval with reciprocal rank fusion and a reranker.
5. Enforce group filtering in both retrievers using a simulated user identity.
6. Generate answers with citations and a fixed "not in the sources" response.
7. Write 50 test questions with the IDs of the passages that answer them, including 10 unanswerable questions and five questions that a `all-staff` user must not be able to answer.
8. Measure recall at 5 and MRR for vector-only, keyword-only, hybrid, and hybrid plus rerank. Measure correct abstention and the permission tests.

**Deliverable:** a repository with the pipeline, the eval set, and `rag-report.md` containing the retrieval comparison table, three diagnosed failures (with the layer at fault), and the permission test results. Any permission leak is a failing grade until fixed.

## Review questions

1. A customer wants the assistant to answer "what is the current stock level of SKU 4471?" from a nightly RAG index. What do you recommend?

    <details><summary>Answer</summary>

    Stock levels change constantly and live in a system of record. Expose a read-only tool or API call that queries inventory at request time (Domain 4), and keep RAG for slow-changing documents such as product manuals. An index refreshed nightly will give stale answers.

    </details>

2. Users report wrong answers about error code "E-2291" even though the troubleshooting guide covers it. What is the most likely cause and fix?

    <details><summary>Answer</summary>

    Pure vector search often handles exact identifiers poorly. Add keyword (BM25) retrieval and merge with the vector results (hybrid retrieval), then rerank. Also check that parsing kept the error code intact and that the relevant section was not split away from its heading.

    </details>

3. Where must document permissions be enforced in a RAG system, and why not elsewhere?

    <details><summary>Answer</summary>

    At retrieval time, by filtering candidates on ACL or group metadata using the authenticated user's identity. Filtering after generation is too late because the model has already seen restricted content, and prompt instructions are not a security control.

    </details>

4. The right passage is retrieved, but the answer is still wrong. Name three things to check.

    <details><summary>Answer</summary>

    Whether the passage was truncated or split away from its context (table headers, section title); whether it was buried among many irrelevant or contradictory passages, including outdated versions; and whether the prompt instructs the model clearly to answer from sources and cite them. Also check whether the question needed several passages that were not all included.

    </details>

5. A prospect asks whether to fine-tune a model on their knowledge base instead of building RAG. How do you answer?

    <details><summary>Answer</summary>

    Fine-tuning changes behaviour and style; it is a poor way to store changing facts, cannot cite sources, must be repeated as content changes and does not respect per-user permissions. RAG keeps knowledge current, cites sources and enforces access control. Fine-tuning can be considered later for format or domain-language behaviour if evals show a gap.

    </details>

6. Which two retrieval metrics would you report in a POC readout, and what do they tell the customer?

    <details><summary>Answer</summary>

    Recall at k (how often a passage that answers the question is in the top k results) and mean reciprocal rank (how high the first relevant passage appears). Together they show whether the system finds the right evidence, separately from whether the model writes a good answer.

    </details>

7. Chunks such as "The limit is 30 days" retrieve poorly because they lack context. Name a technique that helps.

    <details><summary>Answer</summary>

    Contextual enrichment: prepend a short generated description of the chunk's place in the document (for example "From the 2026 Travel Policy, section 4.2, reimbursement deadlines") before embedding and keyword indexing. Parent-child retrieval and including section headings in chunks also help.

    </details>

8. How do you make sure deleted documents stop appearing in answers?

    <details><summary>Answer</summary>

    Use connectors with incremental sync that propagates deletes and permission changes, run periodic full reconciliation between source and index, and include a deletion test in the POC acceptance criteria. Stale deleted content in an index is a compliance risk as well as a quality issue.

    </details>
