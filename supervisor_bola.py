#!/usr/bin/env python3
#coding=utf-8


import rospy
from controller import Supervisor
from geometry_msgs.msg import Vector3
import sys

TIME_STEP = 32

supervisor = Supervisor()

pub = rospy.Publisher('/webots_natasha/Translation', Vector3, queue_size=50)
rospy.init_node('supervisor_bola', anonymous=True)
# do this once only
ball_node = supervisor.getFromDef("bola")

trans_field = ball_node.getField("translation")
rate = rospy.Rate(10)
values = Vector3()

while supervisor.step(TIME_STEP) != -1:

    # this is done repeatedly
    [values.x, values.y, values.z] = trans_field.getSFVec3f()
    ball_node.addForce([0.09,0,0],False)
    pub.publish(values)
    rate.sleep()

