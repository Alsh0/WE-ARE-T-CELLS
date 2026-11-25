

from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
       
        self.image =pygame.image.load(join("art","player.png"))
        
        self.rect = self.image.get_frect(center = (WINDOW_WIDHT/2,400))
        self.direction = pygame.Vector2()
        self.speed = 300
        # mask

        self.mask = pygame.mask.from_surface(self.image)

    def input(self):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a]) or int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT]) 
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w]) or int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP]) 
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self,dt):
        self.rect.center += self.direction * dt * self.speed

        
    def update(self,dt):
            self.input()
            self.move(dt)
        