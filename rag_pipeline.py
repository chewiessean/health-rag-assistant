import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import chromadb
from google import genai

load_dotenv()

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="health_articles")

gemini_client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def retrieve_chunks(question, n_results=3):
    question_embedding = embed_model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=n_results
    )

    chunks = []
    for i in range(len(results["ids"][0])):
        chunks.append({
            "text": results["documents"][0][i],
            "source": results["metadatas"][0][i]["source"],
            "distance": results["distances"][0][i]
        })
    return chunks

def build_prompt(question, chunks):
    context_parts = [f"[Source: {c['source']}] {c['text']}" for c in chunks]
    context_str = "\n".join(context_parts)

    prompt = f"""Context:
{context_str}
    
Question: {question}

Answer the question using only the information in the context above.
Cite the source (e.g., "according to [source]") when using specific information.
If the context does not contain enough information, say so."""

    return prompt

def ask_rag(question):
    chunks = retrieve_chunks(question)
    prompt = build_prompt(question, chunks)

    response = gemini_client.models.generate_content(
        model = "gemini-3.6-flash",
        contents = prompt
    )

    return response.text, chunks

if __name__ == "__main__":
    question = "What are the symptoms of hypertension?"

    answer, used_chunks = ask_rag(question)

    print(f"Question: {question}\n")
    print("Retrieved sources:", [c["source"] for c in used_chunks])
    print(f"\nAnswer:\n{answer}")