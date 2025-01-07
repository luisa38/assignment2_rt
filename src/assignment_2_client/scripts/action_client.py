#!/usr/bin/env python3
import rospy
import actionlib
from rospy import Time
from assignment_2_2024.msg import PlanningAction, PlanningGoal
from geometry_msgs.msg import PoseStamped

def feedback_callback(feedback):
    rospy.loginfo(f"Feedback atual: {feedback.actual_pose}, Estado: {feedback.stat}")

def main():
    rospy.init_node('action_client')

    client = actionlib.SimpleActionClient('/reaching_goal', PlanningAction)
    rospy.loginfo("Aguardando o servidor de ação...")
    client.wait_for_server()

    try:
        goal = PlanningGoal()
        goal.target_pose = PoseStamped()  # Inicialize o target_pose como PoseStamped
        goal.target_pose.header.frame_id = "map"  # Defina o frame_id conforme necessário
        goal.target_pose.header.stamp = rospy.Time.now()  # Adicione um timestamp

        goal.target_pose.pose.position.x = float(input("Digite a coordenada X: "))
        goal.target_pose.pose.position.y = float(input("Digite a coordenada Y: "))
        goal.target_pose.pose.orientation.w = 1.0  # Defina a orientação conforme necessário

        client.send_goal(goal, feedback_cb=feedback_callback)
        rospy.loginfo("Meta enviada. Aguarde o resultado ou pressione CTRL+C para cancelar.")
        client.wait_for_result()

        result = client.get_result()
        rospy.loginfo(f"Resultado: {result}")
    except rospy.ROSInterruptException:
        rospy.logerr("Interrompido pelo usuário.")

if __name__ == "__main__":
    main()
