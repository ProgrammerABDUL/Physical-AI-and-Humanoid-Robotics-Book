# URDF Introduction: Unified Robot Description Format

URDF (Unified Robot Description Format) is an XML format used in ROS to describe robot models. It defines the physical and visual properties of a robot, including its links, joints, and other components.

## What is URDF?

URDF is an XML format that describes a robot in terms of:
- Links: Rigid parts of the robot (e.g., chassis, arms, wheels)
- Joints: Connections between links (e.g., rotational, prismatic, fixed)
- Visual elements: How the robot appears in simulation
- Collision elements: How the robot interacts physically with the environment
- Inertial properties: Mass, center of mass, and inertia tensor for each link

## Basic URDF Structure

A URDF file typically contains:

```xml
<robot name="robot_name">
  <link name="link_name">
    <visual>
      <geometry>
        <box size="0.1 0.1 0.1"/>
      </geometry>
    </visual>
    <collision>
      <geometry>
        <box size="0.1 0.1 0.1"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="1"/>
      <inertia ixx="1" ixy="0" ixz="0" iyy="1" iyz="0" izz="1"/>
    </inertial>
  </link>

  <joint name="joint_name" type="revolute">
    <parent link="parent_link"/>
    <child link="child_link"/>
    <origin xyz="0 0 0" rpy="0 0 0"/>
    <axis xyz="0 0 1"/>
    <limit lower="-1.57" upper="1.57" effort="100" velocity="1"/>
  </joint>
</robot>
```

## Links

Links represent rigid bodies in the robot. Each link can have:
- Visual properties (how it looks)
- Collision properties (how it interacts physically)
- Inertial properties (mass, center of mass, inertia)
- Optional material properties

### Visual Elements

Visual elements define how the link appears in visualizers and simulators:
- Geometry (box, cylinder, sphere, mesh)
- Origin (position and orientation relative to the link frame)
- Material (color, texture)

### Collision Elements

Collision elements define how the link interacts with the physical environment:
- Geometry (similar to visual, but often simplified for performance)
- Origin (position and orientation relative to the link frame)

### Inertial Elements

Inertial elements define the physical properties needed for dynamics simulation:
- Mass
- Inertia tensor (ixx, ixy, ixz, iyy, iyz, izz)

## Joints

Joints connect links and define how they can move relative to each other. Joint types include:

- **Fixed**: No movement between parent and child links
- **Revolute**: Rotational movement around a single axis
- **Continuous**: Like revolute but with unlimited rotation
- **Prismatic**: Linear movement along a single axis
- **Planar**: Movement in a plane
- **Floating**: 6-DOF movement (no constraints)

### Joint Properties

Joints can specify:
- Limits (for revolute and prismatic joints)
- Dynamics (damping, friction)
- Safety controllers
- Calibration

## Transmissions

Transmissions define the relationship between joints and actuators (motors). They specify how effort, velocity, and position are transmitted from the controller to the joint.

## Gazebo-Specific Elements

URDF can include Gazebo-specific elements using the `<gazebo>` tag:
- Material properties for Gazebo
- Plugin specifications
- Sensor definitions
- Simulation parameters

## Best Practices

1. **Start Simple**: Begin with a basic model and add complexity gradually
2. **Use Meshes**: For complex geometries, use mesh files instead of primitive shapes
3. **Proper Inertias**: Calculate realistic inertial properties for accurate simulation
4. **Joint Limits**: Always specify appropriate joint limits
5. **Naming Conventions**: Use consistent naming for links and joints
6. **Validation**: Use tools like `check_urdf` to validate your URDF files

## Common URDF Tools

- `check_urdf`: Validates URDF syntax and structure
- `urdf_to_graphiz`: Generates a visual representation of the kinematic tree
- RViz: Visualizes URDF models in 3D
- Gazebo: Simulates URDF models in physics environment

## Next Steps

Continue to [Week 4: Advanced ROS 2 Concepts](../week4-ros/index.md) to learn about more advanced ROS 2 topics including workspaces and launch files.