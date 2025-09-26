![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green?logo=fastapi)
![Qdrant](https://img.shields.io/badge/VectorDB-Qdrant-orange?logo=qdrant)
![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

# Installation Guide and Usage Instructions
A simple RESTful API for semantic search of Vietnamese legal documents using FastAPI, Sentence-BERT, and Qdrant.

## Features
- Search Vietnamese legal articles with semantic understanding.
- Uses PhoBERT embeddings (via Sentence-BERT).
- Vector storage & search powered by Qdrant.
- Endpoint /search returns relevant articles (title and content).

## Tech Stack
- FastAPI — Python web API framework
- Sentence-BERT — Vietnamese PhoBERT model for embeddings
- Qdrant — Vector database for similarity search
- Docker — Containerized deployment

## Smart Legal Search Highlights
- Uses state-of-the-art Vietnamese Sentence Embedding models (e.g. PhoBERT, SimCSE) to understand user queries semantically — not just by keywords.
- Implements fast vector similarity search with FAISS or Qdrant for efficient Top-K retrieval.
- Automatically removes duplicate articles and ranks the most relevant results.
- Supports hybrid search: combines semantic similarity and keyword scores for better matching.
- Can be expanded with synonym dictionaries and metadata filters (e.g., filter by specific law types).
- Evaluates search accuracy with simple metrics like Top-K Accuracy to ensure real-world reliability.

## Usage.
### 4.1. Load streamlit tool.
The project is developed using the FastAPI tool. To execute the project:
```bash
docker pull xuanhiepp/legal-search-api:latest
docker run -p 8000:8000 xuanhiepp/legal-search-api:latest
```

Wait about 2-3 minutes until the terminal displays as shown below. 
```bash
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

Since the port is mapped as 8000:8000 in docker-compose.yml, you can open your browser and access the the Swagger API screen at:
http://localhost:8000/docs or http://127.0.0.1:8000/docs

## Deployment Options
- **Local run** with Docker (default)
- **Cloud**: Deploy to AWS ECS / GCP Cloud Run / Azure App Service
- **Serverless**: FastAPI + Qdrant Cloud + Hugging Face Spaces


## Evaluation

| Metric       | Value |
|--------------|-------|
| Top-5 Recall | 84%   |
| MRR@5        | 0.79  |
| Avg Latency  | ~120ms |

## Example Query.
```markdown
## API Endpoints

### `POST /search`
- **Description:** Semantic search for legal documents.  
- **Request body:**
```json
{
  "query": "NLĐ bị sa thải có được trả lương hay không?",
  "top_k": 5
}
{
  "results": [
    {
      "title": "Điều 42. Trách nhiệm của NSDLĐ khi đơn phương chấm dứt HĐLĐ",
      "content": "Trường hợp NSDLĐ đơn phương chấm dứt HĐLĐ trái pháp luật..."
    }
  ]
}
<img src="example.png" alt="Example"/>
```

## Contributing
Contributions, issues, and feature requests are welcome.  
Feel free to open an [issue](../../issues) or submit a PR.  

## License
License © 2025 [Duong Xuan Hiep]
