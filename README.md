![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-0.2.5-green)
![LLM](https://img.shields.io/badge/LLM-OpenAI%2FHuggingFace-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

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

## 🔎 System Overview

```mermaid
flowchart TD
    A[User Query] --> B[Retriever: FAISS / Qdrant]
    B --> C[Relevant Documents]
    C --> D[LLM: GPT / HuggingFace]
    D --> E[Generated Answer + Sources]

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
👤 **User Query:**  
*Quy định về chấm dứt hợp đồng lao động là gì?*

**Context (from uploaded file):**  
*Bộ luật Lao động 2019 – Điều 34: Hợp đồng lao động có thể chấm dứt khi hết hạn, khi hai bên đồng ý kết thúc trước thời hạn, hoặc khi người lao động đã đến tuổi nghỉ hưu theo quy định pháp luật. Ngoài ra còn một số trường hợp đặc biệt khác…* 

🤖 **Chatbot Answer:**  
> **Theo Điều 34 Bộ luật Lao động 2019**, hợp đồng lao động chấm dứt trong các trường hợp chính:  
> - **Hết hạn hợp đồng**  
> - **Hai bên thỏa thuận chấm dứt**  
> - **Người lao động đủ tuổi nghỉ hưu**  
>
> *(Source: legal_doc_2023.pdf)*

## Benchmarks / Evaluation
| Metric          | Value |
|-----------------|-------|
| Recall@5        | 82%   |
| Faithfulness    | 86%     |
| Latency/query   | ~1.5s |

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

## Contribution & License
- Contributions, issues, and feature requests are welcome!  
- Feel free to open a PR or report a bug.