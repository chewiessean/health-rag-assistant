# Health RAG Assistant

A Retrieval-Augmented Generation (RAG) project exploring how to build an AI system that answers health-related questions using retrieved context instead of relying purely on a language model's built-in knowledge.

## Progress Log

### Part 1 - Core Concepts
Studied the foundational building blocks of a RAG pipeline and implemented small test scripts:

- **LLM API calls**: sent a prompt to the Gemini API and received a response programmatically (`llm_test.py`).
- **Embeddings**: converted text into numerical vectors and computed cosine similarity between sentences to observe how semantically similar sentences cluster together (`embedding_test.py`).
- **Why not just feed everything to the LLM?**: limited context windows, cost, and irrelevant information degrading answer quality.
- **Vector databases**: conceptually, how tools like Chroma of FAISS allow fast similarity search over large numbers of embeddings.

### Part 2 - Data Collection & Chunking
Collected raw health information and prepared it for retrieval.

- **Data collection**: gathered health topic descriptions (e.g. diabetes, asthma) from reliable sources and saved them as structured JSON records, each containing a `source` and `text` field (`data/health_data.json`).
- **Chunking**: implemented a script (`chunk_data.py`) that splits each record's text into smaller paragraph-level chunks, preserving the original source for each chunk. Since the collected text entries were kept short for testing purposes, each entry was saved as a single chunk (no further splitting was needed).
- **Why chunking matters**: embedding models represent shorter, focused pieces of text more accurately than long documents, so breaking text into meaningful chunks improves retrieval quality later.

### Part 3 - Vector Store & First Retrieval
Set up the retrieval side of the pipeline:

- **Vector store**: installed and configured Chroma, then embedded each chunk from Part 2 and stored it alongside its text and source metadata (`embed_and_store.py`).
-  **First retrieval test**: queried the vector store with a sample question and retrieved the most similar chunks (`retrieval_test.py`). Results were reasonable but limited, since the dataset is still small and entries were kept short for testing - this will improve as the dataset grows.

### Part 4 - Connecting Retrieval and Generation
Combined retrieval and generation into a full ent-to-end RAG pipeline (`rag_pipeline.py`):

- **Prompt design**: retrieved chunks are passed into the prompt along with their sources, and the model is instructed to answer only from the given context, explicitly saying so when information is missing.
- **Testing**: expanded the dataset to include symptoms (previously only had disease definitions), which resolved an early issue where the system correctly reported insufficient data for symptom-related questions. After fix, the pipeline produced accurate, source-attributed answers (e.g. correctly citing both `diabetes` and `diabetes_type2` sources for a symptoms question).
- **Robustness check**: confirmed the system correctly responds with "not enough information" both for completely unrelated topics and for gaps within a known disease's data, rather than hallucinating an answer.

## Tech Stack (planned)
- Python
- Gemini API
- sentence-transformers (embeddings)
- JSON (structured data storage)
- Chroma (vector database)
- Streamlit or Flask (interface)
