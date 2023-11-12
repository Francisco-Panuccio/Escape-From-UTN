import pygame
from constants import *

#Ìconos
""" Logo Principal """
icon = pygame.image.load("icons/logo.png")
pygame.display.set_icon(icon)

""" Volumen """
full_volume = pygame.image.load("icons/full_volume.svg")
full_volume = pygame.transform.scale(full_volume, (scale_volume_x_y, scale_volume_x_y))
void_volume = pygame.image.load("icons/void_volume.svg")
void_volume = pygame.transform.scale(void_volume, (scale_volume_x_y, scale_volume_x_y))