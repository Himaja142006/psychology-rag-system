import os
import json
from dotenv import load_dotenv
from google import genai

# Step 1: Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Step 2: Connect to Gemini
client = genai.Client(api_key=api_key)

# Step 3: Read the text chunks
with open("data/extracted_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunk_size = 1000
overlap = 200

chunks = []
start = 0

while start < len(text):
    end = start + chunk_size
    chunks.append(text[start:end])
    start += chunk_size - overlap

# Step 4: Generate embeddings
embeddings = []

for index, chunk in enumerate(chunks, start=1):

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=chunk
    )

    embedding = response.embeddings[0].values

    embeddings.append({
        "chunk_id": index,
        "text": chunk,
        "embedding": embedding
    })

    print(f"Generated embedding for chunk {index}/{len(chunks)}")

# Step 5: Save embeddings
os.makedirs("data", exist_ok=True)

with open("data/embeddings.json", "w", encoding="utf-8") as file:
    json.dump(embeddings, file, indent=4)

print("\nEmbedding generation completed successfully!")
print("Total embeddings generated:", len(embeddings))