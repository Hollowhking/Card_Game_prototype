import pygame
import math
import sys
import random
import math
import time
import threading
import os

#local imports:
import utils.config


def main():     
    config = utils.config.Config()
    time_between_frame_update = round((1/config.FPS) * 1000, 2)

    pygame.init()
    screen = pygame.display.set_mode((config.window_width, config.window_height))

    running = True
    while running:
        #Time managing:
        prev_time = int(round(time.time() * 1000))
        #-----------------------------

        #-----------------------------
        new_time = int(round(time.time() * 1000))
        time_taken = new_time - prev_time
        if (time_taken < time_between_frame_update):
            time.sleep((time_between_frame_update - time_taken)/1000)

def _key_handler(panel: Panel) -> None:
    for event in pygame.event.get():

        # Debug_exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                print("DEBUG EXIT")
                pygame.quit()
                exit(0)

if __name__ == '__main__':
    main()