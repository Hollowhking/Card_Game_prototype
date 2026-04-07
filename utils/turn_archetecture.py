import time

from entities.player import Player
from utils.config import Config
from utils.action_queue import ActionQueue

class PlayerTurn:
    def __init__(self, player: Player, config: Config):
        self.config = config
        self.player      = player
        self.actionQueue = []

        self.start_time = time.time()
        self.current_time = 0

    def update(self):
        # Get time for turn timer:
        self.current_time = time.time()
        # if queue empty wait for action
        if not self.actionQueue:
            if self.player.end_turn or (self.current_time >= (self.config.Max_Turn_Timer + self.start_time)):
                return True

        # display spell on screen
        if self.actionQueue:
            current_action = self.actionQueue[-1]

            current_action.execute(None)

            self.actionQueue.pop()

        # check if player can still make actions if they cant auto pass turn?
        return False

    def add_action_to_queue(self, action):
        print(f"actor: Player performing action: {action.name}")
        self.actionQueue.append(action)

    def reset(self):
        self.player.reset_turn()
        self.actionQueue.clear()

class EnemyTurn:
    def __init__(self, enemies, config: Config, action_queue: ActionQueue):
        self.config = config
        self.enemies = enemies
        self.queue = action_queue
        self.currentIndex = 0
        self.started = False

    def begin(self):
        self.currentIndex = 0
        self.started = True

    def update(self):
        if not self.started:
            return
        
        if self.queue.is_empty():
            if self.currentIndex < len(self.enemies):
                enemy = self.enemies[self.currentIndex]
                enemy.decideActions()
                self.currentIndex += 1
            else:
                self.started = False
                print("Enemy: ", enemy.name, " turn finished")

    def add_action_to_queue(self, action, actor):
        print(f"actor: {actor.name} performing action: {action.name}")
        self.currentQueue.append(action)

    def reset(self):
        self.currentIndex = 0
        self.currentQueue.clear()