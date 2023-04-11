import os
import pygame
class Constants():
    WIDTH = 480
    HEIGHT = 600
    FPS = 60 #GAME_PATH
    GAME_PATH = os.path.dirname(__file__)
    RECOURCES_PATH = os.path.join(GAME_PATH, 'resources')
    all_sprites = pygame.sprite.Group() # Все движущиеся спрайты
    all_surface_sprites = pygame.sprite.Group() # Все неподвижные спрайты