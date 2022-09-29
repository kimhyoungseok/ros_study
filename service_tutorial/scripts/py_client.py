#!/usr/bin/python
# -*- coding: utf-8 -*-
from re import A
from unittest import result
import rospy
from service_tutorial.srv import AddTwoInts
import sys

def add_two_ints_client(a, b):
    rospy.wait_for_service("add_two.ints")
    try:
        my_client = rospy.ServiceProxy("add_two.ints", AddTwoInts)
        res = my_client(a, b)
        return res.result
    except rospy.ServiceException as e:
        rospy.logerr("service call failed: %s", e)

if __name__=="__main__":
    rospy.init_node("py_client")

    if len(sys.argv) !=3
        rospy.loginfo("rosrun service_tutorial py_client.py a b")
        rospy.loginfo("a, b: int32 number")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    result = add_two_ints_client(a, b)
    rospy.loginfo("send: a=%d, b=%d", a, b)
    rospy.loginfo("response: result=%d", result)

