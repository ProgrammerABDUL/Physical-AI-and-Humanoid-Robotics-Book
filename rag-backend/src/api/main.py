from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from src.config.settings import settings
from src.api.routers import rag, documents, health

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handle startup and shutdown events.
    """
    logger.info("Starting up RAG backend service...")
    # Add startup logic here if needed
    yield
    # Add shutdown logic here if needed
    logger.info("Shutting down RAG backend service...")

def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Physical AI & Humanoid Robotics RAG API",
        description="API for Retrieval-Augmented Generation for the Physical AI & Humanoid Robotics course book",
        version="1.0.0",
        lifespan=lifespan
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        # Add any origins that should be allowed to make requests
        # For development, you might want to restrict this
    )

    # Include API routers
    app.include_router(health.router, prefix="/api", tags=["health"])
    app.include_router(rag.router, prefix="/api", tags=["rag"])
    app.include_router(documents.router, prefix="/api", tags=["documents"])

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )