# RAG-LLM Suite

> A cutting-edge **Retrieval-Augmented Generation (RAG)** suite powered by **Large Language Models (LLMs)**, designed for building intelligent, domain-specific assistants.  
> From **legal document Q&A** to **interactive chatbots**, this project showcases how modern AI can bridge **retrieval** and **reasoning**.

---

## Key Features
- **Modular RAG pipelines**: Plug-and-play with LangChain agents, retrievers, and prompts.  
- **Semantic search at scale**: Integrates FAISS and Qdrant vector stores.  
- **Domain-specific AI**: Specialized legal RAG module for Vietnamese law.  
- **Interactive experience**: Real-time chatbot powered by Chainlit.  
- **Production-ready mindset**: Clean structure, extensible modules, and future deployment plan.  

---

## Project Architecture
```
rag-llm-suite/
│
├── chainlit_app/           # Chatbot UI with Chainlit (notebooks)
│   └── rag_chatbot.ipynb # Notebook demo
│
├── langchain_app/          # LangChain-based RAG pipeline
│   ├── data_source/        # Raw data loader
│   ├── src/                # LLM and RAG modules
│   ├── app.py              # Optional web interface
│   └── rag_langchain.ipynb # Notebook for testing
│
├── legal_rag_app/          # Legal document search with RAG
│   ├── results/            # Output files
│   ├── main.py             # Pipeline entry point
│   └── legal-document-search.ipynb  # Notebook demo
│
├── requirements.txt        # Shared dependencies
└── README.md               # Project overview
```
---

## Quick Start

### 1. Install Dependencies
```
pip install -r requirements.txt
```

### 2. Run LangChain App
```
cd langchain_app
jupyter notebook rag_langchain.ipynb
```

### 3. Run Chainlit UI
```
cd chainlit_app
jupyter notebook rag_chatbot.ipynb
```

### 4. Run Legal App
```
cd chainlit_app
jupyter notebook legal_document_search.ipynb
```

## Example Output
```
👤 User: Quy định về chấm dứt hợp đồng lao động là gì?

🤖 AI Agent:
Theo Điều 34 Bộ luật Lao động 2019, hợp đồng lao động chấm dứt trong các trường hợp:
- Hết hạn hợp đồng
- Hai bên thỏa thuận chấm dứt
- Người lao động đủ tuổi nghỉ hưu
(Source: legal_doc_2023.pdf)
```

## Tech Stack
- **LangChain** – Chains, agents, retrievers
- **LLMs** – OpenAI GPT / HuggingFace models
- **Vector DBs** – FAISS, Qdrant
- **Frontend** – Chainlit UI for interactive chat
- **Backend** – Python (FastAPI-ready)

## Real-World Use Cases
- **Legal AI Assistant:** Search and explain Vietnamese legal codes.
- **Enterprise Knowledge Base:** Internal document Q&A with source grounding.
- **Educational Chatbot:** Support learning from textbooks, research papers.
- **Research Assistant:** Semantic search across large corpora of documents.

## Roadmap
- Add evaluation metrics (Faithfulness, Recall@k, BLEU/ROUGE)
- Dockerize for easy deployment
- Multi-lingual RAG pipelines (EN–VI)
- Plug-and-play API with FastAPI

## Future Work
- Add evaluation metrics (e.g., Faithfulness, Recall@k)
- Dockerize apps for easy deployment
- Support multi-lingual datasets

## Why this project?
This suite is not just a demo. It is a foundation for building production-level intelligent assistants, with modularity and scalability in mind.
It demonstrates:
- Understanding of LLM + RAG architecture
- Ability to design practical AI systems
- Skills in both research and engineering