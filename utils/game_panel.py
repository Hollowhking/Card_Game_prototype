import random
import pygame

import utils.config
import utils.logger

from entities.player import Player
from world_utils.map_manager import Map_Manager
from utils.tile_manager import TileManager
# What the game panel will handle:
# Running tick and render for the manager objects: Tilemanager, player, update the room manager which will have the list of monsters
#  
#
class Panel:
    def __init__(self, config: utils.config.Config):
        self.config = config
        self.logger = utils.logger.Logger(self.config)

        self.player = Player(self.config, None, "001")
        self.tileManager = TileManager(self.config)

        self.map_manager = Map_Manager(self.config, [], self.player, self.tileManager)

    def tick(self, keys):
        self.player.process_keys(keys)
        self.map_manager.update()

# tick will have to check if the player is moving to another room
# which will be handled by a int in the tile manager so if it 
# is 0 the player is not within a doorway, if 1,2,3,4 it is in one
# of the doorways depending on the top left right bottom of the 
# room

    def render(self, screen: pygame.Surface):
        self.tileManager.render(screen)
        self.map_manager.render(screen)