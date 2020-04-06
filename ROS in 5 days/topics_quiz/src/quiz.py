#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import LaserScan

pub = None


def callback(msg):       
    pub_msg = Twist()   
    if float(msg.ranges[360]) > 1:
        pub_msg.linear.x = 0.3
        pub_msg.angular.z = 0 
    if float(msg.ranges[360]) < 1:
        pub_msg.linear.x = 0
        pub_msg.angular.z = 0.3
    if float(msg.ranges[0]) < 1:
        pub_msg.linear.x = 0
        pub_msg.angular.z = 0.3
    if float(msg.ranges[719]) < 1:
        pub_msg.linear.x = 0
        pub_msg.angular.z = -0.3
    pub.publish(pub_msg)  

# if __name__ == '__main__':
rospy.init_node('topics_quiz_node')

sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rospy.spin()   
rate = rospy.Rate(2)
rate.sleep()
    
