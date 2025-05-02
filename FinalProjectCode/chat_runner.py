
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))
from util.llm_utils import TemplateChat
from collections import defaultdict

#RAG System imports
import os
import glob
import time
from typing import List, Dict, Any

# Vector database, embedding, and text processing
import chromadb
from langchain.text_splitter import RecursiveCharacterTextSplitter


import ollama
import numpy as np

# Utility imports
import pandas as pd

# Simple tool processor for demonstration (replace with real tools later)
def tool_router(func):
    calls = defaultdict(list)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        calls[f'{func.__name__}_calls'].append({'name': func.__name__, 'args': args, 'kwargs': kwargs, 'result': result})
        #print('\n\nTools Called: \n', calls, '\n\n')
        return result
    return wrapper


def run_chat(**kwargs):
    chat = TemplateChat.from_file(
        **kwargs
    )

    # Start the chat loop
    first_message = chat.start_chat()
    print("Agent:", first_message)

    while True:
        try:
            user_input = input("You: ")
            if user_input.strip().lower() == "/exit":
                break
            response = chat.send(user_input)
            print("Agent:", response)

        except StopIteration as e:
            if isinstance(e.value, tuple):
                print("Agent:", e.value[0])
                print("Ending match:", e.value[1])
            break

#RAG

class OllamaEmbeddingFunction:
    """Custom embedding function that uses Ollama for embeddings"""
    
    def __init__(self, model_name="nomic-embed-text"):
        self.model_name = model_name
    
    def __call__(self, input: List[str]) -> List[List[float]]:
        """Generate embeddings for a list of texts using Ollama"""
        responses = ollama.embed(model=self.model_name, input=input)
        return responses.embeddings
    
def load_documents(data_dir: str) -> Dict[str, str]:
    """
    Load text documents from a directory
    """
    documents = {}
    for file_path in glob.glob(os.path.join(data_dir, "*.txt")):
        with open(file_path, 'r') as file:
            content = file.read()
            documents[os.path.basename(file_path)] = content
    
    print(f"Loaded {len(documents)} documents from {data_dir}")
    return documents


def chunk_documents(documents: Dict[str, str], chunk_size: int = 500, chunk_overlap: int = 50) -> List[Dict[str, Any]]:
    """
    Split documents into smaller chunks for embedding,
    using LangChain's RecursiveCharacterTextSplitter
    """
    chunked_documents = []
    
    # Create the chunker with specified parameters
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    
    for doc_name, content in documents.items():
        # Apply the chunker to the document text
        
        chunks = text_splitter.split_text(content)
        
        for i, chunk in enumerate(chunks):
            chunked_documents.append({
                "id": f"{doc_name}_chunk_{i}",
                "text": chunk,
                "metadata": {"source": doc_name, "chunk": i}
          })
    
    print(f"Created {len(chunked_documents)} chunks from {len(documents)} documents")
    return chunked_documents


def setup_chroma_db(chunks: List[Dict[str, Any]], collection_name: str = "dnd_knowledge", use_ollama_embeddings: bool = True, ollama_model: str = "nomic-embed-text") -> chromadb.Collection:
    """
    Set up ChromaDB with document chunks
    """
    # Initialize ChromaDB Ephemeral client
    client = chromadb.Client()
    # Initialize ChromaDB Persistent client
    #client = chromadb.PersistentClient(path="/path/to/save/to")
    
    # Create embedding function
    # Use custom Ollama embedding function
    embedding_function = OllamaEmbeddingFunction(model_name=ollama_model)
    print(f"Using Ollama for embeddings with model: {ollama_model}")
    
    # Create or get collection
    try:
        client.delete_collection(collection_name)
    except:
        pass
    
    collection = client.create_collection(
        name=collection_name,
        embedding_function=embedding_function
    )
    
    # Add documents to collection
    collection.add(
        ids=[chunk["id"] for chunk in chunks],
        documents=[chunk["text"] for chunk in chunks],
        metadatas=[chunk["metadata"] for chunk in chunks]
    )
    
    print(f"Added {len(chunks)} chunks to ChromaDB collection '{collection_name}'")
    return collection


def retrieve_context(collection: chromadb.Collection, query: str, n_results: int = 3) -> List[str]:
    """
    Retrieve relevant context from ChromaDB based on the query
    """
    return collection.query(query_texts=[query], n_results=n_results).get("documents")[0]


def generate_response(query: str, contexts: List[str], model: str = "mistral:latest") -> str:
    """
    Generate a response using Ollama LLM with the retrieved context
    """
    # Create prompt with context
    context_text = "\n\n".join(contexts)
    
    prompt = f"""You are a helpful assistant for Dungeons & Dragons players.
    Use the following information to answer the question.
    
    Context:
    {context_text}
    
    Question: {query}
    
    Answer:"""
    
    response = ollama.generate(
        model=model,
        prompt=prompt,
    )
    
    return response["response"]


def display_results(query: str, contexts: List[str], response: str) -> None:
    """
    Display the results in a formatted way
    """
    print("\n" + "="*80)
    print(f"QUERY: {query}")
    print("="*80)
    
    print("\nCONTEXT USED:")
    print("-"*80)
    for i, context in enumerate(contexts, 1):
        print(f"Context {i}:")
        print(context[:200] + "..." if len(context) > 200 else context)
        print()
    
    print("\nGENERATED RESPONSE:")
    print("-"*80)
    print(response)
    print("="*80 + "\n")
#RAG end

def process_response(self, response):
    # Fill out this function to process the response from the LLM
    # and make the function call 
    
    if response.message.tool_calls:
        fn_call = response.message.tool_calls[0].function
        result = process_function_call(fn_call)

        # append the tool’s output
        self.messages.append({
            'role': 'tool',
            'name': fn_call.name,
            'content': result
        })

        # re‑invoke the model so it can see the tool’s output
        response = self.completion()

        # **append** that assistant response into the history
        self.messages.append({
            'role': response.message.role,
            'content': response.message.content
        })

    return response