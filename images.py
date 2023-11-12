import pygame
from constants import *

#Imágenes/Fondos
""" Advertencia Español """
warning_spa = pygame.image.load("images/main/warning_s.png")
warning_spa = pygame.transform.scale(warning_spa, (screen_x, screen_y))
""" Advertencia Inglés """
warning_eng = pygame.image.load("images/main/warning_e.png")
warning_eng = pygame.transform.scale(warning_eng, (screen_x, screen_y))
""" Escuela Roja, Pantalla de Título Español """
background_main_spa = pygame.image.load("images/main/school_s.png")
background_main_spa = pygame.transform.scale(background_main_spa, (screen_x, screen_y))
""" Escuela Roja, Pantalla de Título Inglés """
background_main_eng = pygame.image.load("images/main/school_e.png")
background_main_eng = pygame.transform.scale(background_main_eng, (screen_x, screen_y))
""" Escuela Iluminada por Relámpago, Pantalla de Título Español """
background_main_ligth_spa = pygame.image.load("images/main/school_light_s.png")
background_main_ligth_spa = pygame.transform.scale(background_main_ligth_spa, (screen_x, screen_y))
""" Escuela Iluminada por Relámpago, Pantalla de Título Inglés """
background_main_ligth_eng = pygame.image.load("images/main/school_light_e.png")
background_main_ligth_eng = pygame.transform.scale(background_main_ligth_eng, (screen_x, screen_y))
""" Screamer Logo """
screamer_logo = pygame.image.load("images/main/scream_logo.png")
screamer_logo = pygame.transform.scale(screamer_logo, (screen_x, screen_y))
""" Puntaje Global Español """
global_score_spa = pygame.image.load("images/main/global_score_spa.png")
global_score_spa = pygame.transform.scale(global_score_spa, (screen_x, screen_y))
""" Puntaje Global Inglés """
global_score_eng = pygame.image.load("images/main/global_score_eng.png")
global_score_eng = pygame.transform.scale(global_score_eng, (screen_x, screen_y))
""" Nombre de Usuario Español """
player_input_spa = pygame.image.load("images/main/player_input_spa.png")
player_input_spa = pygame.transform.scale(player_input_spa, (screen_x, screen_y))
""" Nombre de Usuario Inglés """
player_input_eng = pygame.image.load("images/main/player_input_eng.png")
player_input_eng = pygame.transform.scale(player_input_eng, (screen_x, screen_y))
""" Animación de Inicio (Uno, Encierro) """
animation = pygame.image.load("images/main/animation.png")
animation = pygame.transform.scale(animation, (screen_x, screen_y))
""" Animación de Inicio (Dos, Motos) """
animation_two = pygame.image.load("images/main/animation_two.png")
animation_two = pygame.transform.scale(animation_two, (screen_x, screen_y))
""" Escuela Roja """
school_background = pygame.image.load("images/main/school.png")
school_background = pygame.transform.scale(school_background, (screen_x, screen_y))
""" Escuela Roja con Desenfoque """
school_background_blur = pygame.image.load("images/main/school_blur.png")
school_background_blur = pygame.transform.scale(school_background_blur, (screen_x, screen_y))
""" Escuela Real """
real_school = pygame.image.load("images/main/real_school.png")
real_school = pygame.transform.scale(real_school, (screen_x, screen_y))


