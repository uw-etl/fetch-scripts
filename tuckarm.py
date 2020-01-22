import rospy
import actionlib

from moveit_python import (MoveGroupInterface)
from moveit_msgs.msg import MoveItErrorCodes

class TuckingClient(object):

	def __init__(self):
		self.move_group = MoveGroupInterface("arm", "base_link")

	def tuck(self):
		joints = ["shoulder_pan_joint", "shoulder_lift_joint", "upperarm_roll_joint",
			  "elbow_flex_joint", "forearm_roll_joint", "wrist_flex_joint", "wrist_roll_joint"]
		pose = [1.32, 1.40, -0.2, 1.72, 0.0, 1.66, 0.0]
		while not rospy.is_shutdown():
			result = self.move_group.moveToJointPosition(joints, pose, 0.02)
			if result.error_code.val == MoveItErrorCodes.SUCCESS:
				return

if __name__ == "__main__":
	#create node
	rospy.init_node("tuck")

	#setup client
	tuck_client = TuckingClient()

	#tuck the arm
	tuck_client.tuck()
