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

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 8
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 8
        if keystate[pygame.K_UP]:
            self.rect.y = 100
        if keystate[pygame.K_DOWN]:
            self.rect.y += 0

        if self.rect.right > Constants.WIDTH:
            self.rect.right = Constants.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > Constants.HEIGHT:
            self.rect.bottom = Constants.HEIGHT
        else:
            self.rect.y += 4
        self.speedy = 0
        self.isOnJump
        self.jumpHeight

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP] and not self.isOnJump and self.rect.bottom >= Constants.HEIGHT:
            self.isOmJump = True

            if self.isonjump and self.jumpHeight <= self.rect.y:
