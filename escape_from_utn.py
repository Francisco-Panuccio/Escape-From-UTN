import pygame
from variables import *
from constants import *
from images import *
from sounds import *
from rects import *
from class_player import *
from functions.volume_function import *
from functions.main_function import *
from functions.level_one_functions import *
from functions.level_two_functions import *
from functions.level_three_functions import *

pygame.init()
screen = pygame.display.set_mode((screen_x, screen_y))

#Título e Ícono
pygame.display.set_caption("Escape From UTN")

#Fuentes de Texto
font_text = pygame.font.SysFont("Arial Black", 40)
font_text_score = pygame.font.SysFont("Arial Black", 20)

#Timer
second_timer = pygame.USEREVENT + 0
pygame.time.set_timer(second_timer, 1000)
frames_clock = pygame.time.Clock()

#Cargar Configuración del Idioma Guardada
language_config = Player.load_player_config("Config.json")
if (language_config == False or language_config == None):
    language = False
else:
    if (language_config["Config"][0]["Language"] == True):
        language = True
    else:
        language = False

while (running["value"] == True):
    for event in pygame.event.get():
        #Eventos de Tiempo (cada 1 segundo)
        if (event.type == pygame.USEREVENT):
            if (event.type == second_timer):
                clock["value"] += 1
                clock_two["value"] += 2
                if (play["value"] == "Level_Three" and timer_condition["value"] == True):
                    final_timer["value"] -= 1

        #Guardar el Nombre de Jugador
        if (play["value"] == "Player"):
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_BACKSPACE):
                    #Borrar
                    player["name"] = player["name"][:-1]
                elif (event.key == pygame.K_RETURN):
                    if (player["name"] == ""):
                        player["name"] = "Lucifer"
                    #Animación de Inicio
                    play["value"] = "Animation"
                    clock["value"] = 0
                    bullying.play()
                elif (event.key == pygame.K_ESCAPE):
                    #Volver al Inicio
                    play["value"] = "Main"
                else:
                    if (len(player["name"]) >= 13):
                        player["name"] = "Belfegor"
                    else:
                        player["name"] += event.unicode

        #Código de Puerta Nivel 2
        if (play["value"] == "Level_Two"):
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_BACKSPACE):
                    code_door["value"] = code_door["value"][:-1]
                elif (event.key == pygame.K_RETURN):
                    if (code_door["value"] == "1207"):
                         correct_code.play()
                         clock_two["value"] = 0
                         codelock_condition["value"] = True
                    else:
                        wrong_code.play()
                else:
                    if (len(code_door["value"]) >= 4):
                        code_door["value"] = "616"
                    else:
                        code_door["value"] += event.unicode

        #Final Malo Nivel 3
        if (timer_condition["value"] == True and final_timer["value"] == 1):
            clock_two["value"] = 0
       
        #Eventos al Presionar el Click del Mouse
        if (event.type == pygame.MOUSEBUTTONDOWN):
            position_click = list(event.pos)

            #Controlar Volumen
            if (volume_rect.collidepoint(event.pos)):
                if (volume):
                    volume = False
                else:
                    volume = True

            #Pantalla de Inicio
            if (play["value"] == "Main"):     
                if (rect_controller["value"] == False):       
                    #Controlar Idioma
                    if (language_rect.collidepoint(event.pos)):
                        if (not language):
                            language = True
                        else:
                            language = False
                        #Guardar Configuración del Idioma
                        Player.save_player_config("Config.json", language)

                    #Acceder al Puntaje Global
                    if (score_rect.collidepoint(event.pos)):
                        #Cargar Data del Jugador
                        play["value"] = "Score"
                        player_data = (Player.load_player_data("Global_Score.json"))

                    #Misterio al Apretar el Logo
                    if (logo_rect.collidepoint(event.pos)):
                        scream_logo_sound.play()
                        screamer["value"] = True
                        clock_two["value"] = 0

                    #Comenzar a Jugar
                    if (play_rect.collidepoint(event.pos)):
                        whispers_start.play()
                        play["value"] = "Player"

            #Seleccionar Nombre de Jugador
            elif (play["value"] == "Player"):
                if (arrow_rect.collidepoint(event.pos)):
                    if (player["name"] == ""):
                        player["name"] = "Lucifer"
                    #Animación de Inicio
                    play["value"] = "Animation"
                    clock["value"] = 0
                    bullying.play()
            
            #Puntaje Global
            elif (play["value"] == "Score"):
                if (return_main_score_rect.collidepoint(event.pos)):
                    #Volver al Menú Principal al acceder al Puntaje Global 
                    play["value"] = "Main"

            #Nivel Uno
            elif (play["value"] == "Level_One"):
                if (rect_controller["value"] == False):
                    click_level_one(event)

            #Nivel Dos
            elif (play["value"] == "Level_Two"):
                if (rect_controller["value"] == False):
                    click_level_two(event)

            #Nivel Tres
            elif (play["value"] == "Level_Three"):
                if (rect_controller["value"] == False):
                    click_level_three(event)

        #Quitar el Juego
        if (event.type == pygame.QUIT):
            running["value"] = False

    #Renderizaciones
    if (language == False):
        if (play["value"] == "Main"):
            run_background(screen, warning_spa, background_main_spa, background_main_ligth_spa)
        elif (play["value"] == "Score"):
            run_global_score(screen, global_score_spa, player_data, font_text_score)
        elif (play["value"] == "Player"):
            run_player_input(screen, player_input_spa, font_text, frames_clock)
        elif (play["value"] == "Animation"):
            run_startup_animation(screen)
        elif (play["value"] == "Level_One"):
            run_level_one(screen, font_text, level_one_text_spa, loading_screen_one_spa)
        elif (play["value"] == "Level_Two"):
            run_level_two(screen, loading_screen_two_spa, font_text, frames_clock, level_two_text_spa, board_spa, chair_spa, window_spa) 
        elif (play["value"] == "Level_Three"):
            run_level_three(screen, font_text, loading_screen_three_spa, level_three_background_two_spa, blur_spa, blur_two_spa, good_ending_spa) 
        if (screamer["value"] == True):
            run_mystery_logo(screen) 
    else:
        if (play["value"] == "Main"):
            run_background(screen, warning_eng, background_main_eng, background_main_ligth_eng)
        elif (play["value"] == "Score"):
            run_global_score(screen, global_score_eng, player_data, font_text_score)
        elif (play["value"] == "Player"):
            run_player_input(screen, player_input_eng, font_text, frames_clock)
        elif (play["value"] == "Animation"):
            run_startup_animation(screen)  
        elif (play["value"] == "Level_One"):
            run_level_one(screen, font_text, level_one_text_eng, loading_screen_one_eng)
        elif (play["value"] == "Level_Two"):
            run_level_two(screen, loading_screen_two_eng, font_text, frames_clock, level_two_text_eng, board_eng, chair_eng, window_eng) 
        elif (play["value"] == "Level_Three"):
            run_level_three(screen, font_text, loading_screen_three_eng, level_three_background_two_eng, blur_eng, blur_two_eng, good_ending_eng) 
        if (screamer["value"] == True):
            run_mystery_logo(screen) 
    control_volume(screen, volume)
    pygame.display.flip()