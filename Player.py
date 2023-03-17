import pygame
from Colours import Colours
from Constants import Constants

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(Colours.GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = Constants.WIDTH / 2
        self.rect.bottom = Constants.HEIGHT - 10
        #Собственное:
        self.speedy = 0
        self.isOnJump = False
        self.jumpHeight = 200 #высота прыжка. Придумать, как инвертировать. 234
        #т.е. сделать так, чтоб больше высота - выше прыжок, а не наоборот, как сейчас

    def update(self):
        keystate = pygame.key.get_pressed()

        #Сделать движение влево-вправо
        #Сделать прыжок более реалистичным(настроить скорость подьема и падения)
        #Добавить папку resources и положить туда внешний вид спрайта
    

        if keystate[pygame.K_UP] and not self.isOnJump and self.rect.bottom >= Constants.HEIGHT:
            self.isOnJump = True

        if self.isOnJump and self.jumpHeight <= self.rect.y:
            self.rect.y -= 50#скорость прыжка вверх
            return
        else:
            self.isOnJump = False

        if self.rect.bottom <= Constants.HEIGHT and not self.isOnJump:
            self.rect.y += self.speedy#Скорость падения
            self.speedy += 0.01#Скорсоть падения постоянно увеличивается
        else:
            self.speedy = 0
            self.rect.bottom = Constants.HEIGHT