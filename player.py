#coding:utf-8

import pygame
from pygame import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, K_SPACE, QUIT)
from data import *


class Player(pygame.sprite.Sprite):

    SPRITE_SIZE = (75, 25)
    SPRITE_COLOR = WHITE

    def __init__(self) -> None:
        super(Player, self).__init__()
        self.surface = pygame.Surface(self.SPRITE_SIZE)
        self.surface.fill(self.SPRITE_COLOR)
        self.rect = self.surface.get_rect()
        self.speed = 5

    @property
    def x(self) -> int:
        return self.rect.x
    @property
    def y(self) -> int:
        return self.rect.y

    @property
    def top(self) -> int:
        return self.rect.top
    @property
    def bottom(self) -> int:
        return self.rect.bottom
    @property
    def left(self) -> int:
        return self.rect.left
    @property
    def right(self) -> int:
        return self.rect.right
    
    def update(self, pressed_key) -> None:
        if pressed_key[K_UP]:
            self.rect.move_ip(0, -self.speed)
            if self.top < 0:
                self.rect.top = 0
        elif pressed_key[K_DOWN]:
            self.rect.move_ip(0, self.speed)
            if self.bottom > SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT
        elif pressed_key[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
            if self.left < 0:
                self.rect.left = 0
        elif pressed_key[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
            if self.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
