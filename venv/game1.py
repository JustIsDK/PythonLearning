import sys
from  setting import Settings
import pygame
from ship import Ship
import game_functions as gf


# def run_game():

#     pygame.init()
#     screen = pygame.display.set_mode((1120,800))
#     pygame.display.set_caption('Alien Invasion')
#
#     bg_color = (230,230,230)
#
#     while True:
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#         screen.fill(bg_color)
#
#         pygame.display.flip()
#
# run_game()

def run_game():

    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    while True:

        gf.check_events()

        screen.fill(ai_setting.bg_color)

        ship.blitme()

        pygame.display.flip()

run_game()