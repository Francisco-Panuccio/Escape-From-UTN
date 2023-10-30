import pygame
from constants import *
from class_player import *

#Controlar el Volumen
def control_volume(screen, volume_f, volume_v, volume):
    if (volume):
        pygame.draw.rect(screen, (black), volume_f.get_rect())
        screen.blit(volume_f, (volume_x, volume_y), volume_f.get_rect())
    else:
        pygame.draw.rect(screen, (black), volume_v.get_rect())
        screen.blit(volume_v, (volume_x, volume_y), volume_v.get_rect())

#Correr Pantalla de Inicio
def run_background(clock, clock_two, screen, warning, background, background_light, thunder):
    screen.blit(warning, (0,0))
    if (clock["value"] > 6):
        screen.blit(background, (0,0))
        if (clock["value"] >= 10 and clock_two["value"] == 20):
            screen.blit(background_light, (0,0))
            thunder.play()
            clock_two["value"] = 0

#Correr Screamer de Logo
def run_mystery_logo(screen, screamer_logo, screamer, clock_two):
    screen.blit(screamer_logo, (0,0))
    if (clock_two["value"] > 8):
        screamer["value"] = False

#Correr Selección de Jugador
def run_player_input(screen, background, font_text, player, frames_clock):
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_BACKSPACE):
                player["name"] = player["name"][:-1]
            else:
                player["name"] += event.unicode
    screen.blit(background, (0,0))
    player_text = font_text.render(player["name"], True, (white))
    screen.blit(player_text, (player_input_x, player_input_y))
    frames_clock.tick(60)

#Correr Animación de Inicio
def run_startup_animation(clock, screen, school, real_school, interference, play):
    screen.blit(school, (0,0))
    if (clock["value"] > 10 and clock["value"] < 12):
        interference.play()
        screen.blit(real_school, (0,0))
    if (clock["value"] == 19):
        play["value"] = "Level_One"

#Correr Nivel 1
def run_level_one(screen, level_one_background):
    screen.blit(level_one_background, (0,0))