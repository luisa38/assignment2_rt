#!/usr/bin/env python3
import rospy
from assignment_2_2024.msg import PlanningGoal
from std_srvs.srv import Trigger, TriggerResponse

last_target = None

def handle_target_service(req):
    global last_target
    if last_target:
        rospy.loginfo(f"Última meta registrada: x={last_target[0]}, y={last_target[1]}")
        return TriggerResponse(success=True, message=f"x: {last_target[0]}, y: {last_target[1]}")
    else:
        rospy.logwarn("Nenhum alvo foi registrado ainda.")
        return TriggerResponse(success=False, message="Nenhuma meta encontrada")

def goal_callback(msg):
    global last_target
    # Armazena a posição alvo (x, y) da meta recebida
    last_target = (msg.target_pose.pose.position.x, msg.target_pose.pose.position.y)
    rospy.loginfo(f"Meta atualizada: {last_target}")

def main():
    rospy.init_node('target_service')

    # Serviço para obter a última meta
    rospy.Service('/last_target', Trigger, handle_target_service)

    # Assinar o tópico de metas publicadas pelo action client
    rospy.Subscriber('/reaching_goal/goal', PlanningGoal, goal_callback)

    rospy.loginfo("Serviço '/last_target' pronto.")
    rospy.spin()

if __name__ == "__main__":
    main()

