# AI Agent with ReAct Pattern

This repository contains a collection of **AI Agents** that combine **Large Language Models (LLMs)** with external tools following the **ReAct (Reasoning + Acting)** pattern.

The goal is to build **transparent, modular, and tool-augmented AI pipelines** for real-world tasks such as reasoning, reflection, summarization, and vision.

## Key Features
- ReAct Pattern: Agents reason step by step, decide when to use tools, and integrate tool outputs with LLM reasoning.
- Multi-Tool Support: Works with vector stores (FAISS, Qdrant), vision models (YOLO, SAM), and summarization pipelines.
- Traceability: Keeps reasoning trace for better debugging and explainability.
- Extensibility: Compatible with LangChain, Hugging Face, or custom pipelines.
---

## Repository Structure

- **ai_react_agent_graph.ipynb** -- Demonstrates how to build a **graph-based ReAct Agent** that integrates reasoning steps and tool calls dynamically.
- **news_filter_summarizer_agent.ipynb** -- A pipeline for **filtering and summarizing news articles** with an LLM + retrieval module.
- **object_detection_tools.ipynb** -- Shows how to connect **vision models (YOLO, SAM)** as callable tools for an agent.
- **reflection_agent_faiss.ipynb** -- A reflection-based agent that retrieves knowledge using **FAISS vector database**.
- **reflection_agent_qdrant.ipynb** -- Similar to the FAISS version but uses **Qdrant vector database** for semantic retrieval.
- **images/** -- Folder to store sample images, detection results, and visualization outputs.

---

## **How It Works**

1. **User Query:** The agent receives a question or task.
2. **Reasoning:** The LLM generates intermediate thoughts.
3. **Tool Calls:** The agent invokes external tools when needed (e.g., vector DB, detection model).
4. **CombIntegration:** Tool outputs are merged with LLM knowledge.
5. **Answer:** A grounded, transparent answer with reasoning trace is returned.

## Getting Started
```
pip install -r requirements.txt
```
Then open any notebook in Kaggle or Jupyter Lab:
```
jupyter notebook object_detection_tools.ipynb
```

## **Future Work**

- Add support for multi-agent collaboration.
- Integrate RAG pipelines with domain-specific datasets.
- Enhance visualization of reasoning traces.
