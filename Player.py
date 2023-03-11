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
            self.rect.y -= 8
        if keystate[pygame.K_DOWN]:
            self.rect.y += 8

        if self.rect.right > Constants.WIDTH:
            self.rect.right = Constants.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > Constants.HEIGHT:
            self.rect.bottom = Constants.HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        self.isonjump = False
        self.jumpheight = 400

    def updat(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP] and not self.isonjump and self.rect.bottom >= Constants.HEIGHT:
            self.isonjump = True

        if self.isonjump and self.jumpheight <= self.rect.y:
            self.rect.y -= 5
            return
        else:
            self.isonjump = False

        if self.rect.bottom <= Constants.HEIGHT and not self.isonjump:
            self.rect.y += self.speedy
            self.speedy +=2
        else:
            self.speedy = 0
            self.rect.bottom = Constants.HEIGHT

all_sprites = pygame.sprite.Group()
player = Player()