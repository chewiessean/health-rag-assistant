from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="health_articles")

question = "I have severe headache and nausea"

question_embedding = model.encode(question).tolist()

results = collection.query(
    query_embeddings=[question_embedding],
    n_results=3
)

print(f"Question: {question}\n")

for i in range(len(results["ids"][0])):
    chunk_id = results["ids"][0][i]
    text = results["documents"][0][i]
    distance = results["distances"][0][i]
    source = results["metadatas"][0][i]["source"]

    print (f"Rank {i+1} - source: {source} (distance: {distance:.4f})")
    print(f"  {text}\n")