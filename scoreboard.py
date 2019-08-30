# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 06:29:15 2019

@author: Mike
"""

import pygame

class Scoreboard:
    
    def __init__(self,br_game):
        
        self.screen = br_game.screen
        self.screen_rect = br_game.screen.get_rect()
        self.settings = br_game.settings
        self.score = 0
        self.bomb_clicked = 0
        
        self.text_color = (252,3,53)
        self.font = pygame.font.SysFont('arial',48)
        
        self.prep_score()
        
        
    def prep_score(self):
        """Implement score into image"""
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True,
                                    self.text_color,self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        
        