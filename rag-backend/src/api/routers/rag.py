from fastapi import APIRouter, HTTPException, Depends
from src.models.query import QueryRequest, QueryResponse
from src.services.rag_service import rag_service
from src.api.dependencies import get_rag_service
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/rag/query", response_model=QueryResponse)
async def query_endpoint(query_request: QueryRequest) -> QueryResponse:
    """
    Process a RAG query and return a response with sources.
    """
    try:
        response = await rag_service.query(query_request)
        return response
    except Exception as e:
        logger.error(f"Error in RAG query endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

@router.post("/rag/validate")
async def validate_endpoint(query: str, response: str, context: str):
    """
    Validate that a response is grounded in the provided context.
    """
    try:
        is_valid = await rag_service.validate_response_accuracy(query, response, context)
        return {"is_valid": is_valid}
    except Exception as e:
        logger.error(f"Error in RAG validation endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error validating response: {str(e)}")