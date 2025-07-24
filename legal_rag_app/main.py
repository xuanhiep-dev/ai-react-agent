from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
import os
import yaml
os.environ["TRANSFORMERS_NO_TF"] = "1"


# 1. FastAPI Initialization
app = FastAPI(
    title="Legal Dense Search API",
    description="RESTful API: Semantic search Điều luật dùng PhoBERT + Qdrant",
    version="1.0"
)


# 2. Load model PhoBERT
model = SentenceTransformer(
    "VoVanPhuc/sup-SimCSE-VietNamese-phobert-base",
    device='cpu'
)


# 3. Connect Qdrant Cloud
def load_env(config_file):
    if config_file.endswith(".yaml") or config_file.endswith(".yml"):
        # Load YAML
        with open(config_file, "r") as f:
            config = yaml.safe_load(f)
            for key, value in config.items():
                os.environ[str(key)] = str(value)
    else:
        # Load .env
        with open(config_file) as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    os.environ[key.strip()] = value.strip()


load_env('config.yaml')
qdrant_url = os.getenv("QDRANT_URL")
qdrant_key = os.getenv("QDRANT_API_KEY")
qdrant_client = QdrantClient(
    url=qdrant_url,
    api_key=qdrant_key,
)


# 4. Request schema
class SearchRequest(BaseModel):
    query: str


class SearchResult(BaseModel):
    title: str
    content: str


# 5. Endpoint /search
@app.post("/search", response_model=List[SearchResult])
def search(req: SearchRequest):
    user_query = req.query

    # Encode query
    query_vec = model.encode(user_query, normalize_embeddings=True)

    # Dense search
    hits = qdrant_client.query_points(
        collection_name="laws_collection",
        query=query_vec.tolist(),
        limit=20,
        with_payload=True
    ).points

    seen_titles = set()
    results = []

    for hit in hits:
        payload = hit.payload
        title = payload.get("title", "").strip()
        content = payload.get("text", "").strip()

        # If saw the title, skip it.
        if title in seen_titles:
            continue

        seen_titles.add(title)

        results.append(SearchResult(
            title=title,
            content=content
        ))

    # Get top 5 hits
    results = results[:5]

    return results
