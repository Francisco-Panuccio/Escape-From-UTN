import pygame
from constants import *
from variables import *
from icons import *

#Rectángulos Main
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
score_rect.x = score_x
score_rect.y = score_y
""" Logo (Misterio) """
logo_rect = pygame.Rect((logo_x, logo_y), (logo_width, logo_height))
logo_rect.x = logo_x
logo_rect.y = logo_y
""" Volver al Menú Principal (Desde Score) """
return_main_score_rect = pygame.Rect((return_main_score_x, return_main_score_y), (return_main_score_width, return_main_score_height))
return_main_score_rect.x = return_main_score_x
return_main_score_rect.y = return_main_score_y
""" Jugar """
play_rect = pygame.Rect((play_x, play_y), (play_width, play_height))
play_rect.x = play_x
play_rect.y = play_y
""" Flecha para Continuar """
arrow_rect = pygame.Rect((arrow_x, arrow_y), (arrow_width, arrow_height))
arrow_rect.x = arrow_x
arrow_rect.y = arrow_y
""" Puntaje Global """
global_score_rect = pygame.Rect((global_score_x, global_score_y), (global_score_width, global_score_height))
global_score_rect.x = global_score_x
global_score_rect.y = global_score_y
""" Puntaje Global Bordes """
global_score_border_rect = pygame.Rect((global_score_border_x, global_score_border_y), (global_score_border_width, global_score_border_height))
global_score_border_rect.x = global_score_border_x
global_score_border_rect.y = global_score_border_y

#Rectángulos Nivel Uno
""" Ojo (Visión Fantasmal) (Nivel Uno) """
eye_rect = pygame.Rect((eye_x, eye_y), (eye_width, eye_height))
eye_rect.x = eye_x
eye_rect.y = eye_y
""" Sprite Caja (Nivel Uno) """
crate_rect = pygame.Rect((crate_x, crate_y), (crate_width, crate_height))
crate_rect.x = crate_x
crate_rect.y = crate_y
""" Sprite Candado (Nivel Uno) """
lock_rect = pygame.Rect((lock_x, lock_y), (lock_width, lock_height))
lock_rect.x = lock_x
lock_rect.y = lock_y

#Rectángulos Nivel Dos
""" Pizarrón (Nivel Dos) """
board_rect = pygame.Rect((board_x, board_y), (board_width, board_height))
board_rect.x = board_x
board_rect.y = board_y
""" Silla (Nivel Dos) """
chair_rect = pygame.Rect((chair_x, chair_y), (chair_width, chair_height))
chair_rect.x = chair_x
chair_rect.y = chair_y
""" Ventana (Nivel Dos) """
window_rect = pygame.Rect((window_x, window_y), (window_width, window_height))
window_rect.x = window_x
window_rect.y = window_y
""" Libro con Código (Nivel Dos) """
book_rect = pygame.Rect((book_x, book_y), (book_width, book_height))
book_rect.x = book_x
book_rect.y = book_y
""" Puerta con Código (Nivel Dos) """
codelock_rect = pygame.Rect((codelock_x, codelock_y), (codelock_width, codelock_height))
codelock_rect.x = codelock_x
codelock_rect.y = codelock_y
""" Cerrar Imagen (Nivel Dos) """
close_image_rect = pygame.Rect((close_image_x, close_image_y), (close_image_width, close_image_height))
close_image_rect.x = close_image_x 
close_image_rect.y = close_image_y

#Rectángulos Nivel Tres
""" Casillero (Nivel Tres) """
locker_three_rect = pygame.Rect((locker_three_x, locker_three_y), (locker_three_width, locker_three_height))
locker_three_rect.x = locker_three_x
locker_three_rect.y = locker_three_y
""" Puerta (Nivel Tres) """
door_three_rect = pygame.Rect((door_three_x, door_three_y), (door_three_width, door_three_height))
door_three_rect.x = door_three_x
door_three_rect.y = door_three_y
""" Temporizador (Nivel Tres) """
timer_three_rect = pygame.Rect((timer_three_x, timer_three_y), (timer_three_width, timer_three_height))
timer_three_rect.x = timer_three_x
timer_three_rect.y = timer_three_y
""" Volver al Menú Principal (Nivel Tres) """
return_main_rect = pygame.Rect((return_main_x, return_main_y), (return_main_width, return_main_height))
return_main_rect.x = return_main_x
return_main_rect.y = return_main_y