""" Nivel 1 (Pantalla de Carga Español) """
loading_screen_one_spa = pygame.image.load("images/level_one/level_one_spa.png")
loading_screen_one_spa = pygame.transform.scale(loading_screen_one_spa, (screen_x, screen_y))
""" Nivel 1 (Pantalla de Carga Inglés) """
loading_screen_one_eng = pygame.image.load("images/level_one/level_one_eng.png")
loading_screen_one_eng = pygame.transform.scale(loading_screen_one_eng, (screen_x, screen_y))
""" Nivel 1 (Casillero Real) """
real_locker = pygame.image.load("images/level_one/real_locker.png")
real_locker = pygame.transform.scale(real_locker, (screen_x, screen_y))
""" Nivel 1 (Casillero Rojo) """
level_one_background = pygame.image.load("images/level_one/level_one_background.png")
level_one_background = pygame.transform.scale(level_one_background, (screen_x, screen_y))
""" Nivel 1 (Texto Español) """
level_one_text_spa = pygame.image.load("images/level_one/text_one_spa.png")
level_one_text_spa = pygame.transform.scale(level_one_text_spa, (text_width, text_height))
""" Nivel 1 (Texto Inglés) """
level_one_text_eng = pygame.image.load("images/level_one/text_one_eng.png")
level_one_text_eng = pygame.transform.scale(level_one_text_eng, (text_width, text_height))
""" Nivel 1 (Visión Fantasmal) """
ghostly_eye = pygame.image.load("images/level_one/eye.png")
ghostly_eye = pygame.transform.scale(ghostly_eye, (eye_width, eye_height))
""" Nivel 1 (Martillo y Destornillador) """
hammer_screwdriver = pygame.image.load("images/level_one/hammer_screw.png")
hammer_screwdriver = pygame.transform.scale(hammer_screwdriver, (crate_width, crate_height))
""" Nivel 1 (Screamer de Monstruo) """
screamer_monster_one = pygame.image.load("images/level_one/monster_one.png")
screamer_monster_one = pygame.transform.scale(screamer_monster_one, (screen_x, screen_y))


""" Nivel 2 (Pantalla de Carga Español) """
loading_screen_two_spa = pygame.image.load("images/level_two/level_two_spa.png")
loading_screen_two_spa = pygame.transform.scale(loading_screen_two_spa, (screen_x, screen_y))
""" Nivel 2 (Pantalla de Carga Inglés) """
loading_screen_two_eng = pygame.image.load("images/level_two/level_two_eng.png")
loading_screen_two_eng = pygame.transform.scale(loading_screen_two_eng, (screen_x, screen_y))
""" Nivel 2 (Texto Español) """
level_two_text_spa = pygame.image.load("images/level_two/text_two_spa.png")
level_two_text_spa = pygame.transform.scale(level_two_text_spa, (text_width, text_height))
""" Nivel 2 (Texto Inglés) """
level_two_text_eng = pygame.image.load("images/level_two/text_two_eng.png")
level_two_text_eng = pygame.transform.scale(level_two_text_eng, (text_width, text_height))
""" Nivel 2 (Aula Real) """
real_classroom = pygame.image.load("images/level_two/real_classroom.png")
real_classroom = pygame.transform.scale(real_classroom, (screen_x, screen_y))
""" Nivel 2 (Aula Iluminada) """
level_two_background_light = pygame.image.load("images/level_two/level_two_background_one.png")
level_two_background_light = pygame.transform.scale(level_two_background_light, (screen_x, screen_y))
""" Nivel 2 (Aula Roja) """
level_two_background = pygame.image.load("images/level_two/level_two_background_two.png")
level_two_background = pygame.transform.scale(level_two_background, (screen_x, screen_y))
""" Nivel 2 (Pizarrón Español) """
board_spa = pygame.image.load("images/level_two/board_spa.png")
board_spa = pygame.transform.scale(board_spa, (level_two_game_width, level_two_game_height))
""" Nivel 2 (Pizarrón Inglés) """
board_eng = pygame.image.load("images/level_two/board_eng.png")
board_eng = pygame.transform.scale(board_eng, (level_two_game_width, level_two_game_height))
""" Nivel 2 (Silla Español) """
chair_spa = pygame.image.load("images/level_two/chair_spa.png")
chair_spa = pygame.transform.scale(chair_spa, (level_two_game_width, level_two_game_height))
""" Nivel 2 (Silla Inglés) """
chair_eng = pygame.image.load("images/level_two/chair_eng.png")
chair_eng = pygame.transform.scale(chair_eng, (level_two_game_width, level_two_game_height))
""" Nivel 2 (Ventana Español) """
window_spa = pygame.image.load("images/level_two/window_spa.png")
window_spa = pygame.transform.scale(window_spa, (level_two_game_width, level_two_game_height))
""" Nivel 2 (Ventana Inglés) """
window_eng = pygame.image.load("images/level_two/window_eng.png")
window_eng = pygame.transform.scale(window_eng, (level_two_game_width, level_two_game_height))
""" Nivel 2 (Libro) """
book_code = pygame.image.load("images/level_two/book_code.png")
book_code = pygame.transform.scale(book_code, (level_two_game_width, level_two_game_height))
""" Nivel 2 (Puerta) """
codelock = pygame.image.load("images/level_two/codelock.png")
codelock = pygame.transform.scale(codelock, (level_two_game_width, level_two_game_height))
""" Nivel 2 (Screamer de Monstruo) """
screamer_monster_two = pygame.image.load("images/level_two/monster_two.png")
screamer_monster_two = pygame.transform.scale(screamer_monster_two, (screen_x, screen_y))


