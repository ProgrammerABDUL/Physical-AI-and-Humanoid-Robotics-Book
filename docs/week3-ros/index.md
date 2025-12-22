# Week 3: Introduction to ROS 2

This module introduces the Robot Operating System (ROS 2), a flexible framework for writing robot software. ROS 2 is a collection of tools, libraries, and conventions that aim to simplify the task of creating complex and robust robot behavior across a wide variety of robot platforms.

## Learning Objectives

By the end of this module, you will:
- Understand the core concepts of ROS 2
- Learn about nodes, topics, services, and actions
- Set up your ROS 2 development environment
- Create your first ROS 2 packages and nodes

## What is ROS 2?

ROS 2 (Robot Operating System 2) is the next generation of the Robot Operating System. While not an actual operating system, ROS 2 is a middleware framework that provides services designed for a heterogeneous computer cluster:

- Hardware abstraction
- Device drivers
- Libraries
- Visualizers
- Message-passing
- Package management

ROS 2 is designed to be more robust, secure, and suitable for production environments compared to its predecessor.

## Key Concepts

### Nodes
A node is an executable that uses ROS 2 to communicate with other nodes. Nodes are organized into packages, which provide structure and allow for reusable components.

### Topics and Messages
Topics are named buses over which nodes exchange messages. Messages are data packets sent from one node to another via a topic.

### Services
Services provide a request/response communication pattern. A service client sends a request message to a service server, which then sends back a response.

### Actions
Actions are like services, but they're designed for long-running tasks. They provide feedback during execution and can be canceled.

## ROS 2 Architecture

ROS 2 uses a DDS (Data Distribution Service) implementation for communication between nodes. This provides:
- Real-time capabilities
- Deterministic behavior
- Scalability
- Security features

## Setting Up Your Environment

Before diving into ROS 2 development, you'll need to set up your environment:

1. Install ROS 2 Humble Hawksbill (the LTS version recommended for this course)
2. Set up your ROS 2 workspace
3. Source the ROS 2 environment

## Next Steps

Continue to [ROS 2 Fundamentals](./ros2-fundamentals.md) to dive deeper into the core concepts of ROS 2.