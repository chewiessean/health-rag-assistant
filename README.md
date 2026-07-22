# Health RAG Assistant

A Retrieval-Augmented Generation (RAG) project exploring how to build an AI system that answers health-related questions using retrieved context instead of relying purely on a language model's built-in knowledge.

## Progress Log

### Part 1 - Core Concepts
Studied the foundational building blocks of a RAG pipeline and implemented small test scripts:

- **LLM API calls**: sent a prompt to the Gemini API and received a response programmatically ('llm_test.py').
- **Embeddings**: converted text into numerical vectors and computed cosine similarity between sentences to observe how semantically similar sentences cluster together ('embedding_test.py').
- **Why not just feed everything to the LLM?**: limited context windows, cost, and irrelevant information degrading answer quality.
- **Vector databases**: conceptually, how tools like Chroma of FAISS allow fast similarity search over large numbers of embeddings.

## Tech Stack (planned)
- Python
- Gemini API
- sentence-transformers (embeddings)
- Chroma (vector database)
- Streamlit or Flask (interface)
