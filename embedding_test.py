from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Kedi bahçede uyuyor.",
    "Kedicik bahçede uyukluyor.",
    "Köpek parkta koşuyor.",
    "Bugün hava çok güzel.",
    "Gülü bahçeye dikelim.",
    "Ayşe sürekli gülümser."
]

embeddings = model.encode(sentences)

print("Her cümlenin vektör boyutu:", embeddings.shape)

similarity_matrix = cosine_similarity(embeddings)

for i in range(len(sentences)):
    for j in range(i+1, len(sentences)):
        print(f"'{sentences[i]}' <--> '{sentences[j]}'")
        print(f" Benzerlik: {similarity_matrix[i][j]:.3f}\n")