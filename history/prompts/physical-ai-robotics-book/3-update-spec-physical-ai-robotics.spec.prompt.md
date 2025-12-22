---
id: 3
title: Update Spec for Physical AI Robotics Book
stage: spec
date: 2025-12-22
surface: agent
model: Claude Sonnet 4.5
feature: physical-ai-robotics-book
branch: 2-physical-ai-robotics-book
user: user
command: /sp.specify
labels: [spec,ai,robotics,education,course]
links:
  spec: specs/2-physical-ai-robotics-book/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/2-physical-ai-robotics-book/spec.md
 - specs/2-physical-ai-robotics-book/checklists/requirements.md
tests:
---

## Prompt

```
update the specification AI-Driven Book + Integrated RAG Chatbot for "Physical AI & Humanoid Robotics" Course

Target audience:
- Students enrolled in the Physical AI & Humanoid Robotics program
- Robotics developers, AI engineers, and educators building embodied-intelligence systems
- Builders integrating AI (LLMs, VLA, SLAM, Isaac) into humanoid robots
- Learners needing a unified source for ROS 2, Gazebo, Isaac Sim, VLA, and GPT-based robotics

Focus:
- Creating a complete, AI-generated course book for the "Physical AI & Humanoid Robotics" curriculum
- Integrating an in-book RAG chatbot capable of answering questions based *strictly* from course content
- Providing architecture, theory, and implementation guidance for:
  - ROS 2 (robot nervous system)
  - Gazebo & Unity (digital twin simulation)
  - NVIDIA Isaac Sim & Isaac ROS (AI perception, VSLAM, manipulation)
  - VLA (Vision-Language-Action pipelines)
  - LLM-driven cognitive robotics for command → action translation
- Enabling students to build a simulated and partially physical humanoid robot pipeline
- Ensuring the book supports classroom learning, lab setup, hardware selection, and capstone execution

Success criteria:
- Fully defines all modules of the course according to:
  - Module 1: ROS 2 + URDF
  - Module 2: Gazebo/Unity digital twin
  - Module 3: NVIDIA Isaac platform + perception + VSLAM
  - Module 4: VLA + Whisper + GPT-driven action planning
- Provides step-by-step implementation guidance for core robotics systems:
  - Hardware vendor comparisons
  - Non-essential robotics history or philosophy

Course-aligned structure requirements:
- Cover weekly progression:
  - Weeks 1–2: Foundations of Physical AI & sensors
  - Weeks 3–5: ROS 2 fundamentals
  - Weeks 6–7: Simulation with Gazebo/Unity
  - Weeks 8–10: NVIDIA Isaac ecosystem
  - Weeks 11–12: Humanoid robot design, locomotion & manipulation
  - Week 13: Conversational & multimodal robotics using GPT + Whisper
- Include hardware guidance:
  - Workstation specs for Isaac Sim (RTX GPUs)
  - Jetson Orin kits for edge deployment
  - Sensors (RealSense D435i, IMU)
  - Optional robot platforms (Unitree Go2/G1, OP3, proxies)
- Present hybrid lab design:
  - On-premise "Physical AI Lab"
  - Cloud-native "Ether Lab"
  - Latency considerations (cloud → physical robot)

Timeline:
- Book production timeline: 4–6 weeks
- RAG backend build: 2 weeks
- In-book chatbot integration: 1 week
- QA, testing, and deployment: 48–72 hours

Not building:
- A full mechanical engineering textbook on humanoid robot design
- Low-level electronics or PCB design guides
- Reinforcement learning theory beyond the practical Isaac Sim workflow
- Robotics hardware purchasing advisor beyond essential recommendations
- A general-purpose AI or robotics encyclopedia
```

## Response snapshot

Updated the specification for the AI-Driven Book with Integrated RAG Chatbot to focus specifically on the "Physical AI & Humanoid Robotics" course. The updated spec includes user scenarios tailored to students and robotics developers, functional requirements covering all four required modules (ROS 2, Simulation, Isaac, VLA), and success criteria aligned with the 13-week course progression. The specification maintains the RAG chatbot functionality while focusing the content on robotics education with specific hardware guidance and lab setup instructions.

## Outcome

- ✅ Impact: Created updated feature specification focused on Physical AI & Humanoid Robotics education
- 🧪 Tests: N/A for specification creation
- 📁 Files: Created spec.md and requirements.md in specs/2-physical-ai-robotics-book/
- 🔁 Next prompts: Plan the implementation using /sp.plan
- 🧠 Reflection: Specification now properly targets the robotics course audience with appropriate content structure

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin planning phase with /sp.plan