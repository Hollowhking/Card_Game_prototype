import time

from utils.tile_manager import Room

class move_Tile:
    def __init__(self, entity, source, target, duration = 2):
        self.entity = entity
        self.source = source
        self.target = target
        self.name = f"Movement_Action from {str(source)} to {str(target)}"
        self.duration = duration

        self.start_time = time.time()
        self.is_done = False

    def begin(self):
        self.start_time = time.time()

    def execute(self, room: Room):
        if self.is_done:
            return

        duration_timer = (time.time - self.start_time) / self.duration

        if duration_timer >= 1:
            self.entity.set_x(self.target[0])
            self.entity.set_y(self.target[1])
            self.is_done = True
        # check if that move is possible
        # if (room.tiles[self.target[0]][self.target[1]].collision):
        #     pass