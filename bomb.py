# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 09:04:33 2019

@author: Mike
"""


import pygame
import random
from pygame.sprite import Sprite

class Bomb(Sprite):
    """A class to manage the bomb."""
    
    def __init__(self,br_game):
        """Initialize the bomb and set its starting position."""
        super().__init__()
        self.screen = br_game.screen
        self.screen_rect = br_game.screen.get_rect()
        
        self.settings = br_game.settings
        
        """Load bomb and get its rect"""
        picture = pygame.image.load("images/2.png")
        self.image = pygame.transform.scale(picture,(80,80))
        self.rect = self.image.get_rect()
        
        
        
    def update(self):
        """Update new bomb position"""
        self.rect.x = (random.randint(0,1120))
        self.rect.y = (random.randint(0,720))
        self.randpos = (self.rect.x,self.rect.y)

        

        
    def blitme(self):
        """Draw the bombs in random location on screen"""
        #self.rand_pos = (random.randint(0,1120),random.randint(0,720))
        self.screen.blit(self.image,(self.randpos))
        pygame.display.update()
        

        
        
            