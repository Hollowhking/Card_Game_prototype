import time

from utils.turn_archetecture import PlayerTurn
from utils.turn_archetecture import EnemyTurn

class StateMachine:
    def __init__(self, playerturn: PlayerTurn, enemyturn: EnemyTurn):
        self.playerturn = playerturn
        self.enemyturn  = enemyturn
        self.current_state = playerturn

        self.enter_state(self.current_state)

    def update(self):
        # triggers once a turn is finished 
        if self.current_state.update():
            self.current_state.reset() # resets the current state

            if self.current_state == self.playerturn:
                self.current_state = self.enemyturn
            else: 
                self.current_state = self.playerturn

            self.enter_state(self.current_state)
    
    def enter_state(self, state):
        self.playerturn.player.can_act = False
        for e in self.enemyturn.enemies:
            e.can_act = False

        if state == self.playerturn:
            self.playerturn.player.can_act = True
            self.playerturn.start_time = time.time()
        if state == self.enemyturn:
            self.enemyturn.enemies[0].can_act = True
            self.enemyturn.waiting_start_time = time.time()