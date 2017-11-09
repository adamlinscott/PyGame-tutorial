# Import the modules
import sys
import random
import pygame
from pygame.locals import *

#open game window
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))


#load player
player = pygame.image.load("resources/images/dude.png")


#Game loop
while True:
	#draw image on screen
	screen.blit(player, (100,100))
	#update window
	pygame.display.flip()
	
	
	#check for intent to close game
	for event in pygame.event.get():
		# check if the event is the X button 
		if event.type==pygame.QUIT:
			# if it is quit the game
			pygame.quit() 
			exit(0) 