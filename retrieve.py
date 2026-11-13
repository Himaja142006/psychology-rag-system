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

# Step 4: Ask a question
question = input("Enter your question: ")

# Step 5: Convert question into embedding
response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=question
)

question_embedding = response.embeddings[0].values

# Step 6: Search ChromaDB
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=3
)

# Step 7: Display retrieved information
print("\nRelevant information retrieved from PDF:\n")

for index, document in enumerate(results["documents"][0], start=1):

    print(f"\n--- Retrieved Chunk {index} ---\n")
    print(document)