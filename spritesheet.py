
# File handles importing of textures as sprite for tiles and frames

import pygame
import json 

class SpriteSheet:
    def __init__(self,filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.meta_data = self.filename.replace("png","json")
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close

    def get_sprite(self,x,y,w,h):
        sprite = pygame.Surface((w,h),pygame.SRCALPHA)
        sprite.blit(self.sprite_sheet,(0,0),(x,y,w,h))
        return sprite

    def parse_sprite(self,name):
        sprite = self.data['frames'][name]['frame']
      
        x,y,w,h = sprite['x'],sprite['y'], sprite['w'],sprite['h']
        image = self.get_sprite(x,y,w,h)
        image = pygame.transform.scale(image,(96,96))
        return image