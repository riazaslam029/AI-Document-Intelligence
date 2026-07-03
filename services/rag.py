from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model once
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def split_document(text):
    """
    Split a document into smaller chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )

    return splitter.split_text(text)


def create_embeddings(chunks):
    """
    Generate embeddings for document chunks.
    """

    embeddings = embedding_model.encode(chunks)

    return embeddings


def build_vector_store(chunks):
    """
    Create a FAISS vector index from document chunks.
    """

    embeddings = create_embeddings(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings).astype("float32"))

    return index, chunks


def retrieve_chunks(question, index, chunks, top_k=3):
    """
    Retrieve the most relevant chunks for a question.
    """

    query_embedding = embedding_model.encode([question])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        top_k,
    )

    return [chunks[i] for i in indices[0]]

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def rag_answer(question, index, chunks):
    """
    Answer a question using Retrieval-Augmented Generation.
    """

    context = retrieve_chunks(
        question,
        index,
        chunks
    )

    prompt = f"""
You are an intelligent document assistant.

Answer ONLY using the information below.

Context:

{"\n\n".join(context)}

Question:

{question}

If the answer is not contained in the context, reply:

"I couldn't find this information in the document."
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text