import pygame
import time

from utils.config import Config
from utils.logger import Logger
from actions.movement_action import move_Tile

class Bug:
    def __init__(self, config: Config, action_callback, name):
        self.config = config
        self.logger = Logger(self.config)
        #

        #========================
        self.name = name
        self.x = 2
        self.y = 2
        self.screen_x = self.x
        self.screen_y = self.y
        self.draw_box = (self.screen_x, self.screen_y, self.config.tile_size, self.config.tile_size)

        self.can_act = False
        self.action_callback = action_callback

        self.last_valid_action = time.time()
        self.scale_location()


    def update(self):
        if not self.can_act:
            return
        
        #once per each AP call this: 
        self.decideActions()

        
    def render(self, screen: pygame.Surface):
        self.scale_location()
        self.draw_box = (self.screen_x, self.screen_y, self.config.tile_size, self.config.tile_size)

        pygame.draw.rect(screen, self.config.BLUE, self.draw_box)


    def decideActions(self):
        if self.actionAllowed():
            move_action = move_Tile(self, (self.x, self.y), (self.x + 1, self.y))
            self.action_callback(move_action, self)

    def actionAllowed(self):
        cur_time = time.time()
        if (self.last_valid_action + self.config.movement_buffer_time_limit_seconds < cur_time):
            return True
        else:
            return False
    #===================
    def reset_turn(self):
        self.can_act = False
        print("End Turn: ", self.name)

    def scale_location(self):
        self.screen_x = self.x * self.config.tile_size
        self.screen_y = self.y * self.config.tile_size

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y
