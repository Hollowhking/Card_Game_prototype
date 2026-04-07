
class Punch:
    def __init__(self, location, damage, direction):
        self.location  = location
        self.damage    = damage
        self.direction = direction

    def execute(self, enemy_list):
        # Show the punch animation
        # circle through each enemy locations check if a punch will land
        pass