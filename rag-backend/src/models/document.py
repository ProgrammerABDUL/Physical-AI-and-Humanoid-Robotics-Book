from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from uuid import UUID, uuid4

class Document(BaseModel):
    """
    Model representing a document in the course content.
    """
    id: UUID = Field(default_factory=uuid4)
    title: str
    content: str
    source: str  # URL or file path where the document originated
    module: str  # Which module this document belongs to (e.g., "ROS 2", "Simulation", etc.)
    week: int  # Which week this content covers
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)
    embedding: Optional[List[float]] = None  # Vector embedding of the document content

class DocumentChunk(BaseModel):
    """
    Model representing a chunk of a document after splitting for RAG.
    """
    id: UUID = Field(default_factory=uuid4)
    document_id: UUID
    content: str
    chunk_index: int
    embedding: Optional[List[float]] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DocumentQuery(BaseModel):
    """
    Model for querying documents.
    """
    query: str
    top_k: int = 5  # Number of similar documents to retrieve
    module_filter: Optional[str] = None  # Optional filter by module
    week_filter: Optional[int] = None  # Optional filter by week
    include_metadata: bool = True
    selected_text: Optional[str] = None  # Optional selected text for context-specific queries

class DocumentResponse(BaseModel):
    """
    Model for document query responses.
    """
    query: str
    results: List[Dict[str, Any]]
    context_used: str
    response: str
    sources: List[str]
    timestamp: datetime = Field(default_factory=datetime.utcnow)