import chromadb


def store_embeddings(
    embedding_records,
    persist_directory="data/chroma_db",
    collection_name="psychology_documents"
):

    # Connect to ChromaDB
    client = chromadb.PersistentClient(
        path=persist_directory
    )

    # Create or access collection
    collection = client.get_or_create_collection(
        name=collection_name
    )

    # Prepare data
    ids = []
    documents = []
    embeddings = []
    metadatas = []

    for item in embedding_records:

        ids.append(str(item["chunk_id"]))
        documents.append(item["text"])
        embeddings.append(item["embedding"])

        metadatas.append({
            "chunk_id": item["chunk_id"]
        })

    # Store embeddings
    if ids:
        collection.upsert(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    return collection