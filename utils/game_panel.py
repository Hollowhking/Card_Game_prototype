import random
import pygame

import utils.config
import utils.logger
from utils.tile_manager import TileManager
from utils.state_manager import StateMachine
from utils.turn_archetecture import PlayerTurn
from utils.turn_archetecture import EnemyTurn
from utils.action_queue import ActionQueue

from entities.player import Player
from entities.bug_enemy import Bug
# What the game panel will handle:
# Running tick and render for the manager objects: Tilemanager, player, update the room manager which will have the list of monsters
#  
#
class Panel:
    def __init__(self, config: utils.config.Config):
        self.config = config
        self.logger = utils.logger.Logger(self.config)

        self.actionQueue = ActionQueue()
        # Here should be a room manager that for each room takes a player and a defined room file which includes all data for each encounter
        self.playerTurn = PlayerTurn(None, self.config, self.actionQueue)
        self.enemyTurn  = EnemyTurn(None, self.config, self.actionQueue)

        self.player = Player(self.config, self.actionQueue)

        enemy1 = Bug(self.config, "Bug1", 2, 2)
        enemy2 = Bug(self.config, "Bug2", 2, 4)
        self.enemyarray = [enemy1, enemy2]

        self.playerTurn.player = self.player
        self.enemyTurn.enemies = self.enemyarray

        self.statemachine = StateMachine(self.playerTurn, self.enemyTurn)
        #===========================================================
        self.tilemanager  = TileManager(self.config)
        self.tilemanager.load_room("test")

    def tick(self, keys):
        self.player.process_keys(keys)
        self.actionQueue.update()

        self.statemachine.update()


# tick will have to check if the player is moving to another room
# which will be handled by a int in the tile manager so if it 
# is 0 the player is not within a doorway, if 1,2,3,4 it is in one
# of the doorways depending on the top left right bottom of the 
# room

    def render(self, screen: pygame.Surface):
        self.tilemanager.render(screen)
        self.player.render(screen)
        for enemy in self.enemyarray:
            enemy.render(screen)