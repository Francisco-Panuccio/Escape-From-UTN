from constants import *
from rects import *
from images import *
from variables import *
from sounds import *
from functions.format_function import *

#Correr Pantalla de Inicio
def run_background(screen, warning, background, background_light):
    screen.blit(warning, (0,0))
    if (clock["value"] > 4):
        screen.blit(background, (0,0))
        rect_controller["value"] = False
        if (clock["value"] >= 10 and clock_two["value"] == 20):
            screen.blit(background_light, (0,0))
        if (clock["value"] >= 10 and clock_two["value"] == 22):
            thunder.play()
            clock_two["value"] = 0

#Correr Screamer de Logo
def run_mystery_logo(screen):
    play["value"] = ""
    screen.blit(screamer_logo, (0,0))
    if (clock_two["value"] > 5):
        screamer["value"] = False
        play["value"] = "Main"

#Correr Puntaje Global
def run_global_score(screen, global_s, player_data, font_text):
    if ((player_data == False) or (player_data == None)):
        screen.blit(global_s, (0,0))
    else:  
        player_dict = str(player_data["Players"])
        player_data = format_function(player_dict)
        split_data = player_data.split("\n")
        screen.blit(global_s, (0,0))
        pygame.draw.rect(screen, (violet), global_score_border_rect, 0, 15)
        pygame.draw.rect(screen, (black), global_score_rect, 0, 15)
        for i, ll in enumerate(split_data):
            global_score_text = font_text.render(ll, True, (white))
            screen.blit(global_score_text, (global_score_text_x, global_score_text_y + (i*50)))
        
#Correr Selección de Jugador
def run_player_input(screen, background, font_text, frames_clock):
    player_text = font_text.render(player["name"], True, (white))
    screen.blit(background, (0,0))
    screen.blit(player_text, (player_input_x, player_input_y))
    frames_clock.tick(60)

#Correr Animación de Inicio
def run_startup_animation(screen):
    rect_controller["value"] = True
    if (clock["value"] < 7):
        screen.blit(animation, (0,0))
    elif (clock["value"] >= 7 and clock["value"] < 9):
        screen.blit(animation_two, (0,0))
    else:
        screen.blit(school_background, (0,0))
    if (clock["value"] == 11):
        interference.play()
        screen.blit(real_school, (0,0))
    if (clock["value"] >= 12 and clock["value"] < 18):
        screen.blit(school_background_blur, (0,0))
    if (clock["value"] == 18):
        interference.play()
        screen.blit(real_locker, (0,0))
    if (clock["value"] == 19):
        play["value"] = "Level_One"
        scream_echo.play()
        clock_two["value"] = 0