# Assignment 2 - Part 1 - Research Track

## Description
This ROS1 package implements:
1. An **Action Client** to send targets (\(x, y\)) to the Action Server and optionally cancel them. It also publishes custom messages containing the robot's position and velocity.
2. A **Service Node** that returns the last target set by the Action Client.

## How to Use
1. Compile the ROS workspace:
   ```bash
   cd ~/ros_ws
   catkin_make
   ```

2. Launch the simulation:
   ```bash
   roslaunch assignment_2_client assignment.launch
   ```
3. Interact with the Action Client:
  * Enter set x and y to send a target (e.g., set 2.0 and 2.0).
  * Ctrl+c to cancel the current goal.

4. To get the last goal:
   ```bash
   rosservice call /last_target
   ```
## Expected Behaviour
* The Action Client sends targets to the Action Server.
* The robot moves to the target or cancels the goal based on user input.
* The Service Node returns the last target sent.

## Requirements
* ROS installed
* Package assignment_2_2024
