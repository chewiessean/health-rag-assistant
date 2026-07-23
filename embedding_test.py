from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "The cat is sleeping in the garden.",
    "The kitten is dozing off in the garden.",
    "The dog is running in the park.",
    "The weather is very nice today.",
    "Let's plant a rose in the garden.",
    "Ayse always smiles."
]

embeddings = model.encode(sentences)

print("Vector dimension of each sentence:", embeddings.shape)

similarity_matrix = cosine_similarity(embeddings)

for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):
        print(f"'{sentences[i]}' <--> '{sentences[j]}'")
        print(f"  Similarity: {similarity_matrix[i][j]:.3f}\n")