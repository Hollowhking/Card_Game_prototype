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
        print("Current entity: ", self.current_state.id)
        if self.current_state.update():
            self.current_state.reset() # resets the current state

            if self.current_state == self.playerturn:
                self.current_state = self.enemyturn
            else: 
                self.current_state = self.playerturn

            self.enter_state(self.current_state)
    
    def enter_state(self, state):

        if state == self.playerturn:
            print("start_turn: Player")
            self.playerturn.start_turn()
        if state == self.enemyturn:
            print("start_turn: Enemy")
            self.enemyturn.start_turn()