from constants import *
from variables import *

#Disminuir Score
def decrease_score(font_text, screen):
    score_number = score["value"]
    score_text = font_text.render(f"Score: {score_number}", True, (white))
    screen.blit(score_text, (score_text_x, score_text_y))
    if (clock_two["value"] == 122):
        score["value"] = score["value"] - 10
        clock_two["value"] = 4
    if (score["value"] < 0):
        score["value"] = 0