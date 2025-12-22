from typing import List
import re
from src.config.settings import settings

class TextSplitter:
    """
    Utility for splitting text into chunks for RAG processing.
    """

    def __init__(self, chunk_size: int = None, chunk_overlap: int = None):
        self.chunk_size = chunk_size or settings.CHUNK_SIZE
        self.chunk_overlap = chunk_overlap or settings.CHUNK_OVERLAP

    def split_text(self, text: str) -> List[str]:
        """
        Split text into chunks of specified size with overlap.
        """
        if len(text) <= self.chunk_size:
            return [text]

        chunks = []
        start = 0

        while start < len(text):
            # Determine the end position
            end = start + self.chunk_size

            # If we're near the end, include the remainder
            if end >= len(text):
                chunks.append(text[start:])
                break

            # Try to break at sentence boundary
            chunk = text[start:end]

            # Find the last sentence ending within the chunk
            sentence_end = max(
                chunk.rfind('. '),
                chunk.rfind('? '),
                chunk.rfind('! '),
                chunk.rfind('\n'),
                chunk.rfind('.\n'),
                chunk.rfind('?\n'),
                chunk.rfind('!\n')
            )

            # If we found a sentence boundary and it's not too close to the start
            if sentence_end != -1 and sentence_end > self.chunk_overlap:
                actual_end = start + sentence_end + 1
                chunks.append(text[start:actual_end])
                start = actual_end - self.chunk_overlap
            else:
                # If no good sentence boundary, just take the chunk
                chunks.append(chunk)
                start = end - self.chunk_overlap

        # Filter out any empty chunks
        chunks = [chunk for chunk in chunks if chunk.strip()]

        return chunks

    def split_by_headers(self, text: str) -> List[str]:
        """
        Split text based on markdown headers.
        """
        # This is a simple implementation - in practice, you might want a more sophisticated approach
        header_pattern = r'\n#{1,6}\s+.*?\n'
        sections = re.split(header_pattern, text)

        # Remove empty sections and clean up
        sections = [section.strip() for section in sections if section.strip()]

        # Now split large sections further if needed
        final_chunks = []
        for section in sections:
            if len(section) > self.chunk_size:
                # If section is too large, split it further
                sub_chunks = self.split_text(section)
                final_chunks.extend(sub_chunks)
            else:
                final_chunks.append(section)

        return final_chunks