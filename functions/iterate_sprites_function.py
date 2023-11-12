import pygame

def iterate_sprites(end_range, path_sprite, list, width, height):
    for i in range(1, end_range):
        path = path_sprite + str(i) + ".png"
        sprite = pygame.image.load(path)
        sprite = pygame.transform.scale(sprite, (width, height))
        list.append(sprite)