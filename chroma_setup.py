import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="health_articles")

print("Client created successfully")
print("Collection name:", collection.name)
print("Number of items in collection:", collection.count())