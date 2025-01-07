#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from assignment_2_client.msg import PositionVelocity

def callback(msg):
    pub = rospy.Publisher('/position_velocity', PositionVelocity, queue_size=10)
    pos_vel = PositionVelocity()
    pos_vel.x = msg.pose.pose.position.x
    pos_vel.y = msg.pose.pose.position.y
    pos_vel.vel_x = msg.twist.twist.linear.x
    pos_vel.vel_z = msg.twist.twist.angular.z
    pub.publish(pos_vel)

def main():
    #global pub
    rospy.init_node('position_velocity_publisher')
    #pub = rospy.Publisher('/position_velocity', PositionVelocity, queue_size=10)
    rospy.Subscriber('/odom', Odometry, callback)
    rospy.loginfo("Node position_velocity_publisher started.")
    rospy.spin()

if __name__ == "__main__":
    main()
