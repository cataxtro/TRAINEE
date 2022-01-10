#!/usr/bin/env python3
#coding=utf-8

import rospy
from std_msgs.msg import String

def callback(data):
    data = str(data)
    data1 = list(data.split(" "))
    
    if '"centro' in data1 and 'esquerda"' in data1:
    	print ("Bola perto, andar esquerda e defender")
    elif '"centro'  in data1 and 'centro"' in data1:
    	print ("Bola perto, defender")
    elif '"centro'  in data1 and 'direita"' in data1:
    	print ("Bola perto, andar direita e defender")
    else:
    	print ("Bola longe")


def listener():
    	
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('receiver_vision', anonymous=True)

    rospy.Subscriber('/webots_natasha/vision_controller', String, callback)

    
    

    rospy.spin()

if __name__ == '__main__':

    listener()
