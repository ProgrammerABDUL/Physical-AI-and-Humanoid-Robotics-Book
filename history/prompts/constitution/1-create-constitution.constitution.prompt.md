---
id: 1
title: Create Constitution
stage: constitution
date: 2025-12-22
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: main
user: user
command: /sp.constitution
labels: [constitution,setup,initial]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
---

## Prompt

```
/sp.constitution

Project Title: AI-Driven Book + Integrated RAG Chatbot

Mission:
Create a fully AI/spec-driven technical book and deploy it using Docusaurus on GitHub Pages. The project must integrate a Retrieval-Augmented Generation (RAG) chatbot inside the published book. The chatbot must answer user questions strictly based on book content or user-selected text, using modern AI tooling and cloud services.

Core Deliverables:
1. **AI/Spec-Driven Book Creation**
   - Use Spec-Kit Plus for planning, scoping, structuring, and generating the book.
   - Use Claude Code to write, refactor, and maintain the book's content.
   - Implement the book using **Docusaurus**.
   - Deploy the final book to **GitHub Pages**.
   - Ensure content is modular, specification-driven, and production-ready.

2. **Integrated RAG Chatbot**
   - Build a fully functional **Retrieval-Augmented Generation chatbot**.
   - It must be embedded directly inside the Docusaurus book (e.g., via React component, plugin, or iframe).
   - The chatbot must:
     - Answer questions about the book.
     - Answer questions strictly based on *user-selected text* when provided.
     - Use retrieval powered by vector search and database storage.

Tech Stack Requirements:
- **OpenAI Agents / ChatKit SDKs** (for inference + agent behaviors)
- **FastAPI** (backend API serving model + retrieval)
- **Neon Serverless Postgres** (for structured metadata storage)
- **Qdrant Cloud Free Tier** (vector database for embeddings)
- **Docusaurus v3** (frontend + book publication)
- **GitHub Pages** (hosting)
- **Spec-Kit Plus** (planning/specs automation)
- **Claude Code** (code generation + refactoring)

Success Criteria:
- A complete book written through Spec-Kit modules, plans, and specs.
- Book successfully deployed on GitHub Pages and fully accessible.
- Embedded chatbot fully functional within the published site.
- Chatbot can:
  - Answer questions from the entire book.
  - Process and answer based *only* on highlighted/selected text.
- Backend system runs using FastAPI with Neon + Qdrant.
- Retrieval quality is high (accurate, relevant, grounded).
- Smooth developer experience, clear instructions, and modular architecture.

Constraints:
- All writing, planning, specs, and code must flow through Spec-Kit and Claude Code.
- No manual writing of major sections outside the Spec-Kit pipeline.
- Chatbot must operate with minimal hallucination using grounding + RAG best practices.
- All components must be open-source compatible and follow clean-code conventions.
- Deployment must use free-tier or open-source options only.

Working Style Expectations:
- Produce detailed plans using `/sp.plan`, modules using `/sp.module`, and specifications using `/sp.specify`.
- Maintain version-controlled code changes via Claude Code.
- Ensure architecture diagrams, folder structures, and API routes are defined before coding.
- Follow structured documentation principles and maintain consistency across chapters.

Output Expectations:
- A unified book repository containing:
  - `/docs` (book content)
  - `/src` (custom components)
  - `/rag-backend` (FastAPI + DB + Qdrant integration)
  - RAG Chatbot UI integrated into Docusaurus
- Clear README with setup, development workflow, and deployment instructions.
- Automated build + deployment workflow for GitHub Pages.
```

## Response snapshot

Updated the project constitution file with principles aligned to the AI-Driven Book + Integrated RAG Chatbot project requirements. Created a comprehensive constitution with core principles including specification-driven development, AI-assisted code generation, test-first development, modular architecture, grounded AI responses, and open-source compatibility. Also defined technical requirements, development workflow, and governance sections.

## Outcome

- ✅ Impact: Created foundational project constitution with 6 core principles
- 🧪 Tests: N/A for documentation update
- 📁 Files: Updated .specify/memory/constitution.md
- 🔁 Next prompts: Plan and specify the AI book and RAG chatbot components
- 🧠 Reflection: Constitution properly captures the project's core values and constraints

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin specification work for the AI book components