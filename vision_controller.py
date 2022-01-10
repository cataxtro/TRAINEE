#!/usr/bin/env python3
#coding=utf-8

import rospy
import cv2
import numpy as np
from controller import Robot
from sensor_msgs.msg import Image as visionSimImage
from std_msgs.msg import String
from cv_bridge import CvBridge

class ControllerVision(object):
    ###########################FUNÇÕES DO CÓDIGO###########################

    #Construtor, recebe o objeto da robô gerado no controlador central e define as variáveis necessárias para o funcionamento do código
	def __init__(self, robot):
        #Inicialização das mensagens e tópicos do ROS
		self.image_msg = visionSimImage()

		self.pubImage = rospy.Publisher('/webots_natasha/vision_controller', String, queue_size= 33)

        #Definição dos valores estáticos necessários para decodificação da mensagem da Imagem pelo código da visão
		self.image_msg.encoding = 'bgra8'
		[self.image_msg.height, self.image_msg.width] = [416,416]
		self.image_msg.step = 1664

		#Inicialização da "Constantes" da biblioteca do Webots
		self.natasha = robot

		#Definição e ativação da camera
		self.camera_sensor = self.natasha.getDevice('Camera')
		self.camera_sensor.enable(33)
		

    #Define o loop do código
	def loop(self):
		self.sensorImage()
    
    ###########################FUNÇÕES DO WEBOTS###########################
    #Função que captura e envia a imagem da camera
	def sensorImage(self):
		self.image_msg.data = self.camera_sensor.getImage()
		
		

		bridge = CvBridge()
		
		img = bridge.imgmsg_to_cv2(self.image_msg,desired_encoding='bgr8')


		imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

		#bola
		lower_ball = np.array([0, 100, 0])
		upper_ball = np.array([6, 255, 255])
		mask_ball = cv2.inRange(imgHSV, lower_ball, upper_ball)



		indices_ball = np.where(mask_ball> [0]) # procurando coordenadas na mascara e colocando em indices
     
		x,y = np.mean(indices_ball, axis=1)

		x_sit = "fora"
		y_sit = "fora"
    
		if y <= 416 and y > 260:
			y_sit = "direita"
		elif y < 156 and y >= 0:
			y_sit = "esquerda"
		elif y >= 156 and y <=260:
			y_sit = "centro"
	    
		if x <= 416 and x > 260:
			x_sit = "embaixo"
		elif x < 160 and x >= 0:
			x_sit = "encima"
		elif x >= 160 and x <= 260:
			x_sit = "centro"
			
		self.pubImage.publish(x_sit + " e " + y_sit)
