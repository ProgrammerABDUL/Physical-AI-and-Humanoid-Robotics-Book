# ROS 2 Fundamentals: Nodes, Topics, and Services

This document covers the fundamental concepts of ROS 2: nodes, topics, services, and how they interact to form a distributed robot system.

## Nodes

A node is an executable that uses ROS 2 to communicate with other nodes. Nodes are the fundamental building blocks of a ROS 2 program. You can think of a node as a single process that performs a specific task within the robot system.

### Creating a Node

In ROS 2, nodes are typically implemented in one of the supported languages (C++ or Python). Each node:

1. Initializes itself with the ROS 2 communication system
2. Creates publishers, subscribers, services, or clients as needed
3. Processes callbacks when messages arrive
4. Spins to process incoming messages

### Node Names and Namespaces

Each node must have a unique name within the ROS 2 graph. Nodes can also be organized using namespaces, which provide a hierarchical naming system similar to directories in a filesystem.

## Topics and Publishers/Subscribers

Topics form the backbone of ROS 2's publish/subscribe communication model. This asynchronous communication pattern allows for loose coupling between nodes.

### Publishers and Subscribers

- **Publisher**: A node that sends messages to a topic
- **Subscriber**: A node that receives messages from a topic

The communication is unidirectional: publishers send messages without knowing who (if anyone) is subscribed, and subscribers receive messages without knowing who published them.

### Message Types

All messages published on a topic must be of the same type. ROS 2 comes with many standard message types, and users can define custom message types as well.

### Quality of Service (QoS)

ROS 2 introduces Quality of Service profiles that allow fine-tuning of communication behavior:
- Reliability: Best effort vs. reliable delivery
- Durability: Volatile vs. transient local
- History: Keep all messages vs. keep last N messages
- Deadline and lifespan settings

## Services

Services provide synchronous request/response communication between nodes. When a node makes a service call, it waits for the response before continuing.

### Service Architecture

- **Service Server**: A node that provides a service
- **Service Client**: A node that uses a service

Services are useful for operations that have a clear request/response pattern, such as:
- Parameter configuration
- Calibration routines
- Simple computational tasks

## Actions

Actions are designed for long-running tasks that may take seconds, minutes, or even hours to complete. They provide:

1. Goal requests (like services)
2. Continuous feedback during execution
3. Result responses upon completion
4. Ability to cancel ongoing actions

## Creating Packages

ROS 2 organizes code into packages, which contain nodes, libraries, and other resources. A package typically includes:

- Source code files
- Package manifest (package.xml)
- Build configuration files (CMakeLists.txt for C++, setup.py for Python)
- Launch files
- Configuration files

### Package Dependencies

Packages declare their dependencies in the package.xml file, which allows the build system to properly compile and link code.

## Communication Patterns

ROS 2 supports several communication patterns:

1. **Point-to-point**: Direct communication between two nodes
2. **One-to-many**: One publisher, multiple subscribers
3. **Many-to-one**: Multiple publishers, one subscriber (less common)
4. **Peer-to-peer**: Service-based communication

## Launch Files

Launch files allow you to start multiple nodes at once with predefined parameters and configurations. They can also handle node lifecycle management and automatic restarts.

## Parameters

Parameters provide a way to configure nodes at runtime. They can be:
- Declared within the node
- Set at launch time
- Changed dynamically during execution

## Next Steps

Continue to [URDF Introduction](./urdf-intro.md) to learn about Unified Robot Description Format, which is used to describe robot models in ROS 2.