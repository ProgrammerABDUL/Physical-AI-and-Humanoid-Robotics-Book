# Data Model: Physical AI & Humanoid Robotics Course Book

**Feature**: 2-physical-ai-robotics-book
**Date**: 2025-12-22
**Status**: Initial Data Model

## Course Content Data Model

### Book Content Structure
```
CourseBook
├── id: UUID
├── title: String
├── description: String
├── modules: Module[]
├── weeklyProgression: WeeklyModule[]
├── hardwareGuidance: HardwareGuide[]
└── labSetup: LabConfiguration[]
```

### Module Structure
```
Module
├── id: UUID
├── moduleId: String (e.g., "module1-ros2")
├── title: String
├── description: String
├── weeks: Week[]
├── learningObjectives: String[]
├── prerequisites: String[]
├── topics: Topic[]
├── codeExamples: CodeExample[]
├── diagrams: Diagram[]
└── assessment: Assessment[]
```

### Weekly Structure
```
Week
├── id: UUID
├── weekNumber: Integer
├── title: String
├── content: String (Markdown)
├── learningObjectives: String[]
├── practicalTasks: PracticalTask[]
├── requiredReading: String[]
└── assignments: Assignment[]
```

### Topic Structure
```
Topic
├── id: UUID
├── title: String
├── content: String (Markdown)
├── difficultyLevel: Enum (Beginner, Intermediate, Advanced)
├── duration: Integer (minutes)
├── relatedTopics: UUID[]
└── codeExamples: UUID[]
```

### Practical Task Structure
```
PracticalTask
├── id: UUID
├── title: String
├── description: String (Markdown)
├── environmentRequirements: String[] (e.g., ["ROS 2 Humble", "Isaac Sim"])
├── hardwareRequirements: HardwareComponent[]
├── steps: TaskStep[]
├── expectedOutcome: String
└── validationCriteria: String[]
```

### Task Step Structure
```
TaskStep
├── id: UUID
├── stepNumber: Integer
├── instruction: String (Markdown)
├── codeSnippet: String (optional)
├── diagramRef: UUID (optional)
└── verificationCheck: String
```

## RAG System Data Model

### Document Structure
```
Document
├── id: UUID
├── moduleId: UUID
├── weekId: UUID
├── topicId: UUID
├── title: String
├── content: String (full text content)
├── contentChunks: ContentChunk[]
├── metadata: JSON
├── createdAt: DateTime
├── updatedAt: DateTime
└── embeddingStatus: Enum (pending, processing, indexed, failed)
```

### Content Chunk Structure
```
ContentChunk
├── id: UUID
├── documentId: UUID
├── content: String (chunked text, ~512 tokens)
├── chunkOrder: Integer
├── embeddingVector: Float[] (OpenAI embedding vector)
├── embeddingId: String (Qdrant ID)
├── semanticMetadata: JSON
└── createdAt: DateTime
```

### Query and Response Structure
```
Query
├── id: UUID
├── sessionId: UUID
├── userId: UUID (optional, for analytics)
├── queryText: String
├── selectedText: String (optional, for context-specific queries)
├── queryType: Enum (general, context-specific, topic-specific)
├── timestamp: DateTime
└── response: Response (optional, populated after processing)
```

```
Response
├── id: UUID
├── queryId: UUID
├── responseText: String
├── sourceDocuments: DocumentReference[]
├── confidenceScore: Float (0.0-1.0)
├── responseMetadata: JSON
├── timestamp: DateTime
└── validationStatus: Enum (unverified, verified)
```

### Document Reference Structure
```
DocumentReference
├── documentId: UUID
├── title: String
├── moduleId: UUID
├── weekId: UUID
├── relevanceScore: Float
└── textExcerpt: String
```

## Hardware Guidance Data Model

### Hardware Component Structure
```
HardwareComponent
├── id: UUID
├── name: String
├── category: Enum (workstation, edge, sensor, robot, other)
├── specifications: JSON
├── recommendedModels: String[]
├── compatibilityNotes: String
├── pricingInfo: JSON
└── setupInstructions: String (Markdown)
```

### Workstation Configuration
```
WorkstationConfig
├── id: UUID
├── name: String
├── gpuRequirements: GPURequirement
├── cpuRequirements: CPURequirement
├── memoryRequirements: MemoryRequirement
├── storageRequirements: StorageRequirement
├── osRequirements: String
└── specialConsiderations: String
```

### GPU Requirement Structure
```
GPURequirement
├── minimumVRAM: Integer (GB)
├── recommendedVRAM: Integer (GB)
├── cudaSupport: Boolean
├── recommendedModels: String[] (e.g., ["RTX 4090", "RTX 4080"])
└── performanceNotes: String
```

## Lab Setup Data Model

### Lab Configuration
```
LabConfiguration
├── id: UUID
├── name: String (e.g., "Physical AI Lab", "Ether Lab")
├── type: Enum (onPremise, cloudNative, hybrid)
├── components: LabComponent[]
├── networkRequirements: NetworkRequirement[]
├── setupInstructions: String (Markdown)
├── latencyConsiderations: String
└── maintenanceGuide: String (Markdown)
```

### Lab Component Structure
```
LabComponent
├── id: UUID
├── name: String
├── type: Enum (simulationServer, robotControl, monitoring, storage, compute)
├── specifications: JSON
├── quantity: Integer
└── deploymentNotes: String
```

### Network Requirement Structure
```
NetworkRequirement
├── id: UUID
├── requirementType: Enum (bandwidth, latency, reliability, security)
├── minimumValue: Float
├── recommendedValue: Float
├── measurementUnit: String
└── impactNotes: String
```

## User Interaction Data Model

### Chat Session Structure
```
ChatSession
├── id: UUID
├── userId: UUID (optional)
├── startTime: DateTime
├── endTime: DateTime (optional)
├── isActive: Boolean
├── sessionMetadata: JSON
└── queries: Query[]
```

### User Preference Structure
```
UserPreference
├── id: UUID
├── userId: UUID
├── preferredModule: UUID (optional)
├── learningPace: Enum (slow, normal, fast)
├── notificationPreferences: JSON
├── bookmarkedContent: UUID[]
└── progressTracking: JSON
```

## Validation and Quality Assurance Data Model

### Content Validation Structure
```
ContentValidation
├── id: UUID
├── contentId: UUID
├── validationType: Enum (technicalAccuracy, readability, completeness, currency)
├── validatorId: UUID
├── validationDate: DateTime
├── validationResult: Enum (pass, fail, needsRevision)
├── validationNotes: String
└── revisionRequired: Boolean
```

### Quality Metric Structure
```
QualityMetric
├── id: UUID
├── metricType: Enum (responseAccuracy, userSatisfaction, contentCompleteness, systemPerformance)
├── value: Float
├── measurementDate: DateTime
├── measurementMethod: String
└── targetThreshold: Float
```