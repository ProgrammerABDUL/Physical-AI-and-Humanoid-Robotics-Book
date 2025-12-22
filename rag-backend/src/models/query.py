from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from uuid import UUID

class QueryRequest(BaseModel):
    """
    Model for RAG query requests.
    """
    query: str
    top_k: int = Field(default=5, ge=1, le=20)  # Between 1 and 20 results
    module_filter: Optional[str] = None  # Filter by specific module
    week_filter: Optional[int] = None  # Filter by specific week
    selected_text: Optional[str] = None  # Selected text for context-specific queries
    temperature: float = Field(default=0.7, ge=0.0, le=1.0)  # For LLM generation
    max_tokens: int = Field(default=500, ge=1, le=2000)  # Max tokens in response

class QueryResponse(BaseModel):
    """
    Model for RAG query responses.
    """
    query: str
    response: str
    sources: List[Dict[str, Any]]  # List of source documents used
    context_used: str  # The context provided to the LLM
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    query_id: UUID

class HealthCheckResponse(BaseModel):
    """
    Model for health check responses.
    """
    status: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    services: Dict[str, str]  # Status of dependent services