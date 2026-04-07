import random
import pygame

import utils.config
import utils.logger
from utils.tile_manager import TileManager
from utils.state_manager import StateMachine
from utils.turn_archetecture import PlayerTurn
from utils.turn_archetecture import EnemyTurn

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

        # Here should be a room manager that for each room takes a player and a defined room file which includes all data for each encounter
        self.playerTurn = PlayerTurn(None, self.config)
        self.enemyTurn  = EnemyTurn(None, self.config)

        self.player = Player(self.config, self.playerTurn.add_action_to_queue)

        enemy1 = Bug(self.config, self.enemyTurn.add_action_to_queue, "Bug1")
        self.enemyarray = [enemy1]

        self.playerTurn.player = self.player
        self.enemyTurn.enemies = self.enemyarray

        self.statemachine = StateMachine(self.playerTurn, self.enemyTurn)
        #===========================================================
        self.tilemanager  = TileManager(self.config)
        self.tilemanager.load_room("test")

    def tick(self, keys):
        self.statemachine.update()

        self.player.update(keys)
        for enemy in self.enemyarray:
            enemy.update()

    def render(self, screen: pygame.Surface):
        self.tilemanager.render(screen)
        self.player.render(screen)
        for enemy in self.enemyarray:
            enemy.render(screen)