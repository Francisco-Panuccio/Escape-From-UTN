from constants import *
from variables import *
from sprites import *
from images import *
from sounds import * 
from functions.score_function import *

#Correr Nivel 1
def run_level_one(screen, font_text, level_one_text, loading_screen):
    if (clock_two["value"] < 4):
        screen.blit(loading_screen, (0,0))
    else:
        screen.blit(level_one_background, (0,0))

    if (clock_two["value"] >= 4 and clock_two["value"] < 8):
        screen.blit(level_one_text, (text_x, text_y))
    elif (clock_two["value"] > 4 or ghostly_vision["value"] == True):
        screen.blit(ghostly_eye, (eye_rect))
        if (lock_condition["value"] == False):
            rect_controller["value"] = False
        
    if (ghostly_vision["value"] == True and crate_hit["value"] == 0):
        screen.blit(crate_states[0], (crate_rect))

    if (crate_hit["value"] > 0 and hammer_screw["value"] == False):
        screen.blit(crate_states[crate_hit["value"]], (crate_rect))
    elif (crate_hit["value"] == 8 and hammer_screw["value"] == True and hammer_screw_used["value"] == False):
        screen.blit(hammer_screwdriver, (crate_rect))

    if (clock_two["value"] >= 4 and lock_condition["value"] == False):
        screen.blit(lock_states[0], (lock_rect))
    elif (clock_two["value"] >= 4 and lock_condition["value"] == True):
        screen.blit(lock_states[1], (lock_rect))

    if (screamer_levels["value"] == True and clock["value"] == 1):
        screen.blit(screamer_monster_one, (0,0))
        scream_monster_one.play()
    elif (screamer_levels["value"] == True and clock["value"] > 1):
        play["value"] = "Level_Two"
        clock_two["value"] = 0
        clock["value"] = 0
        screamer_levels["value"] = False
        ghostly_vision["value"] = False
        crate_hit["value"] = 0
        hammer_screw["value"] = False
        hammer_screw_used["value"] = False
        lock_condition["value"] = 0

    decrease_score(font_text, screen)

#Clickear en Pantalla de Nivel 1
def click_level_one(event):
    if (eye_rect.collidepoint(event.pos)):
        if (ghostly_vision["value"] == False):
            ghostly_vision["value"] = True
        else:
            ghostly_vision["value"] = False
            
    if (ghostly_vision["value"] == True):
        if (crate_rect.collidepoint(event.pos)):
            if (crate_hit["value"] < 8):
                crate_hit["value"] += 1
                hit_crate.play()
            elif (crate_hit["value"] == 8):
                crate_hit["value"] = 8
                if (hammer_screw["value"] == False):
                    broken_crate.play()
                    hammer_screw["value"] = True
                else:
                    hammer_screw_used["value"] = True
                if (hammer_screw_used["value"] == True):
                    lock_condition["value"] = True
                    unlock.play()

    if (lock_rect.collidepoint(event.pos)):
        if (lock_condition["value"] == False):
            lock.play()
        else:
            rect_controller["value"] = True
            screamer_levels["value"] = True
            clock["value"] = 0