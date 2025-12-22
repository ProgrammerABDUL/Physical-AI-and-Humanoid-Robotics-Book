# API Contract: RAG Service for Physical AI & Humanoid Robotics Book

**Feature**: 2-physical-ai-robotics-book
**Date**: 2025-12-22
**Version**: 1.0
**Status**: Draft

## Overview

This document defines the API contract for the Retrieval-Augmented Generation (RAG) service that powers the in-book chatbot for the Physical AI & Humanoid Robotics course book. The service provides semantic search capabilities over course content and generates contextually relevant responses to student queries.

## Base URL
```
https://api.physical-ai-book.com/v1  # Production
http://localhost:8000               # Development
```

## Authentication

All API requests require an API key in the header:
```
Authorization: Bearer {api_key}
```

## Common Headers
- `Content-Type: application/json`
- `Accept: application/json`

## API Endpoints

### 1. Query Processing

#### POST /api/rag/query
Submit a query to the RAG system and receive a response based on course content.

**Request:**
```json
{
  "query": "string (required) - The question or query text",
  "session_id": "string (required) - Unique session identifier",
  "selected_text": "string (optional) - Text selected by user for context-specific queries",
  "module_filter": "string (optional) - Module ID to limit search scope",
  "week_filter": "string (optional) - Week ID to limit search scope"
}
```

**Response (200 OK):**
```json
{
  "response_id": "string - Unique response identifier",
  "query": "string - The original query",
  "response": "string - The AI-generated response",
  "sources": [
    {
      "document_id": "string - ID of source document",
      "title": "string - Title of source document",
      "module_id": "string - Module containing the source",
      "week_id": "string - Week containing the source",
      "relevance_score": "number - 0.0-1.0 relevance score",
      "text_excerpt": "string - Excerpt from the source document"
    }
  ],
  "confidence_score": "number - 0.0-1.0 confidence in response accuracy",
  "processing_time_ms": "number - Time taken to process the query"
}
```

**Error Responses:**
- `400 Bad Request`: Invalid request parameters
- `401 Unauthorized`: Missing or invalid API key
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Processing error

### 2. Document Management

#### GET /api/documents
Retrieve a list of indexed documents.

**Query Parameters:**
- `module_id`: Filter by module ID
- `week_id`: Filter by week ID
- `limit`: Number of results (default: 50, max: 100)
- `offset`: Offset for pagination (default: 0)

**Response (200 OK):**
```json
{
  "documents": [
    {
      "id": "string - Document identifier",
      "title": "string - Document title",
      "module_id": "string - Associated module",
      "week_id": "string - Associated week",
      "topic_id": "string - Associated topic",
      "created_at": "string - ISO 8601 timestamp",
      "updated_at": "string - ISO 8601 timestamp",
      "chunk_count": "number - Number of content chunks"
    }
  ],
  "total_count": "number - Total number of documents",
  "has_more": "boolean - Whether more results are available"
}
```

#### GET /api/documents/{document_id}
Retrieve a specific document by ID.

**Response (200 OK):**
```json
{
  "id": "string - Document identifier",
  "title": "string - Document title",
  "module_id": "string - Associated module",
  "week_id": "string - Associated week",
  "content": "string - Full document content",
  "metadata": "object - Additional document metadata",
  "created_at": "string - ISO 8601 timestamp",
  "updated_at": "string - ISO 8601 timestamp"
}
```

#### POST /api/documents/index
Index new course content for RAG search.

**Request:**
```json
{
  "content": "string (required) - The content to be indexed",
  "title": "string (required) - Title of the content",
  "module_id": "string (required) - Module identifier",
  "week_id": "string (required) - Week identifier",
  "topic_id": "string (optional) - Topic identifier",
  "metadata": "object (optional) - Additional metadata"
}
```

**Response (201 Created):**
```json
{
  "document_id": "string - ID of the created document",
  "chunk_count": "number - Number of chunks created",
  "processing_status": "string - Indexing status (pending, processing, completed, failed)"
}
```

### 3. Content Search

#### POST /api/search/semantic
Perform semantic search across course content.

**Request:**
```json
{
  "query": "string (required) - Search query",
  "module_filter": "string (optional) - Module ID to limit search",
  "week_filter": "string (optional) - Week ID to limit search",
  "limit": "number (optional) - Max results (default: 10, max: 50)"
}
```

**Response (200 OK):**
```json
{
  "results": [
    {
      "document_id": "string - ID of matching document",
      "title": "string - Title of matching document",
      "module_id": "string - Module containing the result",
      "week_id": "string - Week containing the result",
      "relevance_score": "number - 0.0-1.0 relevance score",
      "content_preview": "string - Preview of the matching content",
      "chunk_order": "number - Order of the content chunk"
    }
  ],
  "query": "string - The original search query",
  "total_results": "number - Total number of matching results"
}
```

### 4. Health and Status

#### GET /health
Check the health status of the RAG service.

**Response (200 OK):**
```json
{
  "status": "string - Service status (healthy, degraded, unavailable)",
  "version": "string - Service version",
  "timestamp": "string - ISO 8601 timestamp",
  "dependencies": {
    "qdrant": "string - Status of vector database connection",
    "neon": "string - Status of metadata database connection",
    "openai": "string - Status of OpenAI API connection"
  }
}
```

#### GET /api/status
Get detailed status information about the RAG system.

**Response (200 OK):**
```json
{
  "total_documents": "number - Total number of indexed documents",
  "total_chunks": "number - Total number of content chunks",
  "indexing_status": "string - Current indexing status",
  "average_response_time": "number - Average response time in ms",
  "query_count_24h": "number - Number of queries in last 24 hours",
  "uptime": "number - Service uptime in seconds"
}
```

## Rate Limits

- Query endpoints: 100 requests per minute per API key
- Indexing endpoints: 10 requests per minute per API key
- Search endpoints: 200 requests per minute per API key

## Error Format

All error responses follow this format:
```json
{
  "error": {
    "code": "string - Error code",
    "message": "string - Human-readable error message",
    "details": "object - Additional error details (optional)"
  }
}
```

## Data Validation

### Query Length Limits
- Maximum query length: 2000 characters
- Minimum query length: 3 characters

### Text Selection Limits
- Maximum selected text length: 5000 characters
- Minimum selected text length: 10 characters (if provided)

### Content Limits
- Maximum document size: 1MB
- Maximum chunk size: 1000 tokens (approximately 750 words)

## Response Time SLA

- 95th percentile response time: <500ms
- 99th percentile response time: <1000ms
- Availability: 99.9% uptime