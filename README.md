# Awesome AI Engineering [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!--lint disable awesome-git-repo-age-->

> A curated list of courses, repositories, tools and certifications for **AI engineering**: building LLM applications, RAG, agents and MCP integrations, evaluating them, and taking them from demo to production. Focused on the **AI Solutions Engineer** and applied AI engineer roles.

AI Solutions Engineers (also called AI Sales Engineers, Applied AI Engineers or AI Solutions Consultants) sit between customers and product: they run discovery, design and demo AI solutions, ship proofs of concept and earn the trust of buyers and security teams. This list collects the best free material to learn the craft, plus a full **certification prep course** you can take at your own pace.

**Start here:**

- [AI Solution Engineer Certification Prep Course](course/README.md) - 8 domains, hands-on labs, review questions, 60-question mock exam and a capstone POC.
- [Free and paid certifications](certifications.md) - Free credentials, paid certificate programs and which AWS, Microsoft, Google Cloud, NVIDIA, Databricks and Anthropic exams to take, with exam facts.
- [Free AI Certifications Tracker](free-certifications/README.md) - 132 free credentials from FAANG, Big Tech and frontier AI labs, ordered as a study path for this role, with checkboxes to track your progress.

## Contents

- [Understand the Role](#understand-the-role)
- [Free Courses from Top AI Companies](#free-courses-from-top-ai-companies)
  - [Google, DeepMind and Kaggle](#google-deepmind-and-kaggle)
  - [Meta](#meta)
  - [Amazon and AWS](#amazon-and-aws)
  - [Apple](#apple)
  - [Netflix](#netflix)
  - [Microsoft](#microsoft)
  - [NVIDIA](#nvidia)
  - [OpenAI](#openai)
  - [Anthropic](#anthropic)
  - [IBM](#ibm)
  - [Oracle](#oracle)
  - [Intel](#intel)
- [Courses and Learning Paths](#courses-and-learning-paths)
  - [GitHub Curricula](#github-curricula)
- [Prompt and Context Engineering](#prompt-and-context-engineering)
- [Model APIs and SDKs](#model-apis-and-sdks)
- [Agent Frameworks](#agent-frameworks)
- [Agent Design Guides](#agent-design-guides)
- [Model Context Protocol](#model-context-protocol)
- [RAG and Document Processing](#rag-and-document-processing)
- [Vector Databases](#vector-databases)
- [Evaluation, Observability and Guardrails](#evaluation-observability-and-guardrails)
- [Demos and Prototyping](#demos-and-prototyping)
  - [Chat and App UIs](#chat-and-app-uis)
  - [Low-Code Builders](#low-code-builders)
  - [Voice, Browser and Sandboxes](#voice-browser-and-sandboxes)
  - [Local and Self-Hosted Models](#local-and-self-hosted-models)
- [Cookbooks and Reference Apps](#cookbooks-and-reference-apps)
  - [Model Providers](#model-providers)
  - [Cloud Platforms](#cloud-platforms)
- [Interview Preparation](#interview-preparation)
- [Books and Reading](#books-and-reading)
- [Related Awesome Lists](#related-awesome-lists)

## Understand the Role

What AI Solutions Engineers do, how they are hired and how pre-sales engineering works.

- [Awesome Sales Engineer](https://github.com/vladar107/awesome-sales-engineer) - Curated list of books, tools and guides for sales engineering and pre-sales roles.
- [PreSales Collective](https://www.presalescollective.com/) - Global community, training and job board for pre-sales and solutions professionals.
- [Mastering Technical Sales](https://bookshop.org/p/books/mastering-technical-sales-the-sales-engineer-s-handbook-fourth-edition-john-care/5ddb3f222447dda5) - John Care's handbook on discovery, demos, POCs and the sales engineer career $.
- [Great Demo!](https://www.greatdemo.com/) - Peter Cohan's method for crisp, outcome-first software demonstrations.
- [MEDDICC](https://www.meddicc.com/) - The qualification framework most enterprise AI sales teams use to qualify and close deals.

## Free Courses from Top AI Companies

Free courses, learning paths and official tutorials from FAANG, Big Tech and the frontier AI labs only. Items marked *Free badge* or *Free certificate* award a credential at no cost; the rest are free to learn. Paid programs are in [certifications](certifications.md#paid-certificate-programs).

### Google, DeepMind and Kaggle

- [Google Skills catalog](https://www.skills.google/catalog) - Google's renamed Cloud Skills Boost catalog of on-demand courses, labs, learning paths, and skill badges, with many AI items free to start. Free badge.
- [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) - Interactive self-paced introduction to core ML concepts such as regression, classification, embeddings, and LLM basics with visualizations and exercises.
- [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml) - Classic engineering guide of practical best practices for building and operating production ML systems.
- [Beginner: Introduction to Generative AI learning path](https://www.skills.google/paths/118) - Free microlearning path covering generative AI, LLMs, and responsible AI fundamentals on Google Skills. Free badge.
- [Advanced: Generative AI for Developers learning path](https://www.skills.google/paths/183) - Developer-oriented path on attention, transformers, encoder-decoder models, image generation, and building gen AI apps on Google Cloud. Free badge.
- [Introduction to Large Language Models](https://www.skills.google/course_templates/539) - Short course explaining what LLMs are, where they fit, and how prompt tuning improves their output. Free badge.
- [Transformer Models and BERT Model](https://www.skills.google/course_templates/538) - Technical course on the transformer architecture and the BERT model, including how to build a simple classifier. Free badge.
- [Machine Learning Operations (MLOps) for Generative AI](https://www.skills.google/course_templates/927) - Covers the operational challenges of deploying and managing generative models and the Vertex/Agent Platform tooling that addresses them. Free badge.
- [Vector Search and Embeddings](https://www.skills.google/course_templates/939) - Hands-on look at embeddings, semantic and hybrid search, and retrieval-augmented generation using Google's vector search service. Free badge.
- [Machine Learning Operations (MLOps): Getting Started](https://www.skills.google/course_templates/158) - Introduces MLOps tools and practices for deploying, evaluating, monitoring, and operating ML systems on Google Cloud. Free badge.
- [Build Your First Agent with Agent Development Kit (ADK)](https://www.skills.google/course_templates/1563) - Introductory hands-on course that sets up an ADK environment and builds agents in Python and YAML. Free badge.
- [Build intelligent agents with Agent Development Kit (ADK)](https://www.skills.google/course_templates/1382) - Longer intermediate course pairing ADK concepts with labs on tools, multi-agent patterns, and deployment (page returned 403 to automated checks due to rate limiting). Free badge.
- [Build Agent Skills with Google](https://www.skills.google/course_templates/1832) - Intermediate course on building reusable agent skills across ADK and Google's agent tooling. Free badge.
- [AI Research Foundations (Google DeepMind collection)](https://www.skills.google/collections/deepmind) - University-level DeepMind curriculum built with UCL on building, training, and aligning small language models in Keras/JAX. Free badge.
- [Google Cloud Machine Learning & AI training hub](https://cloud.google.com/learn/training/machinelearning-ai) - Landing page that maps Google Cloud AI and ML courses and paths by role and experience level.
- [Gemini API Cookbook](https://github.com/google-gemini/cookbook) - Official notebooks and guides demonstrating Gemini API features such as function calling, grounding, and multimodal input.
- [Generative AI on Google Cloud samples](https://github.com/GoogleCloudPlatform/generative-ai) - Large official repository of notebooks and sample apps for RAG, agents, evaluation, and Gemini on Google Cloud.
- [Agent Development Kit documentation](https://adk.dev/) - Official docs and tutorials for Google's open-source ADK framework, now hosted at adk.dev.
- [Kaggle Learn](https://www.kaggle.com/learn) - Catalog of short hands-on micro-courses in Python, ML, SQL, and deep learning run in browser notebooks. Free certificate.
- [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) - Practical first course on building and validating decision-tree and random-forest models. Free certificate.
- [Intro to Deep Learning](https://www.kaggle.com/learn/intro-to-deep-learning) - Builds and trains neural networks with Keras, covering optimization, overfitting, and dropout. Free certificate.
- [5-Day Gen AI Intensive Course with Google](https://www.kaggle.com/learn-guide/5-day-genai) - Self-paced version of Google's intensive on foundation models, prompting, embeddings, agents, and MLOps for gen AI with codelabs and whitepapers.
- [5-Day AI Agents Intensive Course with Google](https://www.kaggle.com/learn-guide/5-day-agents) - Self-paced intensive on agent architecture, tools, memory, evaluation, and production deployment with hands-on labs.

### Meta

- [PyTorch Tutorials](https://docs.pytorch.org/tutorials/) - Official tutorial collection spanning PyTorch basics through distributed training, compilation, and deployment.
- [Getting Started with Fully Sharded Data Parallel (FSDP2)](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html) - Hands-on tutorial on sharding large-model training across GPUs with PyTorch FSDP2.
- [Llama Cookbook](https://github.com/meta-llama/llama-cookbook) - Meta's official recipes for inference, fine-tuning, RAG, and end-to-end use cases with Llama models.
- [Meta AI developer hub (Llama docs)](https://dev.meta.ai/) - Meta's developer portal for Llama models and tools, which the former llama.com docs now redirect to.

### Amazon and AWS

- [AWS Skill Builder](https://skillbuilder.aws/) - AWS's learning platform with a large free tier of digital courses, learning plans, and free microcredential labs. Free badge.
- [AWS AI courses and training hub](https://aws.amazon.com/ai/learn/) - Entry point to AWS's AI and generative AI training by role, including free Skill Builder content.
- [Machine Learning University: Accelerated Tabular Data](https://github.com/aws-samples/aws-machine-learning-university-accelerated-tab) - Open MLU course materials with lecture notebooks on ML for tabular data used internally at Amazon.
- [Machine Learning University: Accelerated NLP](https://github.com/aws-samples/aws-machine-learning-university-accelerated-nlp) - Open MLU course on text processing, word vectors, RNNs, and transformers with notebooks.
- [MLU-Explain](https://mlu-explain.github.io/) - Interactive visual essays from Machine Learning University that explain core ML concepts.
- [Amazon Bedrock Workshop](https://github.com/aws-samples/amazon-bedrock-workshop) - Official hands-on workshop notebooks covering prompting, RAG, agents, and model customization with Amazon Bedrock.
- [Amazon Bedrock AgentCore samples](https://github.com/awslabs/agentcore-samples) - Official samples for taking agents to production with AgentCore runtime, gateway, memory, and identity (repo renamed from amazon-bedrock-agentcore-samples).

### Apple

- [Apple Developer: AI & Machine Learning](https://developer.apple.com/machine-learning/) - Apple's hub for on-device ML frameworks, tools, models, and WWDC sessions.
- [Foundation Models framework documentation](https://developer.apple.com/documentation/foundationmodels) - Docs for using Apple's on-device foundation model in apps, including guided generation and tool calling.
- [Core ML documentation](https://developer.apple.com/documentation/coreml) - Reference and guides for integrating and optimizing ML models in Apple-platform apps.
- [MLX documentation](https://ml-explore.github.io/mlx/build/html/index.html) - Docs for Apple's array framework for ML research and LLM work on Apple silicon.

### Netflix

- [Metaflow tutorials](https://docs.metaflow.org/getting-started/tutorials) - Official tutorials for Netflix's open-source framework for building and operating ML and AI workflows.

### Microsoft

- [Microsoft Learn training](https://learn.microsoft.com/en-us/training/) - Microsoft's free catalog of modules, learning paths, and career paths with sandbox labs. Free badge.
- [Microsoft Learn AI learning hub](https://learn.microsoft.com/en-us/ai/) - Curated AI learning journeys for building and deploying AI apps and agents on Microsoft platforms.
- [Training for AI engineers (career path)](https://learn.microsoft.com/en-us/training/career-paths/ai-engineer) - Role-based collection of Learn paths for designing and implementing AI solutions on Azure. Free badge.
- [Get started with AI applications and agents on Azure](https://learn.microsoft.com/en-us/training/paths/get-started-ai-apps-agents/) - Introductory Learn path on building AI apps and agents with Azure and Microsoft Foundry. Free badge.
- [Develop generative AI apps on Microsoft Foundry](https://learn.microsoft.com/en-us/training/paths/develop-generative-ai-apps/) - Learn path covering prompt flows, RAG, fine-tuning, and evaluation of gen AI apps in Microsoft Foundry. Free badge.
- [Develop AI Agents on Azure](https://learn.microsoft.com/en-us/training/paths/develop-ai-agents-azure/) - Learn path on building, extending, and orchestrating AI agents with Foundry Agent Service and SDKs. Free badge.
- [ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) - Twelve-week open curriculum of classic machine learning lessons with quizzes and scikit-learn projects.
- [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) - Twelve-week open curriculum covering neural networks, computer vision, NLP, and AI ethics.
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) - Twenty-one lesson course on building generative AI applications, from prompting to RAG and agents.
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) - Lesson series on agent design patterns, tool use, multi-agent systems, and production concerns.
- [MCP for Beginners](https://github.com/microsoft/mcp-for-beginners) - Open curriculum on Model Context Protocol fundamentals with multi-language server and client examples.

### NVIDIA

- [NVIDIA DLI self-paced training](https://www.nvidia.com/en-us/training/self-paced-courses/) - Catalog of NVIDIA Deep Learning Institute online courses, including a set of free introductory ones.
- [AI Learning Essentials](https://www.nvidia.com/en-us/learn/ai-learning-essentials/) - NVIDIA's curated starting point of free AI courses, tutorials, and resources by skill level.
- [NVIDIA Generative AI Examples](https://github.com/NVIDIA/GenerativeAIExamples) - Official reference implementations for RAG, agents, and NIM-based gen AI pipelines.

### OpenAI

- [OpenAI Academy](https://academy.openai.com/) - OpenAI's free learning hub with courses, livestreams, and community clubs on using and building with AI. Free certificate.
- [OpenAI Academy courses](https://academy.openai.com/pages/courses) - Course catalog including Build with AI (Codex and the OpenAI API) and pathway courses that award completion certificates. Free certificate.
- [OpenAI Cookbook](https://developers.openai.com/cookbook) - Official example code and guides for common OpenAI API tasks, now hosted on developers.openai.com.
- [OpenAI API documentation](https://developers.openai.com/api/docs) - Official guides for the OpenAI platform covering models, tools, agents, and evaluation.

### Anthropic

- [Claude Academy](https://academy.claude.com/) - Anthropic's renamed learning hub for working and building with Claude, hosting AI Fluency and capabilities courses. Free certificate.
- [Anthropic courses catalog (Skilljar)](https://anthropic.skilljar.com/) - Full catalog of free Anthropic courses on Claude, Claude Code, the API, MCP, and agents with completion certificates. Free certificate.
- [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) - Developer course on the Claude API covering prompting, tool use, RAG, and agent patterns. Free certificate.
- [Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol) - Hands-on course on building MCP servers and clients that expose tools, resources, and prompts. Free certificate.
- [Model Context Protocol: Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) - Follow-on course on advanced MCP features such as sampling, transports, and production concerns. Free certificate.
- [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) - Practical course on using Claude Code for agentic software development workflows. Free certificate.
- [Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills) - Short course on packaging reusable instructions and scripts as agent skills for Claude. Free certificate.
- [Claude Cookbooks](https://github.com/anthropics/claude-cookbooks) - Official notebooks and recipes for Claude features such as tool use, retrieval, and agents (renamed from anthropic-cookbook).
- [MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic) - Company-partnered short course on building MCP servers and clients for context-rich AI apps.

### IBM

- [watsonx.ai samples](https://github.com/IBM/watsonx-ai-samples) - Official notebooks and examples for building with IBM watsonx.ai models and services.

### Oracle

- [Become an OCI Generative AI Professional (learning path)](https://mylearn.oracle.com/ou/learning-path/become-an-oci-generative-ai-professional/147863) - Free Oracle path on LLMs, RAG, and the OCI Generative AI service that prepares for the paid professional exam.

### Intel

- [Intel AI developer training](https://www.intel.com/content/www/us/en/developer/topic-technology/artificial-intelligence/training/overview.html) - Intel's free AI training hub for optimizing and deploying models on Intel hardware (returns 403 to automated checks).

## Courses and Learning Paths

### GitHub Curricula

- [LLM Course](https://github.com/mlabonne/llm-course) - Roadmaps and Colab notebooks covering LLM fundamentals, the LLM scientist and the LLM engineer.
- [AI Engineering Hub](https://github.com/patchy631/ai-engineering-hub) - In-depth tutorials and projects on LLMs, RAG and real-world agents.
- [GenAI Agents](https://github.com/NirDiamant/GenAI_Agents) - 50+ tutorials implementing agent techniques from simple bots to multi-agent systems.
- [Agents Towards Production](https://github.com/NirDiamant/agents-towards-production) - Code-first tutorials for taking agents from prototype to production.
- [LLMs from Scratch](https://github.com/rasbt/LLMs-from-scratch) - Code for building a GPT-style LLM from scratch to deeply understand internals.
- [Generative-AI-for-beginners-dotnet](https://github.com/microsoft/Generative-AI-for-beginners-dotnet) - Short course on applying GenAI in .NET applications.

## Prompt and Context Engineering

- [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) - Comprehensive guide to prompting, context engineering, RAG and agent techniques.
- [Anthropic Prompt Engineering Interactive Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) - Anthropic's hands-on, notebook-based prompt engineering course.
- [Anthropic Courses](https://github.com/anthropics/courses) - Anthropic's original courses on the API, prompting, evaluations and tool use (archived but still useful).
- [Prompt Engineering Techniques](https://github.com/NirDiamant/Prompt_Engineering) - Notebook tutorials for 22 prompting techniques from basic to advanced.
- [Brex Prompt Engineering Guide](https://github.com/brexhq/prompt-engineering) - Concise, practitioner-written prompt engineering guide from Brex.
- [PromptWizard](https://github.com/microsoft/PromptWizard) - Microsoft framework for automatic, task-aware prompt optimization.
- [Claude prompt engineering overview](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) - Official Claude guide to clear instructions, examples, XML structure and chaining.
- [OpenAI prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering) - Official OpenAI strategies for getting better results from models.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) - Anthropic on curating the right context for long-running agents.

## Model APIs and SDKs

- [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python) - Official Anthropic Python client for the Claude API.
- [Anthropic TypeScript SDK](https://github.com/anthropics/anthropic-sdk-typescript) - Official Anthropic TypeScript client for the Claude API.
- [OpenAI Python SDK](https://github.com/openai/openai-python) - Official OpenAI Python client library.
- [LiteLLM](https://github.com/BerriAI/litellm) - Gateway and SDK that calls 100+ model APIs through one OpenAI-compatible interface with cost tracking.
- [Instructor](https://github.com/567-labs/instructor) - Structured, validated JSON outputs from LLMs using Pydantic models.
- [Outlines](https://github.com/dottxt-ai/outlines) - Constrained generation library that guarantees outputs match a schema or grammar.
- [OpenAI developer docs](https://developers.openai.com/) - Official hub for OpenAI APIs, Responses, Agents SDK and Apps SDK.
- [Gemini API cookbook](https://ai.google.dev/gemini-api/cookbook) - Official Gemini API examples and guides.

## Agent Frameworks

- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - OpenAI's official Agents SDK for tool-using, handoff-based multi-agent workflows in Python.
- [OpenAI Agents SDK for TypeScript](https://github.com/openai/openai-agents-js) - TypeScript version of the OpenAI Agents SDK, including voice agents.
- [Claude Agent SDK for Python](https://github.com/anthropics/claude-agent-sdk-python) - Python SDK exposing the Claude Code agent harness for building custom agents.
- [Claude Agent SDK for TypeScript](https://github.com/anthropics/claude-agent-sdk-typescript) - TypeScript SDK for building agents on the Claude Code harness.
- [Agent Skills](https://github.com/anthropics/skills) - Anthropic's public collection of Agent Skills and the reference format for authoring them.
- [LangGraph](https://github.com/langchain-ai/langgraph) - Graph-based runtime for stateful, durable, human-in-the-loop agents.
- [Deep Agents](https://github.com/langchain-ai/deepagents) - Batteries-included agent harness with planning, sub-agents and a virtual filesystem, built on LangGraph.
- [LangChain](https://github.com/langchain-ai/langchain) - Python framework for composing models, tools, retrievers and agents.
- [LangChain.js](https://github.com/langchain-ai/langchainjs) - JavaScript/TypeScript edition of LangChain for Node and web demos.
- [LlamaIndex](https://github.com/run-llama/llama_index) - Data framework focused on document parsing, indexing and retrieval for RAG and agents.
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - Type-safe Python agent framework from the Pydantic team with structured outputs and evals.
- [Agent Development Kit (ADK)](https://github.com/google/adk-python) - Google's Agent Development Kit for building, evaluating and deploying agents in Python.
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) - Microsoft's unified successor to AutoGen and Semantic Kernel agents for Python and .NET.
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - Enterprise SDK for C#, Python and Java that plugs LLMs into existing applications.
- [CrewAI](https://github.com/crewAIInc/crewAI) - Role-based multi-agent orchestration framework popular for quick business-process demos.
- [smolagents](https://github.com/huggingface/smolagents) - Minimal library for agents that reason by writing and executing code.
- [Mastra](https://github.com/mastra-ai/mastra) - TypeScript agent framework with workflows, memory, RAG and built-in evals.
- [Vercel AI SDK](https://github.com/vercel/ai) - Standard TypeScript toolkit for streaming chat, tool calling and generative UI.
- [Haystack](https://github.com/deepset-ai/haystack) - Production-oriented pipeline framework for search, RAG and agent applications.
- [DSPy](https://github.com/stanfordnlp/dspy) - Declarative framework that compiles and optimizes prompts and LM pipelines programmatically.
- [Agno](https://github.com/agno-agi/agno) - Lightweight Python agent framework and runtime with memory, knowledge and multi-agent teams.
- [Mem0](https://github.com/mem0ai/mem0) - Drop-in long-term memory layer for agents and chat assistants.

## Agent Design Guides

- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) - Anthropic's guide to workflows versus agents and simple composable patterns.
- [A practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) - OpenAI guide to agent design, orchestration and guardrails.
- [12-Factor Agents](https://github.com/humanlayer/12-factor-agents) - Principles for building LLM-powered software reliable enough for production customers.

## Model Context Protocol

- [Model Context Protocol docs](https://modelcontextprotocol.io/) - Official documentation, concepts and quickstarts for MCP.
- [MCP specification](https://github.com/modelcontextprotocol/modelcontextprotocol) - The Model Context Protocol specification and official documentation.
- [MCP reference servers](https://github.com/modelcontextprotocol/servers) - Reference MCP server implementations maintained by the MCP project.
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Official Python SDK for building MCP servers and clients.
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Official TypeScript SDK for building MCP servers and clients.
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector) - Interactive tool for testing and debugging MCP servers.
- [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) - Spec and SDK for MCP Apps, interactive UIs that MCP servers render inside chat clients.
- [FastMCP](https://github.com/PrefectHQ/fastmcp) - Pythonic high-level framework for building MCP servers and clients fast.
- [mcp-agent](https://github.com/lastmile-ai/mcp-agent) - Framework for composing agents from MCP servers using simple workflow patterns.
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - Largest community directory of MCP servers.
- [Agent2Agent (A2A) Protocol](https://github.com/a2aproject/A2A) - Agent2Agent open protocol for interoperability between independent agents.
- [AG-UI](https://github.com/ag-ui-protocol/ag-ui) - Agent-User Interaction protocol for connecting agent backends to frontends.

## RAG and Document Processing

- [RAG Techniques](https://github.com/NirDiamant/RAG_Techniques) - Notebook catalog of advanced RAG techniques with explanations and code.
- [RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) - Video-paired notebooks that build RAG concepts up from first principles.
- [RAGFlow](https://github.com/infiniflow/ragflow) - Open-source RAG engine with deep document understanding and agent features.
- [Docling](https://github.com/docling-project/docling) - Converts PDFs and office documents into clean structured data for GenAI pipelines.
- [MarkItDown](https://github.com/microsoft/markitdown) - Lightweight tool that converts office files and PDFs to Markdown for LLM ingestion.
- [Unstructured](https://github.com/Unstructured-IO/unstructured) - Open-source ETL for turning messy documents into LLM-ready chunks.
- [Firecrawl](https://github.com/firecrawl/firecrawl) - Turns websites into clean LLM-ready Markdown or structured data.
- [GraphRAG](https://github.com/microsoft/graphrag) - Microsoft's knowledge-graph-based RAG system for global, multi-hop questions.
- [LightRAG](https://github.com/HKUDS/LightRAG) - Fast, simple graph-enhanced RAG framework.
- [Neo4j GraphRAG for Python](https://github.com/neo4j/neo4j-graphrag-python) - Official Neo4j library for building GraphRAG applications in Python.
- [RAG on PostgreSQL](https://github.com/Azure-Samples/rag-postgres-openai-python) - RAG over PostgreSQL rows deployable on Azure, a good structured-data demo.

## Vector Databases

- [pgvector](https://github.com/pgvector/pgvector) - Vector similarity search extension for Postgres.
- [Qdrant](https://github.com/qdrant/qdrant) - High-performance Rust vector database with filtering and hybrid search.
- [Chroma](https://github.com/chroma-core/chroma) - Developer-friendly open-source embedding database, the default for many prototypes.
- [Weaviate](https://github.com/weaviate/weaviate) - Open-source vector database combining vector and keyword search.
- [Milvus](https://github.com/milvus-io/milvus) - Cloud-native vector database built for billion-scale search.
- [LanceDB](https://github.com/lancedb/lancedb) - Embedded, serverless-friendly multimodal retrieval library.
- [Faiss](https://github.com/facebookresearch/faiss) - Meta's foundational library for efficient similarity search and clustering.
- [Pinecone examples](https://github.com/pinecone-io/examples) - Pinecone notebooks and sample apps for vector search and RAG.
- [Elastic Search Labs](https://github.com/elastic/elastic-labs) - Elastic notebooks and example apps for semantic search and RAG on Elasticsearch.

## Evaluation, Observability and Guardrails

- [Your AI product needs evals](https://hamel.dev/blog/posts/evals/) - Hamel Husain's practical guide to building evaluation systems.
- [What we learned from a year of building with LLMs](https://applied-llms.org/) - Practitioner lessons on evals, RAG and operating LLM products.
- [promptfoo](https://github.com/promptfoo/promptfoo) - CLI and CI tool for testing prompts, RAG and agents plus LLM red teaming.
- [DeepEval](https://github.com/confident-ai/deepeval) - Pytest-style framework with many ready-made LLM evaluation metrics.
- [Ragas](https://github.com/vibrantlabsai/ragas) - Metrics and test-data generation for evaluating RAG pipelines (formerly explodinggradients/ragas).
- [Langfuse](https://github.com/langfuse/langfuse) - Open-source LLM tracing, prompt management, evals and analytics platform.
- [Phoenix](https://github.com/Arize-ai/phoenix) - Open-source AI observability and evaluation tool built on OpenTelemetry.
- [Opik](https://github.com/comet-ml/opik) - Open-source platform for tracing, evaluating and monitoring LLM apps and agents.
- [MLflow](https://github.com/mlflow/mlflow) - Open-source platform for tracking, evaluating and tracing ML and GenAI apps.
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - OpenTelemetry-based instrumentation for LLM applications.
- [Helicone](https://github.com/Helicone/helicone) - Open-source LLM observability proxy with one-line integration.
- [TruLens](https://github.com/truera/trulens) - Evaluation and tracking for LLM experiments and agents, known for the RAG triad.
- [OpenAI Evals](https://github.com/openai/evals) - OpenAI's framework and registry for evaluating LLMs and LLM systems.
- [Inspect](https://github.com/UKGovernmentBEIS/inspect_ai) - UK AI Security Institute framework for rigorous LLM and agent evaluations.
- [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) - Standard harness for benchmarking language models on academic tasks.
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - Input and output validation framework for adding guardrails to LLM apps.
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) - NVIDIA toolkit for programmable conversational guardrails.
- [Presidio](https://github.com/data-privacy-stack/presidio) - PII detection and anonymization framework, often required in enterprise POCs.

## Demos and Prototyping

### Chat and App UIs

- [Streamlit](https://github.com/streamlit/streamlit) - Fastest way to turn Python scripts into shareable data and chat apps.
- [Gradio](https://github.com/gradio-app/gradio) - Python library for quick ML and chat demos, native to Hugging Face Spaces.
- [Vercel Chatbot](https://github.com/vercel/chatbot) - Vercel's full-featured, hackable Next.js AI chatbot template.
- [assistant-ui](https://github.com/assistant-ui/assistant-ui) - React component library for production-grade AI chat interfaces.
- [CopilotKit](https://github.com/CopilotKit/CopilotKit) - React framework for in-app copilots and generative UI, creators of AG-UI.
- [ChatKit](https://github.com/openai/chatkit-js) - OpenAI's embeddable chat UI toolkit for agent experiences.
- [Open WebUI](https://github.com/open-webui/open-webui) - Self-hosted ChatGPT-style interface for Ollama and OpenAI-compatible APIs.

### Low-Code Builders

- [n8n](https://github.com/n8n-io/n8n) - Workflow automation platform with native AI agent nodes, widely used for integration demos.
- [Dify](https://github.com/langgenius/dify) - Open-source platform for building agentic workflows and RAG apps visually.
- [Langflow](https://github.com/langflow-ai/langflow) - Visual builder for agents and flows with Python extensibility.
- [Prompt flow](https://github.com/microsoft/promptflow) - Tooling to prototype, evaluate and deploy LLM flows, integrated with Azure AI.

### Voice, Browser and Sandboxes

- [Pipecat](https://github.com/pipecat-ai/pipecat) - Open-source framework for real-time voice and multimodal agents.
- [LiveKit Agents](https://github.com/livekit/agents) - Framework for building real-time voice and video AI agents.
- [Browser Use](https://github.com/browser-use/browser-use) - Python library that lets AI agents operate a web browser.
- [E2B](https://github.com/e2b-dev/E2B) - Secure cloud sandboxes for running agent-generated code.

### Local and Self-Hosted Models

- [Ollama](https://github.com/ollama/ollama) - Run open models locally, ideal for offline or on-prem customer demos.
- [vLLM](https://github.com/vllm-project/vllm) - High-throughput inference and serving engine for LLMs.
- [SGLang](https://github.com/sgl-project/sglang) - Fast serving framework for large language and multimodal models.

## Cookbooks and Reference Apps

### Model Providers

- [Claude Quickstarts](https://github.com/anthropics/claude-quickstarts) - Deployable Claude starter apps such as customer support agents and computer use.
- [Claude Agent SDK demos](https://github.com/anthropics/claude-agent-sdk-demos) - Example agents built with the Claude Agent SDK, handy as demo starting points.
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook) - Official OpenAI notebooks and guides covering common API patterns.
- [OpenAI Customer Service Agents Demo](https://github.com/openai/openai-cs-agents-demo) - Customer-service multi-agent demo built with the OpenAI Agents SDK.
- [OpenAI Realtime Agents](https://github.com/openai/openai-realtime-agents) - Demonstration of agentic voice patterns on the OpenAI Realtime API.
- [OpenAI Apps SDK Examples](https://github.com/openai/openai-apps-sdk-examples) - Example ChatGPT apps built with the OpenAI Apps SDK.
- [Gemini Fullstack LangGraph Quickstart](https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart) - Full-stack research agent template combining Gemini, LangGraph and a React frontend.
- [Mistral Cookbook](https://github.com/mistralai/cookbook) - Official Mistral examples and third-party integration notebooks.
- [Hugging Face Cookbook](https://github.com/huggingface/cookbook) - Community notebooks showing practical open-model AI recipes.

### Cloud Platforms

- [Amazon Bedrock Samples](https://github.com/aws-samples/amazon-bedrock-samples) - Amazon Bedrock examples spanning agents, knowledge bases, guardrails and model customization.
- [Generative AI Use Cases on AWS](https://github.com/aws-samples/generative-ai-use-cases) - Deployable AWS reference app bundling many business generative AI use cases, useful for customer demos.
- [Azure Search OpenAI Demo](https://github.com/Azure-Samples/azure-search-openai-demo) - Reference RAG chat app on Azure AI Search and Azure OpenAI, a classic enterprise demo.
- [Azure OpenAI Samples](https://github.com/Azure-Samples/openai) - Samples for Azure OpenAI that complement the OpenAI Cookbook.
- [Get Started with AI Agents on Azure](https://github.com/Azure-Samples/get-started-with-ai-agents) - Starter template for deploying an agent web app on Azure AI Foundry.
- [ADK Recipes](https://github.com/google/adk-recipes) - Agent recipes, reference patterns and vertical examples built with Google ADK.
- [MongoDB GenAI Showcase](https://github.com/mongodb-developer/GenAI-Showcase) - MongoDB examples of RAG, agents and vector search across many frameworks.
- [LangChain Next.js Template](https://github.com/langchain-ai/langchain-nextjs-template) - Starter template pairing LangChain with Next.js for quick web demos.

## Interview Preparation

- [Machine Learning Interviews Book](https://github.com/chiphuyen/ml-interviews-book) - Chip Huyen's book on the ML interview process and practice questions.
- [LLM Interview Questions](https://github.com/llmgenai/LLMInterviewQuestions) - Questions reportedly asked in LLM interviews at AI companies, grouped by topic.
- [LLM Interview Questions and Answers Hub](https://github.com/KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub) - 100+ LLM interview questions with answers.
- [LLMs Interview Questions](https://github.com/Devinterview-io/llms-interview-questions) - LLM interview questions with detailed answers.
- [Data Science Interviews](https://github.com/alexeygrigorev/data-science-interviews) - Theory and technical data science interview questions and answers.
- [Data Science Interview Questions and Answers](https://github.com/youssefHosni/Data-Science-Interview-Questions-Answers) - Curated data science and ML interview questions and answers.

## Books and Reading

- [AI Engineering](https://huyenchip.com/books/) - Chip Huyen's book on building applications with foundation models $.
- [AI Engineering book resources](https://github.com/chiphuyen/aie-book) - Resources and supporting material for Chip Huyen's book AI Engineering.
- [Patterns for building LLM-based systems](https://eugeneyan.com/writing/llm-patterns/) - Eugene Yan's catalog of evals, RAG, caching and guardrail patterns.
- [Latent Space AI engineer reading list](https://www.latent.space/p/2025-papers) - Curated papers and posts every AI engineer should know.
- [AI Engineer conference talks](https://www.ai.engineer/) - Talks from practitioners shipping AI products.
- [AI Notes](https://github.com/swyxio/ai-notes) - Swyx's notes for software engineers getting up to speed on AI, backing Latent Space writing.
- [AI Engineering Resources](https://github.com/InterviewReady/ai-engineering-resources) - Papers and blogs for engineers transitioning into AI engineering.
- [Applied ML](https://github.com/eugeneyan/applied-ml) - Papers and tech blogs on ML in production from real companies.

## Related Awesome Lists

- [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - Large collection of runnable LLM, RAG and agent apps, useful for demo ideas.
- [Awesome Generative AI Guide](https://github.com/aishwaryanr/awesome-generative-ai-guide) - One-stop GenAI repo with research updates, courses and interview resources.
- [Awesome LLM](https://github.com/Hannibal046/Awesome-LLM) - Curated list of LLM papers, frameworks and resources.
- [Awesome AI Agents](https://github.com/e2b-dev/awesome-ai-agents) - Curated list of autonomous AI agents and agent frameworks.
- [Awesome AI Architect](https://github.com/EldanGS/awesome-ai-architect) - Sister list for AI architecture, platforms, governance and the free certifications tracker.
- [Awesome Forward Deployment Engineer](https://github.com/EldanGS/awesome-forward-deployment-engineer) - Sister list for engineers embedded with customers to ship production AI.

## Contributing

Contributions are welcome. Read the [contribution guidelines](contributing.md) first, and follow the [Code of Conduct](code-of-conduct.md).

Found a dead link, an archived repository or a retired exam? [Open an issue](https://github.com/EldanGS/awesome-ai-engineering/issues/new/choose).
