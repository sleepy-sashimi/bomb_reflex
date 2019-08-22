# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 08:40:36 2019

@author: Mike
"""

import sys
import pygame
from settings import Settings
from bomb import Bomb
from scoreboard import Scoreboard

clock = pygame.time.Clock()
time_counter = 0


class BomberReflex:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
    
        self.screen = pygame.display.set_mode(
                (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Bomber Reflex")
        
        self.scoreboard = Scoreboard(self) 
        self.bombs = pygame.sprite.Group()


        
    def run_game(self):
        """Start the main loop for the game."""
        self.clock = pygame.time.Clock()
        elapsed_time = 0

        while True:
            time_delta = clock.tick(60)
            elapsed_time += time_delta
            
            #Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.scoreboard.show_score()
            if elapsed_time >= self.settings.timer:
                self._create_bombs()
                elapsed_time -= self.settings.timer
            self._check_events()
            self.bombs.draw(self.screen)
             
            #Make the most recently drawn screen visible
            pygame.display.flip()
    
    def _increase_diff(self):
        self.settings.level += 1
        self.settings.timer -= 50

    def _create_bombs(self):
        self.bomb = Bomb(self)
        self.bombs.add(self.bomb)
        self.bomb.update()
        
    def _check_bomb_click(self,mouse_pos):
        #Deactivate bomb when clicked
        for bomb in self.bombs:
            bomb_clicked = bomb.rect.collidepoint(mouse_pos)
            if bomb_clicked:
                bomb.kill()
                self.scoreboard.score += self.settings.bomb_points
                self.scoreboard.bomb_clicked += 1
                self.scoreboard.prep_score()         

                
            
    def _check_events(self):
        #Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_bomb_click(mouse_pos)
            elif self.scoreboard.bomb_clicked > 9:
                self._increase_diff()
                self.scoreboard.bomb_clicked = 0
                    
            
    
if __name__ == '__main__':
    #Make game instance and run game
    br = BomberReflex()
    br.run_game()
        
