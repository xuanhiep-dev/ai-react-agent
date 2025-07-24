# RAG-LLM Suite

This repository contains a collection of Retrieval-Augmented Generation (RAG) applications leveraging Large Language Models (LLMs). It includes:

- A **LangChain-based RAG pipeline** for context-aware question answering.
- A **Chainlit-based interface** to interact with the system in real time.
- A shared module with reusable components (retriever, utils, configs).

---

## Project Structure
```
rag-llm-suite/
│
├── chainlit_app/                      # RAG chatbot UI with Chainlit
│   ├── rag_chatbot_demo.ipynb         # Demo notebook for Chainlit chatbot
│   ├── rag_chatbot.ipynb              # Main notebook for chatbot logic
│
├── langchain_app/                     # RAG pipeline using LangChain
│   ├── data_source/
│   │   └── generative_ai/
│   │       └── download.py            # Script to download or prepare data
│   │
│   ├── src/
│   │   ├── base/
│   │   │   └── llm_model.py           # LLM interface setup (e.g., LLaMA)
│   │   │
│   │   └── rag/
│   │       ├── file_loader.py         # File parsing and document preparation
│   │       ├── main.py                # Entry point for RAG pipeline
│   │       ├── offline_rag.py         # RAG without external APIs
│   │       ├── utils.py               # Common utility functions
│   │       └── vectorstore.py         # Vector DB setup (e.g., Chroma)
│   │
│   ├── app.py                         # Optional app interface
│   ├── rag_langchain.ipynb            # Notebook interface for LangChain RAG
│
├── README.md                          # Project overview and usage
└── requirements.txt                   # Shared Python dependencies
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