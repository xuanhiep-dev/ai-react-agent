# RAG-LLM Suite

This repository includes a set of Retrieval-Augmented Generation (RAG) projects that make use of Large Language Models (LLMs). It includes:

- A **LangChain-based RAG pipeline** for context-aware question answering.
- A **Chainlit-based interface** to interact with the system in real time.
- A **legal-domain RAG module** for semantic search and question answering over Vietnamese legal documents.

---

## Project Structure
```
rag-llm-suite/
│
├── chainlit_app/           # Chatbot UI with Chainlit (notebooks)
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

## Features

- Modular design for integrating different RAG pipelines.
- Shared utilities and retriever logic across apps.
- Chainlit UI for fast prototyping and user interaction.
- Easily extensible for more frameworks or UIs.

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