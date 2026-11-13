from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Connect to Gemini
client = genai.Client(api_key=api_key)


def generate_answer(question, retrieved_chunks):

    # Combine retrieved chunks into context
    context = "\n\n".join(retrieved_chunks)

    # Create prompt
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

    # Generate answer using Gemini
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text