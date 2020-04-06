#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest, BB8CustomServiceMessageResponse  # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist
import time

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_square_custom has been called")
    print "Request Data==> side="+str(request.side)
    print "Request Data==> repetitions ="+str(request.repetitions)
    my_response = BB8CustomServiceMessageResponse()
    i=0
    while i < request.repetitions:
        ii = 0
        while ii < 4:
            stime = 2.0
            move.linear.x = 0.2
            move.angular.z = 0
            my_pub.publish(move)
            time.sleep(request.side)

            move.linear.x = 0.0
            move.angular.z = 0.0
            my_pub.publish(move)
            time.sleep(3)
            
            move.linear.x = 0.0
            move.angular.z = 0.2 
            my_pub.publish(move)
            time.sleep(3.7)

            move.linear.x = 0.0
            move.angular.z = 0.0
            my_pub.publish(move)
            time.sleep(0.1)            
            ii+=1
        i+=1
    my_response.success = True
    move.linear.x = 0.0
    move.angular.z = 0.0
    rospy.loginfo("Finished service move_bb8_in_square_custom")
    return my_response # the service Response class, in this case EmptyResponse

rospy.init_node('service_move_bb8_in_square_server') 
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , my_callback) 
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move = Twist()
rate = rospy.Rate(1)
rospy.loginfo("Service /move_bb8_in_square_custom Ready")
rospy.spin() # mantain the service open.
