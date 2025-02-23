
import pygame
from spritesheet import SpriteSheet
from Tiles import TileMap

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface():
        self.setup()

    def setup(self):
        file = SpriteSheet("tiles.png")
        #load tilemap using spritesheet set
        #self.map = TileMap('tile_map.csv',file,groups=self.all_sprites)