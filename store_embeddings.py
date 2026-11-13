import json
import chromadb
import os

# Step 1: Load the generated embeddings

input_path = "data/embeddings.json"

with open(input_path, "r", encoding="utf-8") as file:
    embeddings_data = json.load(file)


# Step 2: Create a persistent ChromaDB client

client = chromadb.PersistentClient(
    path="data/chroma_db"
)


# Step 3: Create or access a collection

collection = client.get_or_create_collection(
    name="psychology_documents"
)


# Step 4: Prepare data for ChromaDB

ids = []
documents = []
embeddings = []
metadatas = []

for item in embeddings_data:

    ids.append(str(item["chunk_id"]))
    documents.append(item["text"])
    embeddings.append(item["embedding"])

    metadatas.append({
        "chunk_id": item["chunk_id"]
    })


# Step 5: Store embeddings in ChromaDB

if ids:
    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )


# Step 6: Display results

print("Embeddings stored successfully in ChromaDB!")

print("Total documents stored:", collection.count())

print("Collection name: psychology_documents")

print("Database location: data/chroma_db")