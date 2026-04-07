import math
import random
import pygame
import time

from utils.config import Config
from utils.logger import Logger
from actions.movement_action import move_Tile

class Player:
    def __init__(self, config: Config, action_callback):
        self.config = config
        self.logger = Logger(self.config)
        #keyboard:
        self.w_press       = False
        self.a_press       = False
        self.s_press       = False
        self.d_press       = False
        self.q_press       = False
        self.space_press   = False

        self.mouse_x       = 0
        self.mouse_y       = 0
        #======================
        self.x = 5
        self.y = 10
        self.screen_x = 0
        self.screen_y = 0
        self.draw_box = (self.screen_x, self.screen_y, self.config.tile_size, self.config.tile_size)

        self.current_action  = None
        self.end_turn        = False
        self.can_act         = True
        self.action_callback = action_callback

        self.last_valid_key_press = time.time()

    def update(self, keys):
        if not self.can_act:
            return

        self.process_keys(keys)
        self.update_x_movement()
        # turns tile location to screen location happens last:
        self.scale_location()
        self.draw_box = (self.screen_x, self.screen_y, self.config.tile_size, self.config.tile_size)


    def render(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.config.RED, self.draw_box)

    def update_x_movement(self):
        if (self.w_press):
            move_action = move_Tile(self, (self.x, self.y), (self.x, self.y - 1))
            self.w_press = False
            if (self.can_act):
                self.action_callback(move_action)

        elif (self.a_press):
            move_action = move_Tile(self, (self.x, self.y), (self.x - 1, self.y))
            self.a_press = False
            if (self.can_act):
                self.action_callback(move_action)

        elif (self.s_press):
            move_action = move_Tile(self, (self.x, self.y), (self.x, self.y + 1))
            self.s_press = False
            if (self.can_act):
                self.action_callback(move_action)

        elif (self.d_press):
            move_action = move_Tile(self, (self.x, self.y), (self.x + 1, self.y))
            self.d_press = False
            if (self.can_act):
                self.action_callback(move_action)

    def process_keys(self, keys):
        if (self.end_turn):
            self.end_turn = False
        if not keys[pygame.K_w]:
            self.w_press = False
                
        if not self.w_press:
            if keys[pygame.K_w]:
                if self.key_press_allowed():
                    self.w_press = True
                    self.last_valid_key_press = time.time()

        if not keys[pygame.K_a]:
            self.a_press = False
    
        if not self.a_press:
            if keys[pygame.K_a]:
                if self.key_press_allowed():
                    self.a_press = True
                    self.last_valid_key_press = time.time()

        if not keys[pygame.K_d]:
            self.d_press = False
    
        if not self.d_press:
            if keys[pygame.K_d]:
                if self.key_press_allowed():
                    self.d_press = True
                    self.last_valid_key_press = time.time()

        if not keys[pygame.K_s]:
            self.s_press = False

        if not self.s_press:
            if keys[pygame.K_s]:
                if self.key_press_allowed():
                    self.s_press = True
                    self.last_valid_key_press = time.time()

        if not keys[pygame.K_SPACE]:
            self.space_press = False

        if not self.space_press:
            if keys[pygame.K_SPACE]:
                if self.key_press_allowed():
                    self.space_press = True
                    self.last_valid_key_press = time.time()
                    self.end_turn = True
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()


    def reset_turn(self):
        self.can_act = False
        print("End Turn: Player")

    def key_press_allowed(self):
        cur_time = time.time()
        if (self.last_valid_key_press + self.config.movement_buffer_time_limit_seconds < cur_time):
            return True
        else:
            return False

    def scale_location(self):
        self.screen_x = self.x * self.config.tile_size
        self.screen_y = self.y * self.config.tile_size

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y


    def update_config(self, config: Config):
        self.config = config