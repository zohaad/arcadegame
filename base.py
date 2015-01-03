# -*- coding: cp1252 -*-
# SuperPac
# Autor: Felipe Araújo de Andrade
# data: 15/08/2012

from helpers import *



import pygame
if module_exists('RPi.GPIO'):
	from gpio import *
else:
	from keyboard import *

from pygame.locals import *
from random import *
from sys import exit as sair

pygame.init()
pygame.mixer.pre_init()
pygame.mixer.init()

screen = pygame.display.set_mode((600, 600))

#pygame.mouse.set_visible(0)

#icone = pygame.image.load("images/icon.png")

pygame.display.set_caption("ArcadePi")

#pygame.display.set_icon(icone)

clock = pygame.time.Clock()

level1 = {
	'background': pygame.image.load('level1/base.png')
}

screen.blit(level1['background'],(0,0))

def main():
    while True:

    	event = pygame.event.wait()
    	if event.type == QUIT:
        	exit()

    	if button_a():
    		dfsfsffsdf()

        pygame.display.update()

main()

