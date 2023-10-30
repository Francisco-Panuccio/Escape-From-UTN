import pygame
from constants import *
from functions import *

pygame.init()
screen = pygame.display.set_mode((screen_x, screen_y))
running = True

#Variables
volume = True #Implica Jugar con Volumen
language = False #Implica Jugar en Español
score = 0 #Puntaje Inicial
screamer = {"value": False} #Implica que no se Activó el Screamer del Logo
player = {"name": ""} #Nombre del Jugador
play = {"value": "Main"} #Implica Estar en la Pantalla Inicial

#Título e Ícono
pygame.display.set_caption("Escape From UTN")
icon = pygame.image.load("icons/logo.png")
pygame.display.set_icon(icon)
full_volume = pygame.image.load("icons/full_volume.svg")
full_volume = pygame.transform.scale(full_volume, (scale_volume_x_y, scale_volume_x_y))
void_volume = pygame.image.load("icons/void_volume.svg")
void_volume = pygame.transform.scale(void_volume, (scale_volume_x_y, scale_volume_x_y))

#Fuentes de Texto
font_text = pygame.font.SysFont("Times New Roman", 30)

#Textos

#Música General
pygame.mixer.init()
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.load("sounds/background.mp3")
pygame.mixer.music.play(-1)

#Sonidos
thunder = pygame.mixer.Sound("sounds/thunder.mp3")
thunder.set_volume(0.2)
screamer_logo_sound = pygame.mixer.Sound("sounds/scream_monster_three.mp3")
screamer_logo_sound.set_volume(0.7)
bullying = pygame.mixer.Sound("sounds/beginning.mp3")
bullying.set_volume(0.3)
interference = pygame.mixer.Sound("sounds/interference.mp3")
interference.set_volume(0.4)

#Imágenes/Fondos
""" Advertencia Español """
warning_spa = pygame.image.load("images/warning_s.png")
warning_spa = pygame.transform.scale(warning_spa, (screen_x, screen_y))
""" Advertencia Inglés """
warning_eng = pygame.image.load("images/warning_e.png")
warning_eng = pygame.transform.scale(warning_eng, (screen_x, screen_y))
""" Escuela Roja, Pantalla de Título Español """
background_main_spa = pygame.image.load("images/school_s.png")
background_main_spa = pygame.transform.scale(background_main_spa, (screen_x, screen_y))
""" Escuela Roja, Pantalla de Título Inglés """
background_main_eng = pygame.image.load("images/school_e.png")
background_main_eng = pygame.transform.scale(background_main_eng, (screen_x, screen_y))
""" Escuela Iluminada por Relámpago, Pantalla de Título Español """
background_main_ligth_spa = pygame.image.load("images/school_light_s.png")
background_main_ligth_spa = pygame.transform.scale(background_main_ligth_spa, (screen_x, screen_y))
""" Escuela Iluminada por Relámpago, Pantalla de Título Inglés """
background_main_ligth_eng = pygame.image.load("images/school_light_e.png")
background_main_ligth_eng = pygame.transform.scale(background_main_ligth_eng, (screen_x, screen_y))
""" Screamer Logo """
screamer_logo = pygame.image.load("images/monster_three.png")
screamer_logo = pygame.transform.scale(screamer_logo, (screen_x, screen_y))
""" Nombre de Usuario Español """
player_input_spa = pygame.image.load("images/player_input_spa.png")
player_input_spa = pygame.transform.scale(player_input_spa, (screen_x, screen_y))
""" Nombre de Usuario Inglés """
player_input_eng = pygame.image.load("images/player_input_eng.png")
player_input_eng = pygame.transform.scale(player_input_eng, (screen_x, screen_y))
""" Escuela Roja """
school_background = pygame.image.load("images/school.png")
school_background = pygame.transform.scale(school_background, (screen_x, screen_y))
""" Escuela Real """
real_school = pygame.image.load("images/real_school.png")
real_school = pygame.transform.scale(real_school, (screen_x, screen_y))
""" Nivel 1 """
level_one_background = pygame.image.load("images/level_one_background.png")
level_one_background = pygame.transform.scale(level_one_background, (screen_x, screen_y))

