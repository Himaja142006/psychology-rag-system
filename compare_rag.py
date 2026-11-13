import chromadb
from google import genai
from dotenv import load_dotenv
import os

# Step 1: Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found!")

# Step 2: Connect to Gemini
client = genai.Client(api_key=api_key)

# Step 3: Connect to ChromaDB
chroma_client = chromadb.PersistentClient(
    path="data/chroma_db"
)

collection = chroma_client.get_collection(
    name="psychology_documents"
)

# Step 4: Get user's question
question = input("Enter your question: ")


# APPROACH 1: NON-RAG

print("\n========== NON-RAG RESPONSE ==========\n")

non_rag_response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=question
)

print(non_rag_response.text)


# APPROACH 2: RAG

print("\n========== RAG RESPONSE ==========\n")

# Convert question into embedding
embedding_response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=question
)

question_embedding = embedding_response.embeddings[0].values

# Retrieve relevant information
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=3
)

retrieved_chunks = results["documents"][0]

# Combine retrieved information
context = "\n\n".join(retrieved_chunks)

# Create RAG prompt
prompt = f"""
You are a question-answering assistant.

Answer the question using ONLY the information
provided in the context.

If the answer is not available in the context,
respond with:
"The answer is not available in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""

# Generate RAG response
rag_response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

print(rag_response.text)

print("\n========== COMPARISON COMPLETED ==========")