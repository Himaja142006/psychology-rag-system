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

# Step 5: Generate question embedding
embedding_response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=question
)

question_embedding = embedding_response.embeddings[0].values

# Step 6: Retrieve relevant chunks
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=3
)

retrieved_chunks = results["documents"][0]

# Step 7: Combine retrieved chunks into context
context = "\n\n".join(retrieved_chunks)

# Step 8: Create prompt for Gemini
prompt = f"""
You are a helpful question-answering assistant.

Answer the user's question using ONLY the information
provided in the context below.

If the answer is not available in the context,
respond with:
"The answer is not available in the provided document."

Do not use outside knowledge.

Context:
{context}

Question:
{question}

Answer:
"""

# Step 9: Generate answer
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

# Step 10: Display answer
print("\n========== RAG SYSTEM ANSWER ==========\n")

print(response.text)