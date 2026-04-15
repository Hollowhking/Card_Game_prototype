import time

from entities.player import Player
from utils.config import Config
from utils.action_queue import ActionQueue

class PlayerTurn:
    def __init__(self, config: Config, player: Player, action_queue: ActionQueue):
        self.id = "Player"
        self.config = config
        self.actionQueue = action_queue

        self.player = player
        self.done = False

        # timer values:
    def start_turn(self):
        self.done = False

    def update(self):
        if self.actionQueue.is_empty():
            if self.player.end_turn:
                return True
        
        if not self.actionQueue.is_empty():
            return False
        
        return False

    def reset(self):
        self.player.reset_turn()
        self.actionQueue.clear()

class EnemyTurn:
    def __init__(self, enemies, config: Config, action_queue: ActionQueue):
        self.id = "Enemy"
        self.config = config
        self.enemies = enemies
        self.queue = action_queue
        self.currentIndex = 0
        self.started = False

    def start_turn(self):
        self.index = 0
        self.started = True

    def update(self):
        if not self.started:
            return False
        
        if self.queue.is_empty():
            print("Queue empty")
            if self.currentIndex < len(self.enemies):
                enemy = self.enemies[self.currentIndex]
                enemy.decideActions(self.queue)
                self.currentIndex += 1
            else:
                return True

    def add_action_to_queue(self, action, actor):
        print(f"actor: {actor.name} performing action: {action.name}")
        self.currentQueue.append(action)

    def reset(self):
        self.currentIndex = 0
        self.started = False