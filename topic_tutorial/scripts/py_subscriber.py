#!/usr/bin/python
#! -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def msgcallback(msg):
    rospy.loginfo("msg : %s", msg.data)

def listener():
    rospy.init_node("py_subscriber")
    rospy.Subscriber("my_topic", String, msgcallback, queue_size= 100)

    rospy.spin()

if __name__== "__main__":
    listener()

    