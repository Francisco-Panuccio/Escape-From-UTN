from constants import *
from variables import *
from images import * 
from sounds import *
from rects import *
from functions.score_function import *

#Correr Nivel 2
def run_level_two(screen, loading_screen, font_text, frames_clock, level_two_text, board, chair, window):
    if (clock_two["value"] < 4):
        screen.blit(loading_screen, (0,0))
    if (clock["value"] >= 2 and clock["value"] < 3):
        scream_monster_one.stop()
        interference.play()
        screen.blit(real_classroom, (0,0))
    if (clock["value"] >= 4 and clock["value"] <= 5):
        screen.blit(level_two_background_light, (0,0))
        screen.blit(level_two_text, (text_x, text_y))
    if (clock["value"] > 5):
        screen.blit(level_two_background, (0,0))
        rect_controller["value"] = False
    if (clock["value"] == 6):
        interference.stop()
        broken_bulb.play()

    if (level_two_image["value"] == "Board"):
        screen.blit(board, (level_two_game_x, level_two_game_y))
    elif (level_two_image["value"] == "Chair"):
        screen.blit(chair, (level_two_game_x, level_two_game_y))
    elif (level_two_image["value"] == "Window"):
        screen.blit(window, (level_two_game_x, level_two_game_y))
    elif (level_two_image["value"] == "Book"):
        screen.blit(book_code, (level_two_game_x, level_two_game_y))
    elif (level_two_image["value"] == "Codelock"):
        screen.blit(codelock, (level_two_game_x, level_two_game_y))
        code_text = font_text.render(code_door["value"], True, (white))
        screen.blit(code_text, (code_text_x, code_text_y))
        frames_clock.tick(60)
        if (codelock_condition["value"] == True and clock_two["value"] >= 2):
            scream_monster_two.play()
            screen.blit(screamer_monster_two, (0,0))
        if (codelock_condition["value"] == True and clock_two["value"] == 4):
            codelock_condition["value"] = False
            rect_controller["value"] = True
            level_two_check["value"] = "Board"
            level_two_image["value"] = ""
            code_door["value"] = ""
            play["value"] = "Level_Three"
            clock_two["value"] = 0
            clock["value"] = 0
    decrease_score(font_text, screen)

#Clickear en Pantalla de Nivel 2
def click_level_two(event):
    if (level_two_check["value"] == "Board"):
        if (board_rect.collidepoint(event.pos)):
            level_two_image["value"] = "Board"

    if (level_two_check["value"] == "Chair"):
        if (chair_rect.collidepoint(event.pos)):
            level_two_image["value"] = "Chair"

    if (level_two_check["value"] == "Window"):
        if (window_rect.collidepoint(event.pos)):
            level_two_image["value"] = "Window"

    if (level_two_check["value"] == "Book"):
        if (book_rect.collidepoint(event.pos)):
            level_two_image["value"] = "Book"

    if (level_two_check["value"] == "Codelock"):
        if (codelock_rect.collidepoint(event.pos)):
            level_two_image["value"] = "Codelock"
        elif (book_rect.collidepoint(event.pos)):
            level_two_image["value"] = "Book"

    if (close_image_rect.collidepoint(event.pos)):
        if (level_two_check["value"] == "Board"):
            level_two_image["value"] = ""
            level_two_check["value"] = "Chair"
        elif (level_two_check["value"] == "Chair"):
            level_two_image["value"] = ""
            level_two_check["value"] = "Window"
        elif (level_two_check["value"] == "Window"):
            level_two_image["value"] = ""
            level_two_check["value"] = "Book"
        elif (level_two_check["value"] == "Book"):
            level_two_image["value"] = ""
            level_two_check["value"] = "Codelock"
        elif (level_two_check["value"] == "Codelock"):
            level_two_image["value"] = ""