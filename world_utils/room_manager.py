import pygame
import string

from utils.config import Config
from utils.logger import Logger
from utils.tile_manager import TileManager
from utils.state_manager import StateMachine
from utils.action_queue import ActionQueue
from utils.turn_archetecture import PlayerTurn, EnemyTurn
from world_utils.room import RoomObj

from entities.player import Player
from entities.bug_enemy import Bug

#Room handler will be the entity that creates and manages the turnclasses
# and create the enemy list
class RoomHandler:
    def __init__(self, config: Config, player: Player, room: RoomObj, tileManager: TileManager):
        self.config = config
        self.player = player

        self.enemies = []
        self.tileManager = tileManager
        self.room = room

        self.actionQueue = ActionQueue()
        self.playerTurn = PlayerTurn(None, self.config, self.actionQueue)
        self.enemyTurn = EnemyTurn(None, self.config, self.actionQueue)

        self.player.action_queue = self.actionQueue
        self.load_room_enemies("test")

        self.playerTurn.player = self.player
        self.enemyTurn.enemies = self.enemies

        self.stateMachine = StateMachine(self.playerTurn, self.enemyTurn)


    def load_room_enemies(self, file_name):
        # this will create the list of enemies:
        enemy1 = Bug(self.config, "Bug1", 2, 2)
        enemy2 = Bug(self.config, "Bug2", 2, 4)
        self.enemies = [enemy1, enemy2]

    def update(self):
        self.actionQueue.update()

        self.stateMachine.update()

    def render(self, screen: pygame.Surface):
        self.player.render(screen)

        for enemy in self.enemies:
            enemy.render(screen)