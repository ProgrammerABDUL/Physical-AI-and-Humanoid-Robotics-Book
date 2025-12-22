# Quickstart Guide: Physical AI & Humanoid Robotics Course Book

**Feature**: 2-physical-ai-robotics-book
**Date**: 2025-12-22
**Status**: Initial Quickstart

## Overview

This guide provides a quick setup process to get the Physical AI & Humanoid Robotics course book running with integrated RAG chatbot functionality. Follow these steps to set up the development environment and run both the Docusaurus book frontend and FastAPI RAG backend.

## Prerequisites

### System Requirements
- **Operating System**: Linux, macOS, or Windows with WSL2
- **Memory**: 16GB RAM minimum (32GB recommended for Isaac Sim)
- **Storage**: 50GB free space minimum
- **GPU**: NVIDIA RTX series with CUDA support (for Isaac Sim)
- **Node.js**: v18.12+ (for Docusaurus)
- **Python**: v3.11+ (for FastAPI backend)

### Software Dependencies
- Git
- Node.js and npm
- Python 3.11+
- pip
- CUDA Toolkit (for Isaac Sim integration)
- Docker (optional, for containerized deployment)

## Setting Up the Development Environment

### 1. Clone the Repository
```bash
git clone <repository-url>
cd physical-ai-and-humanoid-robotics-book
```

### 2. Set Up Backend (RAG System)

#### Install Python Dependencies
```bash
cd rag-backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Configure Environment Variables
Create a `.env` file in the `rag-backend` directory:
```env
OPENAI_API_KEY=your_openai_api_key
QDRANT_URL=your_qdrant_cloud_url
QDRANT_API_KEY=your_qdrant_api_key
NEON_DATABASE_URL=your_neon_database_url
DEBUG=true
```

#### Run Backend Server
```bash
cd rag-backend/src
uvicorn api.main:app --reload --port 8000
```

### 3. Set Up Frontend (Docusaurus Book)

#### Install Node Dependencies
```bash
npm install
```

#### Configure Docusaurus
Update `docusaurus.config.js` to point to your backend API:
```javascript
const config = {
  // ... other config
  themeConfig: {
    // ... other theme config
    ragApiUrl: 'http://localhost:8000',  // Update to your backend URL
  },
};
```

#### Run Frontend Development Server
```bash
npm run start
```

## Running the Full System

### 1. Start the RAG Backend
```bash
cd rag-backend
source venv/bin/activate
cd src
uvicorn api.main:app --reload --port 8000
```

### 2. In a separate terminal, start the Docusaurus Frontend
```bash
npm run start
```

The book will be available at `http://localhost:3000` and the RAG backend at `http://localhost:8000`.

## Initial Content Ingestion

### 1. Prepare Course Content
Ensure your course content is in the `docs/` directory following the 13-week structure.

### 2. Index Content to RAG System
```bash
cd rag-backend
source venv/bin/activate
python -c "
from src.services.content_index_service import ContentIndexService
service = ContentIndexService()
service.index_course_content('docs/')
"
```

### 3. Verify Indexing
Check the RAG system status:
```bash
curl http://localhost:8000/health
curl http://localhost:8000/api/documents/stats
```

## Testing the RAG Chatbot

### 1. Test Basic Query
```bash
curl -X POST http://localhost:8000/api/rag/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is ROS 2?",
    "session_id": "test-session"
  }'
```

### 2. Test Context-Specific Query
```bash
curl -X POST http://localhost:8000/api/rag/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Explain this concept",
    "selected_text": "ROS 2 is a flexible framework for writing robot software...",
    "session_id": "test-session"
  }'
```

## Module Development Workflow

### 1. Adding New Content
1. Create new markdown files in the appropriate week directory under `docs/`
2. Update the sidebar configuration in `sidebars.js`
3. Re-index content using the content ingestion process

### 2. Adding New Modules
1. Create module directory structure in `docs/modules/`
2. Follow the 4-module structure: ROS 2, Simulation, Isaac, VLA
3. Add module-specific diagrams and code examples
4. Re-index content for RAG system

## Deployment

### 1. Build Docusaurus Site
```bash
npm run build
```

### 2. Deploy to GitHub Pages
```bash
npm run deploy
```

### 3. Deploy Backend (if self-hosting)
```bash
# Build Docker image
cd rag-backend
docker build -t rag-backend .

# Run container
docker run -d -p 8000:8000 --env-file .env rag-backend
```

## Troubleshooting

### Common Issues

#### Backend won't start
- Ensure all environment variables are set
- Check that the Qdrant and Neon services are accessible
- Verify Python dependencies are installed

#### Frontend can't connect to backend
- Check that both services are running
- Verify the API URL configuration in Docusaurus
- Ensure no CORS issues exist

#### Content not appearing in RAG results
- Verify content was properly indexed
- Check that embeddings were generated
- Ensure the content format is compatible with the ingestion system

### Useful Commands

#### Check Backend Status
```bash
curl http://localhost:8000/health
```

#### View Indexed Documents
```bash
curl http://localhost:8000/api/documents/
```

#### Clear and Re-index Content
```bash
curl -X DELETE http://localhost:8000/api/documents/all
# Then re-run content indexing
```

## Next Steps

1. **Customize Content**: Add your specific course content to the `docs/` directory
2. **Configure Modules**: Set up the 4 core modules (ROS 2, Simulation, Isaac, VLA)
3. **Add Diagrams**: Include architecture diagrams for each module
4. **Test RAG Accuracy**: Validate that the chatbot provides accurate responses
5. **Hardware Guidance**: Add specific hardware recommendations for your setup
6. **Lab Configuration**: Document your specific lab setup requirements

## Support

For additional help:
- Check the detailed documentation in the `/docs/` directory
- Review the API documentation at `http://localhost:8000/docs`
- Consult the Docusaurus documentation for theming and customization options