#Rectángulos
""" Volumen """
volume_rect = full_volume.get_rect()
volume_rect.x = volume_x
volume_rect.y = volume_y
""" Idioma """
language_rect = pygame.Rect((language_x, language_y), (language_width, language_height))
language_rect.x = language_x
language_rect.y = language_y
""" Puntaje """
score_rect = pygame.Rect((score_x, score_y), (score_width, score_height))
score_rect_x = score_x
score_rect_y = score_y
""" Logo (Misterio) """
logo_rect = pygame.Rect((logo_x, logo_y), (logo_width, logo_height))
logo_rect_x = logo_x
logo_rect_y = logo_y
""" Jugar """
play_rect = pygame.Rect((play_x, play_y), (play_width, play_height))
play_rect_x = play_x
play_rect_y = play_y
""" Flecha para Continuar """
arrow_rect = pygame.Rect((arrow_x, arrow_y), (arrow_width, arrow_height))
arrow_rec_x = arrow_x
arrow_rec_y = arrow_y

#Timer
clock = {"value": 0}
clock_two = {"value": 0} #Segundo Contador de Tiempo para Evitar Delay en Sonidos
second_timer = pygame.USEREVENT + 0
pygame.time.set_timer(second_timer, 1000)
frames_clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        #Eventos de Tiempo (cada 1 segundo)
        if (event.type == pygame.USEREVENT):
            if (event.type == second_timer):
                clock["value"] += 1
                clock_two["value"] += 2

        if (event.type == pygame.MOUSEBUTTONDOWN):
            position_click = list(event.pos)
            print(position_click)

            #Controlar Volumen
            if (volume_rect.collidepoint(event.pos)):
                if (volume):
                    volume = False
                    pygame.mixer.music.set_volume(0)
                    thunder.set_volume(0)
                    screamer_logo_sound.set_volume(0)
                    bullying.set_volume(0)
                    interference.set_volume(0)
                else:
                    volume = True
                    pygame.mixer.music.set_volume(0.4)
                    thunder.set_volume(0.2)
                    screamer_logo_sound.set_volume(0.7)
                    bullying.set_volume(0.3)
                    interference.set_volume(0.4)

            #Pantalla de Inicio
            if (play["value"] == "Main"):            
                #Controlar Idioma
                if (language_rect.collidepoint(event.pos)):
                    if (not language):
                        language = True
                    else:
                        language = False

                #Acceder al Puntaje Global
                if (score_rect.collidepoint(event.pos)):
                    print("Score")

                #Misterio al Apretar el Logo
                if (logo_rect.collidepoint(event.pos)):
                    screamer_logo_sound.play()
                    screamer["value"] = True
                    clock_two["value"] = 0

                #Comenzar a Jugar
                if (play_rect.collidepoint(event.pos)):
                    play["value"] = "Player"

            #Seleccionar Nombre de Jugador
            elif (play["value"] == "Player"):
                if (arrow_rect.collidepoint(event.pos)):
                    #Animación de Inicio
                    play["value"] = "Animation"
                    clock["value"] = 0
                    bullying.play()

            elif (play["value"] == "Level_One"):
                pass

        #Quitar el Juego
        if (event.type == pygame.QUIT):
            running = False

    #Renderizaciones
    if (language == False):
        if (play["value"] == "Main"):
            run_background(clock, clock_two, screen, warning_spa, background_main_spa, background_main_ligth_spa, thunder)
            if (screamer["value"] == True):
                run_mystery_logo(screen, screamer_logo, screamer, clock_two) 
        elif (play["value"] == "Player"):
            run_player_input(screen, player_input_spa, font_text, player, frames_clock)
        elif (play["value"] == "Animation"):
            run_startup_animation(clock, screen, school_background, real_school, interference, play)
        elif (play["value"] == "Level_One"):
            run_level_one(screen, level_one_background)       
    else:
        if (play["value"] == "Main"):
            run_background(clock, clock_two, screen, warning_eng, background_main_eng, background_main_ligth_eng, thunder)
            if (screamer["value"] == True):
                run_mystery_logo(screen, screamer_logo, screamer, clock_two)
        elif (play["value"] == "Player"):
            run_player_input(screen, player_input_eng, font_text, player, frames_clock)
        elif (play["value"] == "Animation"):
            run_startup_animation(clock, screen, school_background, real_school, interference, play)  
        elif (play["value"] == "Level_One"):
            run_level_one(screen, level_one_background)
    control_volume(screen, full_volume, void_volume, volume)
    pygame.display.flip()

""" PROBLEMAS """
#NO SE CÓMO PONER EL INPUT PARA INSERTAR UN NOMBRE DE USUARIO Y QUE SE ACTUALICE EN LA CLASE.