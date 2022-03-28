# coding:utf-8
# pip install -U pygame
# pip install -U math

import pygame
from math import sqrt
from pygame.locals import (KEYDOWN, K_ESCAPE, K_SPACE, QUIT)
from data import *
from enemy import Enemy
from player import Player


def score(coefficient:float, quantity:int) -> int:
    return round(sqrt((coefficient/100*quantity)**2))

def run(*args):
    # Lancement de pygame
    pygame.init()

    # Ecran de base
    screen:pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Messages textuels
    font = pygame.font.Font("freesansbold.ttf", 32)
    text_menu_quit = font.render("Press `Escape` to quit.", True, RED)
    text_menu_quit_rect = text_menu_quit.get_rect()
    text_menu_quit_rect.center = (SCREEN_MID_WIDTH, SCREEN_MID_HEIGHT +20)
    text_menu_play = font.render("Press `Space` to play.", True, RED)
    text_menu_play_rect = text_menu_play.get_rect()
    text_menu_play_rect.center = (SCREEN_MID_WIDTH, SCREEN_MID_HEIGHT -20)

    # Boucle de jeu
    MAIN_RUN = True
    while MAIN_RUN:

        # Ecran de menu
        screen.fill(BLACK)
        pygame.display.set_caption("GOLDORAK - In Menu")
        screen.blit(text_menu_play, text_menu_play_rect)
        screen.blit(text_menu_quit, text_menu_quit_rect)
        pygame.display.flip()

        # Boucle du menu
        loop_menu = True
        while loop_menu:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        MAIN_RUN = False
                        loop_game = False
                        loop_menu = False
                    elif event.key == K_SPACE:
                        loop_game = True
                        loop_menu = False
                    else:
                        pass
                elif event.type == QUIT:
                    MAIN_RUN = False
                    loop_game = False
                    loop_menu = False
                else:
                    pass
        
        if loop_game:
            # Utilise pour calculer le score
            game_speed = 35
            time = 0
            # Creation d'un evenement
            ADDENEMY = pygame.USEREVENT +1
            pygame.time.set_timer(ADDENEMY, 250)
            # Notre joueur
            player = Player()
            # Les ennemis a vesqui
            enemies = pygame.sprite.Group()
            sprites = pygame.sprite.Group()
            sprites.add(player)
            # L'horloge en jeu
            clock = pygame.time.Clock()
            # On rafraichit l'ecran
            pygame.display.set_caption("GOLDORAK - Playing")
            pygame.display.flip()
        
        while loop_game:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    pass
                elif event.type == ADDENEMY:
                    new_enemy = Enemy()
                    enemies.add(new_enemy)
                    sprites.add(new_enemy)
                else:
                    pass
            #
            pressed_key = pygame.key.get_pressed()
            player.update(pressed_key=pressed_key)
            enemies.update()
            # Efface le contenu de la fenetre
            screen.fill(BLACK)
            # Augmente la vitesse de rafraichissement du jeu
            game_speed += 0.1
            time += 1
            # Place toutes les entites (ennemis & joueur) dans la fenetre
            to_blit = []
            for entity in sprites.sprites():
                if type(entity) != Player:
                    trajectory = entity.trajectory
                    screen.blit(trajectory[0], trajectory[1])
                to_blit.append((entity.surface, entity.rect))
            screen.blits(to_blit)
            
            # En cas de collision joueur-ennemi
            if pygame.sprite.spritecollideany(player, enemies):
                player.kill()
                loop_game = False
                # Fenetre
                pygame.display.set_caption("GOLDORAK - Score screen")
                # Textes
                text_replay_speed = font.render(f"Vitesse du jeu maximale: {round(game_speed, 2)}", True, RED)
                text_replay_speed_rect = text_replay_speed.get_rect()
                text_replay_speed_rect.center = (SCREEN_MID_WIDTH, SCREEN_MID_HEIGHT -36)
                text_replay_time = font.render(f"Temps de survie: {time}", True, RED)
                text_replay_time_rect = text_replay_time.get_rect()
                text_replay_time_rect.center = (SCREEN_MID_WIDTH, SCREEN_MID_HEIGHT)
                text_replay_score = font.render(f"Score: {score(game_speed, time)}", True, RED)
                text_replay_score_rect = text_replay_score.get_rect()
                text_replay_score_rect.center = (SCREEN_MID_WIDTH, SCREEN_MID_HEIGHT +36)
                # On colle tout.
                screen.fill(BLACK)
                screen.blit(text_replay_speed, text_replay_speed_rect)
                screen.blit(text_replay_time, text_replay_time_rect)
                screen.blit(text_replay_score, text_replay_score_rect)
                pygame.display.update()
                pygame.display.flip()
                # Boucle pour rejouer
                loop_replay = True
                while loop_replay:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key ==  K_SPACE:
                                loop_replay = False
                            else:
                                pass
                        elif event.type == QUIT:
                            MAIN_RUN = False
                            loop_replay = False
                        else:
                            pass
            else:
                pass
            
            pygame.display.flip()
            clock.tick(game_speed)


if __name__ == "__main__":
    run()
