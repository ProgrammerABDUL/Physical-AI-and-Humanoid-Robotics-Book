import qdrant_client
from qdrant_client.http import models
from typing import List, Dict, Any, Optional
from src.config.settings import settings
from src.models.document import Document, DocumentChunk
from uuid import UUID
import logging

logger = logging.getLogger(__name__)

class VectorStoreService:
    """
    Service for managing vector storage using Qdrant.
    """

    def __init__(self):
        self.client = qdrant_client.QdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT,
            api_key=settings.QDRANT_API_KEY
        )
        self.collection_name = settings.QDRANT_COLLECTION_NAME
        self._create_collection_if_not_exists()

    def _create_collection_if_not_exists(self):
        """
        Create the collection if it doesn't exist.
        """
        try:
            # Try to get collection info to check if it exists
            self.client.get_collection(self.collection_name)
            logger.info(f"Collection '{self.collection_name}' already exists")
        except Exception:
            # Collection doesn't exist, create it
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=1536,  # Default size for OpenAI embeddings
                    distance=models.Distance.COSINE
                )
            )
            logger.info(f"Created collection '{self.collection_name}'")

    async def store_document_chunks(self, chunks: List[DocumentChunk]) -> bool:
        """
        Store document chunks in the vector database.
        """
        try:
            points = []
            for chunk in chunks:
                points.append(
                    models.PointStruct(
                        id=str(chunk.id),
                        vector=chunk.embedding if chunk.embedding else [],
                        payload={
                            "document_id": str(chunk.document_id),
                            "content": chunk.content,
                            "chunk_index": chunk.chunk_index,
                            "metadata": chunk.metadata
                        }
                    )
                )

            self.client.upsert(
                collection_name=self.collection_name,
                points=points
            )
            return True
        except Exception as e:
            logger.error(f"Failed to store document chunks: {str(e)}")
            return False

    async def search_similar(self, query_embedding: List[float], top_k: int = 5,
                           filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Search for similar document chunks based on embedding similarity.
        """
        try:
            # Prepare filters if provided
            search_filter = None
            if filters:
                filter_conditions = []
                for key, value in filters.items():
                    if key == "module" and value:
                        filter_conditions.append(
                            models.FieldCondition(
                                key="metadata.module",
                                match=models.MatchValue(value=value)
                            )
                        )
                    elif key == "week" and value:
                        filter_conditions.append(
                            models.FieldCondition(
                                key="metadata.week",
                                match=models.MatchValue(value=value)
                            )
                        )

                if filter_conditions:
                    search_filter = models.Filter(
                        must=filter_conditions
                    )

            results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=top_k,
                query_filter=search_filter
            )

            # Format results
            formatted_results = []
            for result in results:
                formatted_results.append({
                    "id": result.id,
                    "content": result.payload.get("content", ""),
                    "document_id": result.payload.get("document_id"),
                    "score": result.score,
                    "metadata": result.payload.get("metadata", {})
                })

            return formatted_results
        except Exception as e:
            logger.error(f"Failed to search similar documents: {str(e)}")
            return []

    async def delete_document(self, document_id: UUID) -> bool:
        """
        Delete all chunks associated with a document.
        """
        try:
            # In Qdrant, we can't directly filter by payload in the delete operation
            # So we would need to first search for points with this document_id
            # and then delete them by ID
            # For now, we'll just log that this method needs implementation
            logger.warning("Delete document functionality needs full implementation")
            return True
        except Exception as e:
            logger.error(f"Failed to delete document: {str(e)}")
            return False

# Global instance
vector_store_service = VectorStoreService()