from constants import *
from variables import *
from images import * 
from rects import *
from sounds import *
from class_player import *
from functions.score_function import *

#Correr Nivel 3
def run_level_three(screen, font_text, loading_screen, bad_ending, blur, blur_two, good_end):
    if (clock["value"] >= 0 and clock["value"] < 3):
        screen.blit(loading_screen, (0,0))
    if (clock["value"] >= 3 and clock["value"] < 4):
        scream_monster_two.stop()
        interference.play()
        screen.blit(real_hallway, (0,0))
    if (clock["value"] == 4):
        timer.play()
    if (clock["value"] >= 4 and good_ending["value"] == False):
        screen.blit(level_three_background, (0,0))
        timer_condition["value"] = True
        rect_controller["value"] = False
        final_timer_var = final_timer["value"]
        if (final_timer["value"] >= 0):
            final_timer_text = font_text.render(f"{final_timer_var}", True, (black))
            screen.blit(final_timer_text, (final_timer_text_x, final_timer_text_y))
        else:
            timer_condition["value"] = False
            rect_controller["value"] = True
            if (clock_two["value"] == 4):
                timer.stop()
                interference.play()
                whispers.play()
                bad_ending_bell.play()
                screams.play()
            if(clock_two["value"] >= 4):
                screen.blit(bad_ending, (0,0))
            if (clock_two["value"] >= 16 and clock_two["value"] <= 18):
                interference.play()
                screen.blit(bad_ending_monster, (0,0))
                scream_monster_three.play()
            if (clock_two["value"] > 18 and clock_two["value"] < 36):
                screen.blit(blur, (0,0))
            if (clock_two["value"] >= 36 and clock_two["value"] <= 38):
                interference.play()
                screen.blit(bad_ending_monster_two, (0,0))
            if (clock_two["value"] > 38 and clock_two["value"] < 52):
                screen.blit(blur_two, (0,0))
            if (clock_two["value"] >= 52 and clock_two["value"] <= 60):
                interference.play()
                screen.blit(bad_ending_monster_three, (0,0))
            if (clock_two["value"] == 60):
                running["value"] = False
    if (good_ending["value"] == True):
        screen.blit(good_end, (0,0))
        final_good_ending.play()
        return_main["value"] = True
    decrease_score(font_text, screen)

#Clickear en Pantalla de Nivel 3
def click_level_three(event):
    if (level_three_check["value"] == "Locker"):
        if (locker_three_rect.collidepoint(event.pos)):
            timer.stop() #Solución a bug que no me dejaba reproducir otro sonido por encima
            correct.play()
            timer.play()
            level_three_check["value"] = "Door"
    
    if (level_three_check["value"] == "Door"):
        if (door_three_rect.collidepoint(event.pos)):
            timer.stop()
            correct.play()
            timer.play()
            level_three_check["value"] = "Timer"
            
    if (level_three_check["value"] == "Timer"):
        if (timer_three_rect.collidepoint(event.pos)):
            timer.stop()
            correct.play()
            #Guardar Data del Jugador
            Player.save_player_data("Global_Score.json", player["name"], score["value"])
            good_ending["value"] = True

    if (return_main["value"] == True):
        if (return_main_rect.collidepoint(event.pos)):
            final_good_ending.stop()
            correct.play()
            play["value"] = "Main"
            level_three_check["value"] = "Locker"
            final_timer["value"] = 60
            good_ending["value"] = False
            return_main["value"] = False