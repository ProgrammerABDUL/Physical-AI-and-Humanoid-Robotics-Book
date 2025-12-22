import openai
from typing import List, Dict, Any
from src.models.query import QueryRequest, QueryResponse
from src.services.embedding_service import embedding_service
from src.services.vector_store_service import vector_store_service
from src.config.settings import settings
from src.models.document import DocumentQuery
from uuid import UUID, uuid4
import logging

logger = logging.getLogger(__name__)

class RAGService:
    """
    Service for Retrieval-Augmented Generation functionality.
    Combines document retrieval with language model generation.
    """

    def __init__(self):
        if settings.OPENAI_API_KEY:
            self.client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        else:
            raise ValueError("OPENAI_API_KEY environment variable is required")

    async def query(self, query_request: QueryRequest) -> QueryResponse:
        """
        Process a query using RAG approach.
        """
        try:
            # Generate embedding for the query
            query_embedding = await embedding_service.generate_embedding(query_request.query)

            # Prepare filters
            filters = {}
            if query_request.module_filter:
                filters["module"] = query_request.module_filter
            if query_request.week_filter:
                filters["week"] = query_request.week_filter

            # Search for similar content in the vector store
            search_results = await vector_store_service.search_similar(
                query_embedding=query_embedding,
                top_k=query_request.top_k,
                filters=filters
            )

            if not search_results:
                # If no relevant content found, return a response indicating this
                return QueryResponse(
                    query=query_request.query,
                    response="I couldn't find relevant information in the course content to answer your question.",
                    sources=[],
                    context_used="",
                    query_id=uuid4()
                )

            # Combine the retrieved content to form context
            context_parts = []
            sources = []
            for result in search_results:
                context_parts.append(result["content"])
                sources.append({
                    "content_snippet": result["content"][:200] + "..." if len(result["content"]) > 200 else result["content"],
                    "score": result["score"],
                    "metadata": result["metadata"]
                })

            # Combine context with selected text if provided
            if query_request.selected_text:
                context = f"Context from course content:\n{' '.join(context_parts)}\n\nSelected text for specific question:\n{query_request.selected_text}"
            else:
                context = f"Context from course content:\n{' '.join(context_parts)}"

            # Use OpenAI to generate a response based on the context and query
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are an AI assistant for the Physical AI & Humanoid Robotics course. "
                        "Answer questions based only on the provided course content context. "
                        "If the context doesn't contain enough information to answer the question, "
                        "say so explicitly. Be accurate, concise, and helpful."
                    )
                },
                {
                    "role": "user",
                    "content": f"Context: {context}\n\nQuestion: {query_request.query}\n\nPlease provide a detailed answer based on the context."
                }
            ]

            response = self.client.chat.completions.create(
                model=settings.OPENAI_CHAT_MODEL,
                messages=messages,
                temperature=query_request.temperature,
                max_tokens=query_request.max_tokens
            )

            # Extract the generated response
            generated_response = response.choices[0].message.content

            return QueryResponse(
                query=query_request.query,
                response=generated_response,
                sources=sources,
                context_used=context,
                query_id=uuid4()
            )
        except Exception as e:
            logger.error(f"Error processing RAG query: {str(e)}")
            raise Exception(f"Failed to process query: {str(e)}")

    async def validate_response_accuracy(self, query: str, response: str, context: str) -> bool:
        """
        Validate that the response is grounded in the provided context.
        This is a simplified implementation - in practice, you might use more sophisticated validation.
        """
        # Check if response contains information that can be traced back to context
        # This is a basic check and could be enhanced with more sophisticated NLP techniques
        response_lower = response.lower()
        context_lower = context.lower()

        # Simple validation: check if response contains key terms from context
        context_words = set(context_lower.split()[:50])  # First 50 words as sample
        response_words = set(response_lower.split())

        # If there's significant overlap in terms, consider it valid
        common_words = context_words.intersection(response_words)
        if len(common_words) > 0:
            return True

        return False

# Global instance
rag_service = RAGService()