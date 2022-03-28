# coding:utf-8
# pip install -U pygame
# pip install -U random

import random
import pygame
from data import *


class Enemy(pygame.sprite.Sprite):

    SPRITE_SIZE = (20, 10)
    SPRITE_COLOR = WHITE

    def __init__(self) -> None:
        super(Enemy, self).__init__()
        self.surface = pygame.Surface(self.SPRITE_SIZE)
        self.surface.fill(self.SPRITE_COLOR)
        self.rect = self.surface.get_rect(center=(SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT)))
        self.speed = random.randint(5, 10)
    
    @property
    def x(self) -> int:
        return self.rect.x
    @property
    def y(self) -> int:
        return self.rect.y
    @property
    def trajectory(self) -> tuple[pygame.Surface, pygame.Rect]:
        _trajectory = pygame.Surface((SCREEN_WIDTH, self.SPRITE_SIZE[1]))
        _trajectory.fill(BLUE)
        return (_trajectory, _trajectory.get_rect(center=(self.x-SCREEN_MID_WIDTH, self.y + self.SPRITE_SIZE[1]/2)))
    
    def update(self) -> None:
        self.rect.move_ip(-self.speed, 0)
        if self.x < 0:
            self.kill()