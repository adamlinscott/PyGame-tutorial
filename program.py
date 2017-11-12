# Import the modules
import sys
import random
import pygame
import time
import math
from pygame.locals import *

#Variables
width, height = 640, 480
keys = [False, False, False, False]
playerpos=[100,100]

#open game window
pygame.init()
screen = pygame.display.set_mode((width, height))


#load player
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")


#function to get the time between each frame
lastFrameTime = int(round(time.time() * 1000))
def FrameDeltaTime():
	global lastFrameTime
	delta = int(round(time.time() * 1000)) - lastFrameTime
	lastFrameTime = int(round(time.time() * 1000))
	return delta


#Game loop
while True:
	#clear screen
	screen.fill(0)	
	
	#draw image on screen
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_height()+1):
			screen.blit(grass,(x*100,y*100))

	#rotate image to face mouse
	mPosition = pygame.mouse.get_pos()
	angle = math.atan2(mPosition[1]-(playerpos[1]),mPosition[0]-(playerpos[0]))
	playerrot = pygame.transform.rotate(player, 360-angle*57.29)
	playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
	screen.blit(playerrot, playerpos1) 
	
	#update window
	pygame.display.flip()
	
	#update deltatime
	deltaTime = FrameDeltaTime()
	
	#check for intent to close game
	for event in pygame.event.get():
		# check if the event is the X button 
		if event.type==pygame.QUIT:
			# if it is quit the game
			pygame.quit() 
			exit(0) 
			
		#check for key events
		if event.type == pygame.KEYDOWN:
			if event.key==K_w:
				keys[0]=True
			elif event.key==K_a:
				keys[1]=True
			elif event.key==K_s:
				keys[2]=True
			elif event.key==K_d:
				keys[3]=True
		if event.type == pygame.KEYUP:
			if event.key==pygame.K_w:
				keys[0]=False
			elif event.key==pygame.K_a:
				keys[1]=False
			elif event.key==pygame.K_s:
				keys[2]=False
			elif event.key==pygame.K_d:
				keys[3]=False
				
	#move player
	if keys[0]:
		playerpos[1]-=1 * deltaTime
	elif keys[2]:
		playerpos[1]+=1 * deltaTime
	if keys[1]:
		playerpos[0]-=1 * deltaTime
	elif keys[3]:
		playerpos[0]+=1 * deltaTime

			