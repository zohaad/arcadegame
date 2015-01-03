import pygame
from pygame.locals import *
	
def button_a():
	return pygame.key.get_pressed()[K_a] != 0