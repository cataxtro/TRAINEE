#!/usr/bin/env python3
#coding=utf-8

import robo_estados
import rospy

class Cerebro():
    def __init__(self):
        self.robot = robo_estados.Goleiro()
        if self.robot.state == 'Parado' or self.robot.state == 'Defesa':
            print(self.robot.state)

if __name__ == '__main__':
    brain = Cerebro() # Inicia o construtor da classe
    brain.start() # Roda o método start
    rospy.spin()