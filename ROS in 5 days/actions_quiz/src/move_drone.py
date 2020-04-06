#! /usr/bin/env python
import rospy
import time
import actionlib

from actions_quiz.msg import CustomActionMsgAction, CustomActionMsgFeedback, CustomActionMsgGoal
from std_msgs.msg import Empty

class MoveClass(object):
    # create messages that are used to publish feedback/result
    _feedback = CustomActionMsgFeedback()

    def __init__(self):
        # creates the action server
        self._as = actionlib.SimpleActionServer("action_custom_msg_as", CustomActionMsgAction, self.goal_callback, False)
        self._as.start()


    def goal_callback(self, goal):
        # this callback is called when the action server is called.
        # this is the function that computes the Fibonacci sequence
        # and returns the sequence to the node that called the action server
    
        # helper variables
        r = rospy.Rate(1)
        success = True
        # publish info to the console for the user
        rospy.loginfo('"move_drone": Executing')
        self._pub_takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
        self._takeoff_msg = Empty()
        self._pub_land = rospy.Publisher('/drone/land', Empty, queue_size=1)
        self._land_msg = Empty()
        
        cmd = goal.goal
        
        if cmd == "TAKEOFF":
            i=0
            while not i == 5:
                self._pub_takeoff.publish(self._takeoff_msg)
                rospy.loginfo('Taking off...')
                time.sleep(1)
                i += 1
        if cmd == "LAND":
            i=0
            while not i == 5:
                self._pub_land.publish(self._land_msg)
                rospy.loginfo('Landing...')
                time.sleep(1)
                i += 1

            # check that preempt (cancelation) has not been requested by the action client
        if self._as.is_preempt_requested():
            rospy.loginfo('The goal has been cancelled/preempted')
            # the following line, sets the client in preempted state (goal cancelled)
            self._as.set_preempted()
            success = False
        
        # builds the next feedback msg to be sent
        self._feedback.feedback = cmd
        # publish the feedback
        self._as.publish_feedback(self._feedback)
        r.sleep()
        # self._as.set_succeeded(self._result)
        if success:
            self._result = Empty()
            self._as.set_succeeded(self._result)
        

if __name__ == '__main__':
    rospy.init_node('move_drone')
    MoveClass()
    rospy.spin()
