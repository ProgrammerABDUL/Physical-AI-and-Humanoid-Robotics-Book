import asyncio
from typing import List
from src.models.document import Document, DocumentChunk
from src.services.embedding_service import embedding_service
from src.services.vector_store_service import vector_store_service
from src.utils.text_splitter import TextSplitter
from uuid import UUID
import logging

logger = logging.getLogger(__name__)

class ContentIndexService:
    """
    Service for indexing course content into the vector database.
    """

    def __init__(self):
        self.text_splitter = TextSplitter()

    async def index_document(self, document: Document) -> bool:
        """
        Index a document by splitting it into chunks, generating embeddings, and storing in vector database.
        """
        try:
            # Split document into chunks
            chunks = self.text_splitter.split_text(document.content)

            # Create DocumentChunk objects
            document_chunks = []
            for i, chunk_content in enumerate(chunks):
                chunk = DocumentChunk(
                    document_id=document.id,
                    content=chunk_content,
                    chunk_index=i,
                    metadata={
                        "title": document.title,
                        "source": document.source,
                        "module": document.module,
                        "week": document.week,
                        "tags": document.tags
                    }
                )
                document_chunks.append(chunk)

            # Generate embeddings for all chunks
            chunk_texts = [chunk.content for chunk in document_chunks]
            embeddings = await embedding_service.generate_embeddings(chunk_texts)

            # Assign embeddings to chunks
            for i, embedding in enumerate(embeddings):
                document_chunks[i].embedding = embedding

            # Store chunks in vector database
            success = await vector_store_service.store_document_chunks(document_chunks)

            if success:
                logger.info(f"Successfully indexed document '{document.title}' with {len(document_chunks)} chunks")
                return True
            else:
                logger.error(f"Failed to store document chunks for '{document.title}'")
                return False
        except Exception as e:
            logger.error(f"Failed to index document '{document.title}': {str(e)}")
            return False

    async def index_documents(self, documents: List[Document]) -> int:
        """
        Index multiple documents and return the count of successfully indexed documents.
        """
        success_count = 0
        for document in documents:
            success = await self.index_document(document)
            if success:
                success_count += 1

        logger.info(f"Indexed {success_count}/{len(documents)} documents successfully")
        return success_count

    async def update_document(self, document: Document) -> bool:
        """
        Update an existing document by deleting old chunks and indexing new ones.
        """
        # For now, we'll just index the document again
        # In a full implementation, we would delete the old document first
        return await self.index_document(document)

    async def batch_index_from_file(self, file_path: str, module: str, week: int) -> bool:
        """
        Read content from a file and index it as a document.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            document = Document(
                title=file_path.split('/')[-1],  # Use filename as title
                content=content,
                source=file_path,
                module=module,
                week=week
            )

            return await self.index_document(document)
        except Exception as e:
            logger.error(f"Failed to batch index from file {file_path}: {str(e)}")
            return False

# Global instance
content_index_service = ContentIndexService()