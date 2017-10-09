# moved import sys to game_functions.py

import pygame # import module to make a game

from settings import Settings
from ship   import Ship
from alien import Alien
from game_stats import GameStats
import game_functions as gf
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard



# define new function to run game:
def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    # Make an alien
    alien = Alien(ai_settings, screen)
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings,screen, aliens, stats, play_button, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button)



run_game()
