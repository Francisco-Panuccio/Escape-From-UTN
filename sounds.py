import pygame

#Música General
pygame.mixer.init()
pygame.mixer.music.load("sounds/general/background.mp3")
pygame.mixer.music.play(-1)

#Sonidos
""" General """
interference = pygame.mixer.Sound("sounds/general/interference.mp3")
evil_laugh = pygame.mixer.Sound("sounds/general/evil_laugh.mp3")

""" Main """
thunder = pygame.mixer.Sound("sounds/main/thunder.mp3")
scream_logo_sound = pygame.mixer.Sound("sounds/main/scream_logo.mp3")
whispers_start = pygame.mixer.Sound("sounds/main/whispers_start.mp3")
bullying = pygame.mixer.Sound("sounds/main/beginning.mp3")
scream_echo = pygame.mixer.Sound("sounds/main/scream_echo.mp3")

""" Nivel Uno """
hit_crate = pygame.mixer.Sound("sounds/level_one/hit_crate.mp3")
broken_crate = pygame.mixer.Sound("sounds/level_one/broken_crate.mp3")
lock = pygame.mixer.Sound("sounds/level_one/lock.mp3")
unlock = pygame.mixer.Sound("sounds/level_one/unlock.mp3")
open_door = pygame.mixer.Sound("sounds/level_one/open_door.mp3")
scream_monster_one = pygame.mixer.Sound("sounds/level_one/scream_monster_one.mp3")

""" Nivel Dos """
broken_bulb = pygame.mixer.Sound("sounds/level_two/broken_bulb.mp3")
scream_monster_two = pygame.mixer.Sound("sounds/level_two/scream_monster_two.mp3")
wrong_code = pygame.mixer.Sound("sounds/level_two/wrong_code.mp3")
correct_code = pygame.mixer.Sound("sounds/level_two/correct_code.mp3")

""" Nivel Tres """
scream_monster_three = pygame.mixer.Sound("sounds/level_three/scream_monster_three.mp3")
timer = pygame.mixer.Sound("sounds/level_three/timer.mp3")
bad_ending_bell = pygame.mixer.Sound("sounds/level_three/bad_ending_bell.mp3")
whispers = pygame.mixer.Sound("sounds/level_three/whispers.mp3")
screams = pygame.mixer.Sound("sounds/level_three/screams.mp3")
correct = pygame.mixer.Sound("sounds/level_three/correct.mp3")
final_good_ending = pygame.mixer.Sound("sounds/level_three/final_good_ending.mp3")