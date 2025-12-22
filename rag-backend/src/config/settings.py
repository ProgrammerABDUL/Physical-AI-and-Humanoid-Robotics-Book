from pydantic_settings import Settings
from typing import List, Optional
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(Settings):
    # API Configuration
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # CORS Configuration
    ALLOWED_ORIGINS: List[str] = os.getenv("ALLOWED_ORIGINS", "http://localhost,http://localhost:3000").split(",")

    # Qdrant Configuration
    QDRANT_HOST: str = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT: int = int(os.getenv("QDRANT_PORT", "6333"))
    QDRANT_API_KEY: Optional[str] = os.getenv("QDRANT_API_KEY")
    QDRANT_COLLECTION_NAME: str = os.getenv("QDRANT_COLLECTION_NAME", "course_content")

    # OpenAI Configuration
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    OPENAI_EMBEDDING_MODEL: str = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
    OPENAI_CHAT_MODEL: str = os.getenv("OPENAI_CHAT_MODEL", "gpt-3.5-turbo")

    # Database Configuration (for metadata)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/course_metadata")

    # Application Configuration
    MAX_CONTENT_LENGTH: int = int(os.getenv("MAX_CONTENT_LENGTH", "1000000"))  # 1MB in bytes
    CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", "1000"))  # Number of characters per chunk
    CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", "100"))  # Overlap between chunks

    # Rate limiting
    RATE_LIMIT_REQUESTS: int = int(os.getenv("RATE_LIMIT_REQUESTS", "10"))
    RATE_LIMIT_WINDOW: int = int(os.getenv("RATE_LIMIT_WINDOW", "60"))  # in seconds

settings = Settings()

# Validate required settings
required_settings = [
    "OPENAI_API_KEY",
]

missing_settings = [setting for setting in required_settings if not getattr(settings, setting)]
if missing_settings:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_settings)}")