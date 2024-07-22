from settings import *
from sprites import Sprite


class Level:
    def __init__(self, tmx_map):
        self.display_surface = pygame.display.get_surface()

        self.setup(tmx_map)

        # groups
        self.all_sprites = pygame.sprite.Group()



    def setup(self, tmx_map):
        #for each position in the tile map we get x or y
        for x, y, surf in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x,y), surf, self.all_sprites)

    def run(self):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)

