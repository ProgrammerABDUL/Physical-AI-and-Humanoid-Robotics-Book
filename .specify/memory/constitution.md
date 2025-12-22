<!-- SYNC IMPACT REPORT
Version change: N/A -> 1.0.0
Modified principles: None (new constitution)
Added sections: All sections (new constitution)
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/commands/*.md ✅ reviewed
Follow-up TODOs: None
-->

# AI-Driven Book + Integrated RAG Chatbot Constitution

## Core Principles

### Specification-Driven Development
All features and functionality must originate from and adhere to formal specifications generated through Spec-Kit Plus. No code implementation shall proceed without an approved, detailed specification. This ensures systematic development, reduces rework, and maintains architectural coherence across the AI book and RAG chatbot components.

### AI-Assisted Code Generation
All code must be generated, reviewed, and maintained using Claude Code and other AI-assisted development tools. Manual coding should be minimized to exceptional circumstances only. This principle ensures consistent, high-quality code that follows established patterns and best practices defined in the project constitution.

### Test-First Development (NON-NEGOTIABLE)
Test-driven development is mandatory: Specifications and tests are written and approved before implementation begins. All tests must initially fail, then pass after implementation. Both unit and integration tests are required for all components, especially the RAG system where correctness and reliability are critical.

### Modular Architecture
The system must be built with clean separation of concerns: Docusaurus book frontend, FastAPI backend, vector database layer, and RAG processing components. Each module should be independently deployable, testable, and maintainable. This enables parallel development and reduces system complexity.

### Grounded AI Responses
The RAG chatbot must provide responses strictly grounded in retrieved book content or user-selected text. Hallucination is prohibited. All responses must be verifiable against source material with proper citation. This ensures trustworthiness and accuracy of the AI-powered assistance.

### Open-Source Compatibility
All components, dependencies, and deployment mechanisms must maintain open-source compatibility and utilize free-tier or open-source options wherever possible. This ensures the project remains accessible, extensible, and deployable by the community without licensing constraints.

## Technical Requirements

The project must adhere to the specified technology stack: Docusaurus v3 for frontend, FastAPI for backend, Neon Serverless Postgres for metadata, Qdrant Cloud Free Tier for vector storage, and OpenAI Agents/ChatKit SDKs for AI functionality. All architectural decisions must align with these technology choices and their respective constraints.

## Development Workflow

Development follows the Spec-Kit Plus lifecycle: specification → planning → task breakdown → implementation → testing → deployment. All changes must flow through this pipeline with proper documentation. Feature branches must be created for all work, with pull requests requiring specification alignment verification before merging.

## Governance

This constitution governs all development activities and supersedes any conflicting practices. Amendments require formal documentation and approval through the project's established governance process. All team members must verify compliance with these principles during code reviews and development activities.

**Version**: 1.0.0 | **Ratified**: 2025-12-22 | **Last Amended**: 2025-12-22
