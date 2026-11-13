# Psychology RAG System

## Project Overview

This project implements a Retrieval-Augmented Generation (RAG) system using a psychology textbook PDF as its knowledge source.

The system retrieves relevant information from the document and uses Google's Gemini model to generate answers based on the retrieved content.

Unlike a normal LLM chatbot, this system uses document retrieval to ground its answers in the provided source.

## Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- ChromaDB
- PyMuPDF
- Python-dotenv

## Project Workflow

1. Extract text from the PDF document.
2. Split the extracted text into smaller chunks.
3. Generate embeddings for each chunk using Gemini.
4. Store the embeddings in ChromaDB.
5. Convert user questions into embeddings.
6. Retrieve relevant document chunks.
7. Generate answers using Gemini based on the retrieved context.

## Project Structure

```text
rag-system/
│
├── app/
│   ├── document_loader.py
│   ├── text_chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retrieval.py
│   └── generation.py
│
├── documents/
│   └── psychology.pdf
│
├── data/
│
├── main.py
├── extract_text.py
├── chunk_text.py
├── generate_embeddings.py
├── store_embeddings.py
├── retrieve.py
├── generate_answer.py
├── compare_rag.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone  https://github.com/Himaja142006/psychology-rag-system.git
```

### 2. Navigate to the project folder

```bash
cd psychology-rag-system
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the API key

Create a `.env` file in the project folder and add your Gemini API key:

```text
GEMINI_API_KEY=your_actual_api_key
```

## Running the Project

Before running the application for the first time, generate the document embeddings and populate ChromaDB using the provided ingestion scripts in this order:

1. `extract_text.py`
2. `chunk_text.py`
3. `generate_embeddings.py`
4. `store_embeddings.py`

Then start the RAG application:

```bash
python main.py
```

Enter your questions in the terminal to receive answers based on the psychology document.

Type `exit` to close the application.

## RAG vs Non-RAG

This project also demonstrates the difference between a normal LLM response and a RAG-based response.

- **Non-RAG:** The LLM answers using its general knowledge.
- **RAG:** The LLM retrieves relevant information from the provided document before generating an answer.

The comparison can be demonstrated using:

```bash
python compare_rag.py
```

## Key Learning Outcomes

- Understanding Retrieval-Augmented Generation.
- PDF text extraction and preprocessing.
- Text chunking and overlapping.
- Embedding generation.
- Vector database integration using ChromaDB.
- Semantic search and information retrieval.
- Context-based answer generation using Gemini.
- Comparing RAG and non-RAG responses.

## Author

Developed as part of an AI/GenAI internship learning project.