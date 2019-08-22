# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 08:53:19 2019

@author: Mike
"""


class Settings:
    """Class to store all Bomber Reflex's settings"""
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (96,96,96)
        
        self.bombs = 10
        self.timer = 500
        self.bomb_points = 10000
        self.level = 1
        
        self.score = 0