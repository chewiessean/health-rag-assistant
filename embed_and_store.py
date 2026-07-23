import json
from sentence_transformers import SentenceTransformer
import chromadb

with open("data/health_data.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [chunk["text"] for chunk in chunks]

embeddings = model.encode(texts)
print(f"Generated {len(embeddings)} embeddings, each with {embeddings.shape[1]} dimensions.")

client = chromadb.PersistentClient(path="./chromadb")
collection = client.get_or_create_collection(name="health_articles")

ids = [chunk["chunk_id"] for chunk in chunks]
documents = texts
metadatas = [{"source": chunk["source"], "url": chunk["url"]} for chunk in chunks]
embeddings_list = embeddings.tolist()

collection.add(
    ids=ids,
    embeddings=embeddings_list,
    documents=documents,
    metadatas=metadatas
)

print("Number of items in collection after insert:", collection.count())