import openai
from typing import List, Optional
from src.config.settings import settings
from openai import OpenAI

class EmbeddingService:
    """
    Service for generating and managing embeddings using OpenAI API.
    """

    def __init__(self):
        if settings.OPENAI_API_KEY:
            self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        else:
            raise ValueError("OPENAI_API_KEY environment variable is required")

    async def generate_embedding(self, text: str) -> List[float]:
        """
        Generate embedding for a single text.
        """
        try:
            response = self.client.embeddings.create(
                input=text,
                model=settings.OPENAI_EMBEDDING_MODEL
            )
            return response.data[0].embedding
        except Exception as e:
            raise Exception(f"Failed to generate embedding: {str(e)}")

    async def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of texts.
        """
        try:
            response = self.client.embeddings.create(
                input=texts,
                model=settings.OPENAI_EMBEDDING_MODEL
            )
            return [item.embedding for item in response.data]
        except Exception as e:
            raise Exception(f"Failed to generate embeddings: {str(e)}")

# Global instance
embedding_service = EmbeddingService()