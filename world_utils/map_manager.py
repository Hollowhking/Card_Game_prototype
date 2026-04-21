import string
import os

from utils.config import Config
from world_utils.room import RoomObj
from world_utils.room_manager import RoomHandler
from entities.player import Player
from utils.tile_manager import TileManager
# This class will create the rooms 
# and handle which room the player is in on the map
# whenever a player enters a new room a new instance 
# of room manager is created
class Map_Manager:
    def __init__(self, config: Config, totalMap, player: Player, tileManager: TileManager):
        self.config = config

        self.tileManager = tileManager
        self.player = player
        self.currentRoom = RoomObj()
        self.currentRoomManager = None
        self.move_room("test")

    def move_room(self, room_str):
        self.currentRoom = RoomObj()
        self.currentRoomManager = RoomHandler(self.config, 
                                                self.player, 
                                                self.currentRoom, 
                                                self.tileManager)
        self.tileManager.load_room(room_str)

    def update(self):
        if (self._check_player_exit()):
            #determine what room to move to up down left right depending on player loc and current room val
            self.move_room("test2")
        self.currentRoomManager.update()

    def render(self, screen):
        self.currentRoomManager.render(screen)

    def _check_player_exit(self):
        #check player x,y and current room exit points
        return False