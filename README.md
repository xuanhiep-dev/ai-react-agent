# RAG-LLM Suite

A collection of **Retrieval-Augmented Generation (RAG)** projects built on top of **Large Language Models (LLMs)**.  
The suite demonstrates how to combine **semantic search** with **generative models** to provide accurate, context-grounded answers.

---

## Key Features
- **Modular design**: LangChain-based RAG pipeline, Chainlit chatbot UI, and Legal-domain RAG module.
- **Semantic retrieval**: FAISS / Qdrant vector search integrated with LLMs.
- **Legal-domain support**: Specialized module for Vietnamese legal documents.
- **Interactive UI**: Real-time chatbot interface with Chainlit.
- **Extensible**: Easy to add new data sources, retrievers, or frontends.

---

## Project Structure
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
User: Quy định về chấm dứt hợp đồng lao động là gì?
System: Theo Điều 34 Bộ luật Lao động 2019, hợp đồng lao động chấm dứt trong các trường hợp: ...
(Source: legal_doc_2023.pdf)
```

## Tech Stack
- LangChain – RAG pipeline, retrievers, chains
- LLMs – OpenAI GPT / HuggingFace models
- Vector DBs – FAISS, Qdrant
- UI – Chainlit
- Python – Core implementation

## Use Cases
- Legal document Q&A (Vietnamese law)
- Knowledge base assistants
- Enterprise search + chatbots
- Educational tools for document exploration

## Future Work
- Add evaluation metrics (e.g., Faithfulness, Recall@k)
- Dockerize apps for easy deployment
- Support multi-lingual datasets
