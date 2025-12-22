from typing import Generator
from src.services.rag_service import rag_service
from src.services.embedding_service import embedding_service
from src.services.vector_store_service import vector_store_service
from src.services.content_index_service import content_index_service

def get_rag_service():
    """
    Dependency to get the RAG service instance.
    """
    return rag_service

def get_embedding_service():
    """
    Dependency to get the embedding service instance.
    """
    return embedding_service

def get_vector_store_service():
    """
    Dependency to get the vector store service instance.
    """
    return vector_store_service

def get_content_index_service():
    """
    Dependency to get the content index service instance.
    """
    return content_index_service