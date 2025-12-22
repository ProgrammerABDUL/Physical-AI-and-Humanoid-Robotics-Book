# ROS 2 Debugging Techniques

This document covers essential debugging techniques for ROS 2 applications, including tools, methodologies, and best practices for identifying and resolving issues in robotic systems.

## Debugging Tools Overview

ROS 2 provides a comprehensive set of debugging tools that can help you understand the behavior of your robot system.

### Command Line Tools

#### ros2 topic
Monitor and interact with topics:
```bash
# List all topics
ros2 topic list

# Echo messages on a topic
ros2 topic echo /topic_name

# Show topic information
ros2 topic info /topic_name

# Publish a message to a topic
ros2 topic pub /topic_name std_msgs/String "data: 'hello'"

# Monitor message rate
ros2 topic hz /topic_name

# Monitor bandwidth
ros2 topic bw /topic_name
```

#### ros2 service
Work with services:
```bash
# List all services
ros2 service list

# Call a service
ros2 service call /service_name service_package/srv/ServiceType

# Show service information
ros2 service info /service_name
```

#### ros2 node
Manage nodes:
```bash
# List all nodes
ros2 node list

# Show node information
ros2 node info /node_name

# List node parameters
ros2 param list /node_name
```

#### ros2 lifecycle
Manage lifecycle nodes:
```bash
# List lifecycle nodes
ros2 lifecycle list /node_name

# Get lifecycle state
ros2 lifecycle get /node_name

# Change lifecycle state
ros2 lifecycle configure /node_name
ros2 lifecycle activate /node_name
ros2 lifecycle deactivate /node_name
```

### GUI Tools

#### RViz
RViz is a 3D visualization tool that can display robot models, sensor data, paths, and other information:
- Visualize robot models using TF
- Display sensor data (laser scans, point clouds, images)
- Show paths, trajectories, and markers
- Interactive markers for controlling the robot

#### rqt
rqt is a Qt-based framework that provides various plugins for monitoring and debugging:
- rqt_graph: Visualize the node graph
- rqt_plot: Plot numerical values over time
- rqt_console: Monitor log messages
- rqt_bag: Play and analyze bag files
- rqt_reconfigure: Dynamically reconfigure parameters

## Debugging Strategies

### Systematic Approach

1. **Reproduce the issue**: Ensure you can consistently reproduce the problem
2. **Isolate the component**: Identify which node or component is causing the issue
3. **Check the data flow**: Trace messages from publishers to subscribers
4. **Examine timing**: Check for timing-related issues
5. **Review configurations**: Verify parameters and configurations

### Common Issues and Solutions

#### Topic Connection Issues
- Check topic names for typos
- Verify message types match between publisher and subscriber
- Check Quality of Service (QoS) settings compatibility
- Ensure nodes are in the same namespace if required

#### Performance Issues
- Monitor CPU and memory usage
- Check message frequency and size
- Analyze network bandwidth usage
- Consider using intra-process communication

#### Timing Issues
- Use appropriate time synchronization
- Check for blocking operations in callbacks
- Consider using asynchronous processing
- Monitor real-time constraints

## Logging Best Practices

### Log Levels
- **DEBUG**: Detailed information for diagnosing problems
- **INFO**: General information about program execution
- **WARN**: Indication of potential issues
- **ERROR**: Errors that don't prevent program execution
- **FATAL**: Critical errors that cause program termination

### Effective Logging
- Use appropriate log levels
- Include context information (node name, function, etc.)
- Avoid logging sensitive information
- Use structured logging for easier analysis

## Profiling and Performance Analysis

### CPU Profiling
- Use system profilers (perf, gprof) to identify bottlenecks
- Monitor callback execution times
- Check for unnecessary computations in critical loops

### Memory Analysis
- Monitor memory usage over time
- Check for memory leaks
- Use tools like valgrind for detailed analysis

### Network Analysis
- Monitor topic message rates
- Check bandwidth usage
- Analyze Quality of Service settings

## Debugging in Simulation vs. Real Robots

### Simulation Debugging
- Faster iteration cycles
- Reproducible conditions
- Access to ground truth data
- Ability to pause and step through execution

### Real Robot Debugging
- Safety considerations
- Limited access to internal states
- Environmental uncertainties
- Need for remote debugging capabilities

## Remote Debugging

For debugging on embedded systems or remote robots:
- SSH access to robot systems
- Remote logging and monitoring
- Cross-compilation for debugging builds
- Network-based debugging tools

## Testing and Validation

### Unit Testing
- Test individual components in isolation
- Mock dependencies for controlled testing
- Use testing frameworks (Google Test for C++, unittest for Python)

### Integration Testing
- Test component interactions
- Validate message flows
- Verify system behavior under various conditions

### System Testing
- Test complete robot behavior
- Validate against requirements
- Performance and stress testing

## Next Steps

With a solid understanding of ROS 2 fundamentals, you're ready to move to [Week 6: Simulation with Gazebo and Unity](../week6-simulation/index.md) where you'll learn about robot simulation environments.