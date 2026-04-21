import string

# ROOMs should be a txt file with a tile array followed by an array of enemys and their locations
class RoomObj:
    def __init__(self):
        self.tiles_array = []

        # 2D array that contains a enemy ID and a x,y coords for summoning it on load
        self.enemy_spawn_array = []

    def load_tile_map(self, file_loc: string):
        pass

    def loadRoom(self):
        pass
        #this should return a room obje