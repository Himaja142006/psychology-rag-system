import chromadb
from app.embeddings import generate_embedding


def retrieve_relevant_chunks(
    question,
    n_results=3,
    persist_directory="data/chroma_db",
    collection_name="psychology_documents"
):

    # Connect to ChromaDB
    client = chromadb.PersistentClient(
        path=persist_directory
    )

    # Access the collection
    collection = client.get_collection(
        name=collection_name
    )

    # Generate question embedding
    question_embedding = generate_embedding(question)

    # Retrieve relevant chunks
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=n_results
    )

    # Extract retrieved documents
    retrieved_chunks = results["documents"][0]

    return retrieved_chunks