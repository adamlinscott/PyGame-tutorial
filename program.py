# Import the modules
import sys
import random
import pygame
from pygame.locals import *

#open game window
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))


while True:
    question = raw_input("Ask the magic 8 ball a question: (press enter to quit) ")
    
    answers = random.randint(1,4)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print "It is certain"
    
    elif answers == 2:
        print "Outlook good"
    
    elif answers == 3:
        print "You may rely on it"
    
    elif answers == 4:
        print "Ask again later"