#!/usr/bin/env python3
import rospy
import actionlib
from rospy import Time
from assignment_2_2024.msg import PlanningAction, PlanningGoal
from geometry_msgs.msg import PoseStamped

def feedback_callback(feedback):
    rospy.loginfo(f"Feedback atual: {feedback.actual_pose}, State: {feedback.stat}")

def main():
    rospy.init_node('action_client')

    client = actionlib.SimpleActionClient('/reaching_goal', PlanningAction)
    rospy.loginfo("Wainting for action server...")
    client.wait_for_server()

    try:
        goal = PlanningGoal()
        goal.target_pose = PoseStamped() 
        goal.target_pose.header.frame_id = "map"  
        goal.target_pose.header.stamp = rospy.Time.now()  

        goal.target_pose.pose.position.x = float(input("Write coordinate X: "))
        goal.target_pose.pose.position.y = float(input("Write coordinate Y: "))
        goal.target_pose.pose.orientation.w = 1.0  
        
        client.send_goal(goal, feedback_cb=feedback_callback)
        rospy.loginfo("Goal sent. Wait for the result or do CTRL+C to cancel.")
        client.wait_for_result()

        result = client.get_result()
        rospy.loginfo(f"Result: {result}")
    except rospy.ROSInterruptException:
        rospy.logerr("Stoped by user")

if __name__ == "__main__":
    main()
