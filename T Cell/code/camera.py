from settings import *



class All_Sprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        # self.camera  =camera

    def draw(self,camera):
        for sprite in self:
            self.display_surface.blit(sprite.image,camera.apply(sprite))