""" Nivel 3 (Pantalla de Carga Español) """
loading_screen_three_spa = pygame.image.load("images/level_three/level_three_spa.png")
loading_screen_three_spa = pygame.transform.scale(loading_screen_three_spa, (screen_x, screen_y))
""" Nivel 3 (Pantalla de Carga Inglés) """
loading_screen_three_eng = pygame.image.load("images/level_three/level_three_eng.png")
loading_screen_three_eng = pygame.transform.scale(loading_screen_three_eng, (screen_x, screen_y))
""" Nivel 3 (Pasillo Real) """
real_hallway = pygame.image.load("images/level_three/real_hallway.png")
real_hallway = pygame.transform.scale(real_hallway, (screen_x, screen_y))
""" Nivel 3 (Pasillo Rojo) """
level_three_background = pygame.image.load("images/level_three/level_three_background.png")
level_three_background = pygame.transform.scale(level_three_background, (screen_x, screen_y))
""" Nivel 3 (Monstruo) """
bad_ending_monster = pygame.image.load("images/level_three/bad_ending_monster.png")
bad_ending_monster = pygame.transform.scale(bad_ending_monster, (screen_x, screen_y))
""" Nivel 3 (Monstruo Dos) """
bad_ending_monster_two = pygame.image.load("images/level_three/bad_ending_monster_two.png")
bad_ending_monster_two = pygame.transform.scale(bad_ending_monster_two, (screen_x, screen_y))
""" Nivel 3 (Monstruo Tres) """
bad_ending_monster_three = pygame.image.load("images/level_three/bad_ending_monster_three.png")
bad_ending_monster_three = pygame.transform.scale(bad_ending_monster_three, (screen_x, screen_y))
""" Nivel 3 (Final Bueno Español) """
good_ending_spa = pygame.image.load("images/level_three/good_ending_spa.png")
good_ending_spa = pygame.transform.scale(good_ending_spa, (screen_x, screen_y))
""" Nivel 3 (Final Bueno Inglés) """
good_ending_eng = pygame.image.load("images/level_three/good_ending_eng.png")
good_ending_eng = pygame.transform.scale(good_ending_eng, (screen_x, screen_y))
""" Nivel 3 (Final Malo Español) """
level_three_background_two_spa = pygame.image.load("images/level_three/level_three_background_two_spa.png")
level_three_background_two_spa = pygame.transform.scale(level_three_background_two_spa, (screen_x, screen_y))
""" Nivel 3 (Final Malo Blur Español) """
blur_spa = pygame.image.load("images/level_three/blur_spa.png")
blur_spa = pygame.transform.scale(blur_spa, (screen_x, screen_y))
""" Nivel 3 (Final Malo Blur 2 Español) """
blur_two_spa = pygame.image.load("images/level_three/blur_two_spa.png")
blur_two_spa = pygame.transform.scale(blur_two_spa, (screen_x, screen_y))
""" Nivel 3 (Final Malo Inglés) """
level_three_background_two_eng = pygame.image.load("images/level_three/level_three_background_two_eng.png")
level_three_background_two_eng = pygame.transform.scale(level_three_background_two_eng, (screen_x, screen_y))
""" Nivel 3 (Final Malo Blur Inglés) """
blur_eng = pygame.image.load("images/level_three/blur_eng.png")
blur_eng = pygame.transform.scale(blur_eng, (screen_x, screen_y))
""" Nivel 3 (Final Malo Blur 2 Inglés) """
blur_two_eng = pygame.image.load("images/level_three/blur_two_eng.png")
blur_two_eng = pygame.transform.scale(blur_two_eng, (screen_x, screen_y))