from settings import *
from random import randint
# so the file name is germ but I'm changing it to sprites 


class Germ(pygame.sprite.Sprite):
    def __init__(self,groups,targets,positions):
        super().__init__(groups)
        self.positions = positions
        self.type = choice(['germ1.png','germ2.png','germ3.png'])
        self.image = pygame.image.load(join('art',self.type))
        self.rect = self.image.get_frect(center=self.Respawn())
        self.hitbox = self.rect.inflate(-100,-100)

        # 
        self.speed = 140
        self.direction = pygame.Vector2()
        self.targets = targets
        # damage
        self.damage = 0.02
        # mask
        self.mask = pygame.mask.from_surface(self.image)

        


    def Respawn(self):        
        return choice(self.positions)

        

    def Find_target(self):
       
       target = choice(self.targets)
       organ_pos = pygame.Vector2(target)
       germ_pos = pygame.Vector2(self.rect.center)
       self.direction = pygame.Vector2(organ_pos-germ_pos).normalize()


    
       

    def move(self,dt):
        self.Find_target()
        self.rect.center += self.direction * dt* self.speed 

    def update(self,dt):
        self.move(dt)



class HealthBar(pygame.sprite.Sprite):
    def __init__(self,groups,):
        super().__init__(groups)
        self.length = 500
        self.image = pygame.Surface((self.length,12))
        self.image.fill('#0E4A41')
        self.rect = self.image.get_frect(center=(WINDOW_WIDHT/2,20))


    def update(self,dt):
            self.image = pygame.Surface((self.length,12))
            self.image.fill('#0E4A41')
       





class Organ(pygame.sprite.Sprite):
    def __init__(self,groups,position,name):
        super().__init__(groups)

        self.position = position
        self.image = pygame.image.load(join('art',name+".png"))
        self.image = pygame.transform.scale(self.image,(200,200))
    


        self.rect = self.image.get_frect(center=(self.position))
        self.hitbox = self.rect.inflate(-30,-30)
        # mask
        self.mask = pygame.mask.from_surface(self.image)

    