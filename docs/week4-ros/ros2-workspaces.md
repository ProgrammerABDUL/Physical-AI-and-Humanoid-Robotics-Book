# ROS 2 Workspaces and Launch Files

This document covers the advanced concepts of ROS 2 workspaces and launch files, which are essential for organizing and launching complex robot systems.

## ROS 2 Workspaces

A workspace is a directory containing ROS 2 packages that you want to build and use together. Understanding workspaces is crucial for organizing your robotics projects effectively.

### Workspace Structure

A typical ROS 2 workspace follows this structure:

```
workspace_folder/          # You choose this name
├── src/                   # Source code for packages
│   ├── package_1/
│   ├── package_2/
│   └── ...
├── build/                 # Build artifacts (created by colcon)
├── install/               # Installation directory (created by colcon)
└── log/                   # Build and runtime logs (created by colcon)
```

### Creating a New Workspace

To create a new workspace:

```bash
# Create the workspace directory structure
mkdir -p ~/ros2_ws/src

# Navigate to the workspace
cd ~/ros2_ws

# Optionally, copy packages to the src directory
# cp -r /path/to/your/packages src/

# Build all packages in the workspace
colcon build

# Source the workspace to use the packages
source install/setup.bash
```

### Sourcing Workspaces

When you have multiple workspaces, the order in which you source them matters:

```bash
# Source system installation first
source /opt/ros/humble/setup.bash

# Then source your custom workspace
source ~/ros2_ws/install/setup.bash
```

## colcon Build Tool

`colcon` is the build tool used in ROS 2. It builds packages in the correct order based on dependencies.

### Common colcon Commands

```bash
# Build all packages in the workspace
colcon build

# Build specific packages
colcon build --packages-select package_name1 package_name2

# Build and only show output for packages that fail
colcon build --event-handlers console_cohesion+

# Clean build artifacts
rm -rf build/ install/ log/
```

### Build Configuration

You can configure builds using command-line options or configuration files:

```bash
# Build with release optimizations
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release

# Build with additional compiler flags
colcon build --cmake-args -DCMAKE_CXX_FLAGS="-Wall -Wextra"
```

## Launch Files

Launch files allow you to start multiple nodes with a single command, set parameters, and manage the lifecycle of your robot system.

### XML Launch Files

XML launch files are declarative and easier to read for simple setups:

```xml
<launch>
  <!-- Include another launch file -->
  <include file="$(find-pkg-share my_robot_description)/launch/description.launch.xml"/>

  <!-- Start a node -->
  <node pkg="my_package" exec="my_node" name="my_node_name" output="screen">
    <!-- Set parameters -->
    <param name="param1" value="value1"/>
    <param name="param2" value="value2"/>

    <!-- Remap topics -->
    <remap from="original_topic" to="new_topic"/>

    <!-- Set environment variables -->
    <env name="ENV_VAR" value="env_value"/>
  </node>

  <!-- Start a node with a condition -->
  <node if="$(var enable_feature)" pkg="my_package" exec="feature_node"/>

  <!-- Define variables -->
  <let name="robot_namespace" value="my_robot"/>
</launch>
```

### Python Launch Files

Python launch files offer more flexibility and complex logic:

```python
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node, PushRosNamespace
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Declare launch arguments
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Declare launch arguments
    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use simulation (Gazebo) clock if true'
    )

    # Start a node
    my_node = Node(
        package='my_package',
        executable='my_node',
        name='my_node',
        parameters=[
            {'use_sim_time': use_sim_time},
            {'param1': 'value1'}
        ],
        remappings=[
            ('original_topic', 'new_topic')
        ],
        output='screen'
    )

    return LaunchDescription([
        declare_use_sim_time,
        my_node
    ])
```

### Launch File Best Practices

1. **Modularity**: Break complex launch files into smaller, reusable components
2. **Parameterization**: Use launch arguments to make launch files configurable
3. **Namespacing**: Use namespaces to avoid name conflicts in multi-robot systems
4. **Conditional Launch**: Use conditions to selectively start nodes
5. **Error Handling**: Include proper error handling and logging

## Parameters in Depth

Parameters are a key mechanism for configuring nodes at runtime.

### Parameter Declaration

In your node code, declare parameters to specify their types and constraints:

```cpp
// C++
this->declare_parameter("param_name", default_value);
this->declare_parameter("param_name", default_value,
                       rcl_interfaces::msg::ParameterDescriptor());
```

```python
# Python
self.declare_parameter('param_name', default_value)
```

### Parameter Files

YAML files can define parameters for nodes:

```yaml
my_node:
  ros__parameters:
    param1: value1
    param2: 42
    param3: [1.0, 2.0, 3.0]
    nested:
      param4: value4
```

### Parameter Management

Use the `ros2 param` command-line tools to manage parameters:

```bash
# List parameters of a node
ros2 param list /node_name

# Get parameter value
ros2 param get /node_name param_name

# Set parameter value
ros2 param set /node_name param_name value

# Load parameters from file
ros2 param load /node_name param_file.yaml

# Dump parameters to file
ros2 param dump /node_name
```

## Next Steps

Continue to [Week 5: Advanced ROS 2 and Debugging](../week5-ros/advanced-ros2.md) to learn about advanced ROS 2 concepts and debugging techniques.