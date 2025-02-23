

# File contains classes for tiles as well as title map creation

# Tile class creates basic tile and draw function
class Tile(pygame.sprite.Sprite):
    def __init__(self,image=None,x=0,y=0,spritesheet=None,groups=None,z=0):
        super().__init__(groups)
        self.image = spritesheet.parse_sprite(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.z = z

    def draw(self,surface):
        surface.blit(self.image,(self.rect.x,self.rect.y))