# Implementation Plan: Physical AI & Humanoid Robotics Course Book

**Branch**: `2-physical-ai-robotics-book` | **Date**: 2025-12-22 | **Spec**: [specs/2-physical-ai-robotics-book/spec.md](../specs/2-physical-ai-robotics-book/spec.md)

**Input**: Feature specification from `/specs/2-physical-ai-robotics-book/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Develop a comprehensive Physical AI & Humanoid Robotics course book with integrated RAG chatbot following a 13-week curriculum structure. The implementation will follow a phased approach: Research → Foundation → Analysis → Synthesis, with each module (ROS 2, Gazebo/Unity, Isaac, VLA) developed and validated before publication. The system will include Docusaurus-based book interface, FastAPI backend for RAG functionality, and vector storage in Qdrant with Neon metadata management.

## Technical Context

**Language/Version**: Python 3.11 (FastAPI backend), JavaScript/TypeScript (Docusaurus frontend), Markdown (book content)
**Primary Dependencies**: FastAPI, Docusaurus v3, Qdrant Cloud, Neon Postgres, OpenAI Agents/ChatKit SDKs, ROS 2 Humble, NVIDIA Isaac Sim 4.x, Gazebo Garden
**Storage**: Qdrant Cloud (vector embeddings), Neon Postgres (metadata), GitHub Pages (book hosting)
**Testing**: pytest (backend), Jest (frontend components), manual validation (book content accuracy)
**Target Platform**: Web-based (Docusaurus on GitHub Pages), RTX workstation for Isaac Sim, Jetson Orin for edge deployment
**Project Type**: Web application with integrated backend API
**Performance Goals**: <500ms response time for RAG queries, 99% uptime for book hosting, <2s page load times
**Constraints**: Free-tier usage only (Qdrant Cloud Free, Neon free tier), Docusaurus v3 compatibility, <3000 words per chapter, hardware-specific guidance for RTX/Jetson platforms
**Scale/Scope**: Single course book with 4 core modules, ~1000+ students potentially accessing content, 13 weeks of structured learning

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ Specification-Driven Development: Following approved spec from /specs/2-physical-ai-robotics-book/spec.md
- ✅ AI-Assisted Code Generation: All code will be generated using Claude Code
- ✅ Test-First Development: Backend APIs and RAG functionality will have tests before implementation
- ✅ Modular Architecture: Clear separation between Docusaurus frontend, FastAPI backend, and vector database layers
- ✅ Grounded AI Responses: RAG system will provide responses strictly based on course content
- ✅ Open-Source Compatibility: Using Docusaurus, FastAPI, and free-tier cloud services as specified

## Project Structure

### Documentation (this feature)

```text
specs/2-physical-ai-robotics-book/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
docs/
├── intro.md
├── week1-foundations/
│   ├── index.md
│   ├── sensors.md
│   └── physical-ai-principles.md
├── week2-foundations/
│   └── index.md
├── week3-ros/
│   ├── index.md
│   ├── ros2-fundamentals.md
│   └── urdf-intro.md
├── week4-ros/
│   ├── nodes-topics-services.md
│   └── ros2-workspaces.md
├── week5-ros/
│   ├── advanced-ros2.md
│   └── ros2-debugging.md
├── week6-simulation/
│   ├── index.md
│   ├── gazebo-basics.md
│   └── unity-digital-twin.md
├── week7-simulation/
│   ├── advanced-simulation.md
│   └── simulation-optimization.md
├── week8-isaac/
│   ├── index.md
│   ├── isaac-sim-setup.md
│   └── perception-intro.md
├── week9-isaac/
│   ├── vslam.md
│   ├── manipulation.md
│   └── isaac-ros-pipelines.md
├── week10-isaac/
│   ├── advanced-isaac.md
│   └── deployment.md
├── week11-humanoid/
│   ├── index.md
│   ├── locomotion.md
│   └── manipulation.md
├── week12-humanoid/
│   ├── robot-design.md
│   └── control-systems.md
├── week13-multimodal/
│   ├── index.md
│   ├── gpt-robotics.md
│   └── whisper-integration.md
├── hardware-guidance/
│   ├── workstation-specs.md
│   ├── jetson-deployment.md
│   ├── sensors.md
│   └── robot-platforms.md
├── lab-setup/
│   ├── physical-ai-lab.md
│   └── ether-lab.md
└── modules/
    ├── module1-ros2.md
    ├── module2-simulation.md
    ├── module3-isaac.md
    └── module4-vla.md
```

```text
src/
├── components/
│   ├── RagChatbot/
│   │   ├── RagChatbot.jsx
│   │   ├── RagChatbot.module.css
│   │   └── RagChatbot.test.js
│   └── BookNavigation/
│       ├── BookNavigation.jsx
│       └── BookNavigation.module.css
└── pages/
    └── CustomPage.jsx
```

```text
rag-backend/
├── src/
│   ├── models/
│   │   ├── embedding.py
│   │   ├── document.py
│   │   └── query.py
│   ├── services/
│   │   ├── embedding_service.py
│   │   ├── vector_store_service.py
│   │   ├── rag_service.py
│   │   └── content_index_service.py
│   ├── api/
│   │   ├── main.py
│   │   ├── endpoints/
│   │   │   ├── rag.py
│   │   │   ├── documents.py
│   │   │   └── health.py
│   │   └── dependencies.py
│   ├── config/
│   │   ├── settings.py
│   │   └── constants.py
│   └── utils/
│       ├── text_splitter.py
│       └── validators.py
├── tests/
│   ├── unit/
│   │   ├── test_embedding_service.py
│   │   └── test_rag_service.py
│   └── integration/
│       ├── test_rag_api.py
│       └── test_document_ingestion.py
├── requirements.txt
└── Dockerfile
```

```text
docusaurus.config.js
package.json
babel.config.js
static/
├── img/
├── css/
└── js/
.babelrc
.gitignore
README.md
```

**Structure Decision**: Web application with separate backend API to handle RAG functionality while maintaining Docusaurus for book content. The rag-backend will be deployed separately from the Docusaurus frontend, with the frontend making API calls to the backend for RAG chatbot functionality.

## Phased Implementation Approach

### Phase 1: Research Phase
- Identify and validate sources for ROS 2 Humble, Isaac Sim 4.x, Gazebo Garden
- Research official documentation and best practices
- Collect technical specifications for hardware guidance (RTX, Jetson Orin, sensors)
- Analyze existing RAG implementations for educational contexts

### Phase 2: Foundation Phase
- Set up GitHub repository with Docusaurus scaffold
- Create basic module structure following 13-week progression
- Implement RAG backend with FastAPI, Qdrant, and Neon
- Establish deployment pipeline to GitHub Pages
- Create initial content ingestion system for RAG

### Phase 3: Analysis Phase
- Break down each module into specific concepts and practical tasks
- Map content to weekly learning outcomes
- Design architecture diagrams for each module
- Plan code examples and simulation steps
- Define hardware-specific guidance and lab setup instructions

### Phase 4: Synthesis Phase
- Write complete module content with technical accuracy
- Implement and test all code examples
- Validate diagrams for accuracy and consistency
- Test RAG functionality with course content
- Deploy and validate complete system

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Multiple project structure (frontend + backend) | Course requires both book content delivery and RAG functionality | Single application insufficient for separate scaling needs of static content vs dynamic AI queries |
| Specific hardware dependencies | Physical AI course requires specific platforms for Isaac Sim and Jetson deployment | Generic hardware guidance would not meet course requirements for hands-on implementation |