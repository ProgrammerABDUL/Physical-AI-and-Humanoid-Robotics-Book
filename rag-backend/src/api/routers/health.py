from fastapi import APIRouter
from src.models.query import HealthCheckResponse
from src.services.embedding_service import embedding_service
from src.services.vector_store_service import vector_store_service
from datetime import datetime

router = APIRouter()

@router.get("/health", response_model=HealthCheckResponse)
async def health_check():
    """
    Health check endpoint to verify all services are running.
    """
    services_status = {}

    # Check embedding service
    try:
        # Try to generate a simple embedding to test the service
        test_embedding = await embedding_service.generate_embedding("test")
        services_status["embedding"] = "healthy" if test_embedding else "unhealthy"
    except Exception:
        services_status["embedding"] = "unhealthy"

    # Check vector store service
    try:
        # Try to perform a simple search to test the service
        test_search = await vector_store_service.search_similar([0.0] * 1536, top_k=1)
        services_status["vector_store"] = "healthy"
    except Exception:
        services_status["vector_store"] = "unhealthy"

    # Overall status
    overall_status = "healthy" if all(status == "healthy" for status in services_status.values()) else "degraded"

    return HealthCheckResponse(
        status=overall_status,
        services=services_status
    )

@router.get("/ready")
async def readiness_check():
    """
    Readiness check endpoint to verify the service is ready to accept requests.
    """
    return {"status": "ready"}