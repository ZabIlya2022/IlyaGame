# Игра Shmup - 1 часть
# Cпрайт игрока и управление
import os
import pygame
import random
from Constants import Constants
from Sprites.PlayerSprite import Player
from Colours import Colours
from Sprites.BoxSprite import BoxSprite
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()
box1 = BoxSprite(400, 550, 100)
box2 = BoxSprite(70, 550, 60)
player = Player()
Constants.all_sprites.add(player)
Constants.all_surface_sprites.add(box1, box2)
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(Constants.FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
    background = pygame.image.load("pngtree-magic-red-background-advertising-background-png-image_395568.jpg")
    # Обновление
    Constants.all_sprites.update()
    Constants.all_surface_sprites.update
    # Рендеринг
    # screen.fill(Colours.BLACK)
    screen.blit(background, (0, 0))
    Constants.all_sprites.draw(screen)
    Constants.all_surface_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()