
import pygame, sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500,500))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()