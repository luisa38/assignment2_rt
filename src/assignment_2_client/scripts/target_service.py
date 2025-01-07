#!/usr/bin/env python3
import rospy
from assignment_2_2024.msg import PlanningGoal
from std_srvs.srv import Trigger, TriggerResponse

last_target = None

def handle_target_service(req):
    global last_target
    if last_target:
        rospy.loginfo(f"Last goal: x={last_target[0]}, y={last_target[1]}")
        return TriggerResponse(success=True, message=f"x: {last_target[0]}, y: {last_target[1]}")
    else:
        rospy.logwarn("No goal stored yet.")
        return TriggerResponse(success=False, message="No goal found")

def goal_callback(msg):
    global last_target

    last_target = (msg.target_pose.pose.position.x, msg.target_pose.pose.position.y)
    rospy.loginfo(f"New goal: {last_target}")

def main():
    rospy.init_node('target_service')

    # Serviço para obter a última meta
    rospy.Service('/last_target', Trigger, handle_target_service)

    rospy.Subscriber('/reaching_goal/goal', PlanningGoal, goal_callback)

    rospy.loginfo("Service '/last_target' done.")
    rospy.spin()

if __name__ == "__main__":
    main()

