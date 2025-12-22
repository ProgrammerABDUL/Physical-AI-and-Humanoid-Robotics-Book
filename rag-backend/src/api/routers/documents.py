from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from typing import Optional
from src.models.document import Document
from src.services.content_index_service import content_index_service
import logging
import tempfile
import os

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/documents/index")
async def index_document_endpoint(
    title: str = Form(...),
    content: str = Form(...),
    source: str = Form(...),
    module: str = Form(...),
    week: int = Form(...)
):
    """
    Index a document by providing its content directly.
    """
    try:
        document = Document(
            title=title,
            content=content,
            source=source,
            module=module,
            week=week
        )

        success = await content_index_service.index_document(document)
        if success:
            return {"message": "Document indexed successfully", "success": True}
        else:
            raise HTTPException(status_code=500, detail="Failed to index document")
    except Exception as e:
        logger.error(f"Error indexing document: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error indexing document: {str(e)}")

@router.post("/documents/upload")
async def upload_document_endpoint(
    file: UploadFile = File(...),
    module: str = Form(...),
    week: int = Form(...)
):
    """
    Upload and index a document file.
    """
    try:
        # Read file content
        content = await file.read()
        content_str = content.decode('utf-8')

        # Create document
        document = Document(
            title=file.filename,
            content=content_str,
            source=file.filename,
            module=module,
            week=week
        )

        # Index the document
        success = await content_index_service.index_document(document)
        if success:
            return {"message": f"File {file.filename} uploaded and indexed successfully", "success": True}
        else:
            raise HTTPException(status_code=500, detail="Failed to index uploaded document")
    except Exception as e:
        logger.error(f"Error uploading document: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error uploading document: {str(e)}")

@router.get("/documents/health")
async def documents_health():
    """
    Health check for the documents service.
    """
    return {"status": "healthy", "service": "documents"}