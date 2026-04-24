import pygame
import os
from pathlib import Path

from utils.config import Config
from utils.logger import Logger
from world_utils.room import RoomObj
class Tile:
    def __init__(self, image=None, collision=False, distructable=False):
        self.image        = image
        self.collision    = collision
        self.distructable = distructable
    
    def get_image(self):
        return self.image

#=====================

#=====================

class TileManager:
    def __init__(self, config: Config):
        self.config = config
        self.tiles_array = [None] * config.num_tile_options
        self.map_tile_num = [[1 for _ in range(self.config.game_Map_Area_Width)] for _ in range(self.config.game_Map_Area_Height)]

        self.logger = Logger(self.config)
        self.get_Tile_Images()
    
    def get_Tile_Images(self):
        ROOT_DIR = Path(__file__).resolve().parent.parent
        try:
            background_Tile_Set_str = ROOT_DIR / self.config.tile_directory / "CobbleStone-sheet.png"
            background_Tile_Set_img = pygame.image.load(str(background_Tile_Set_str)).convert_alpha()

            tile_image   = background_Tile_Set_img.subsurface(pygame.Rect(0, 0, self.config.base_tile_size, self.config.base_tile_size))
            scaled_image = pygame.transform.scale(tile_image, (self.config.tile_size, self.config.tile_size))
            self.tiles_array[0] = Tile(scaled_image, True, False)

            #Void Tile:
            tile_image   = background_Tile_Set_img.subsurface(pygame.Rect((self.config.base_tile_size * 3), 0, self.config.base_tile_size, self.config.base_tile_size))
            scaled_image = pygame.transform.scale(tile_image, (self.config.tile_size, self.config.tile_size))
            self.tiles_array[3] = Tile(scaled_image, True, False)


            #CobbleStone:
            tile_image   = background_Tile_Set_img.subsurface(pygame.Rect((self.config.base_tile_size * 4), 0, self.config.base_tile_size, self.config.base_tile_size))
            scaled_image = pygame.transform.scale(tile_image, (self.config.tile_size, self.config.tile_size))
            self.tiles_array[4] = Tile(scaled_image, True, False)


            #GRASS
            tile_image   = background_Tile_Set_img.subsurface(pygame.Rect((self.config.base_tile_size * 5), 0, self.config.base_tile_size, self.config.base_tile_size))
            scaled_image = pygame.transform.scale(tile_image, (self.config.tile_size, self.config.tile_size))
            self.tiles_array[5] = Tile(scaled_image, False, False)

            tile_image   = background_Tile_Set_img.subsurface(pygame.Rect((self.config.base_tile_size * 6), 0, self.config.base_tile_size, self.config.base_tile_size))
            scaled_image = pygame.transform.scale(tile_image, (self.config.tile_size, self.config.tile_size))
            self.tiles_array[6] = Tile(scaled_image, False, False)

        except IOError:
            print("Tilemap load not found at ", background_Tile_Set_str)

    def load_room(self, map_code:str):
        ROOT_DIR = Path(__file__).resolve().parent.parent
        file_name = ROOT_DIR / self.config.map_directory / f"{map_code}.txt"
        
        line_count = 0
        char_count = 0
        with open(file_name) as f:
            lines = f.read().splitlines()

        for line in lines:
            for char in line.split(' '):
                self.map_tile_num[line_count][char_count] = char
                char_count += 1
            char_count  = 0
            line_count += 1


    def render(self, screen: pygame.Surface):
        for row in range(self.config.game_Map_Area_Height):
            for col in range(self.config.game_Map_Area_Width):
                tile_index = self.map_tile_num[row][col]
                tile = self.tiles_array[int(tile_index)]

                tile_x = (col * self.config.tile_size)
                tile_y = (row * self.config.tile_size) + self.config.game_Map_Starting_Y

                #double check it has an image val:
                if (tile.get_image()):
                    screen.blit(tile.get_image(), (tile_x, tile_y))
                

    def get_map(self):
        return self.map_tile_num