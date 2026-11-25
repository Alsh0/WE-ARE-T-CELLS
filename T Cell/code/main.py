

from settings import *
from player import *
from camera import *
from sprites import *

from random import choice

# since I'm not pretty skilled I'm writing my camera code within this main file
# update I made the camera logic GG

# temporary

germ_positions = [
(0,0),
(WINDOW_WIDHT,600),
(0,WINDOW_HEIGHT),
(WINDOW_WIDHT,WINDOW_HEIGHT),
(WINDOW_WIDHT/2,WINDOW_HEIGHT),
(1000,1000)
]



class Camera():
    def __init__(self,width,height):
        self.camera = pygame.Rect(0,0,width,height)
        self.width = width
        self.height = height

    def apply(self,entity):
        return entity.rect.move(self.camera.topleft)   

    def update(self,target):
        x = -target.rect.x + (WINDOW_WIDHT//2)
        y = -target.rect.y + (WINDOW_HEIGHT//2)

        self.camera = pygame.Rect(x,y,self.width,self.height)






class Game():
    def __init__(self):
        # setup
        pygame.init()
        pygame.mixer.init()
        self.running = True
        
        self.clock = pygame.Clock()
        self.display_surface= pygame.display.set_mode((WINDOW_WIDHT,WINDOW_HEIGHT))
        pygame.display.set_caption('We are T cells!')


        # sprites and groups

        self.all_sprites = All_Sprites()
        self.germs = pygame.sprite.Group()
        self.UI = pygame.sprite.Group()
        self.organ_sprites = pygame.sprite.Group()
        # events
        self.germ_event = pygame.event.custom_type()
        self.germ_timer = pygame.time.set_timer(self.germ_event,600)
        # fonts and texts

        self.font = pygame.font.Font("freesansbold.ttf",16)
        self.pause_font = pygame.font.Font("freesansbold.ttf",34)

        # sounds
        self.germ_sound = pygame.mixer.Sound(join("sound","nom_nom.mp3")) # really annoying I guess I'll scrap the whole thing
        self.germ_death_sound = pygame.mixer.Sound(join('sound','death.mp3'))

        # simple pause mechanics
        self.paused = False


        self.setup()

    def input(self):
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_SPACE]:
            self.pause_game()



    def pause_game(self):
        self.paused = True

        while self.paused:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if pygame.K_RETURN:
                        self.paused = False
                        self.show_pause_screen()

        





       





    def show_score(self):
        self.score = (pygame.time.get_ticks()//100)
        text = self.font.render(f"SCORE: {self.score}",True,"white")
        text_rect = text.get_frect(center=(40,580))
        self.display_surface.blit(text,text_rect)

    def colisons(self):

        for germ in self.germs:
            for organ in self.organ_sprites:
                if germ.rect.colliderect(organ.hitbox) :       
                        if not self.health_bar.length <= 0:
                            germ.speed = 0
                            self.health_bar.length -= germ.damage
                        else:
                            self.running = False 

        player_germ_colisions = pygame.sprite.spritecollide(self.player,self.germs,True,pygame.sprite.collide_mask)

        if player_germ_colisions:
            self.germ_death_sound.play()

                


    def show_pause_screen(self):
        pause_text = self.pause_font.render('PAUSED',True,'White')
        pause_text_rect = pause_text.get_frect(center=(WINDOW_WIDHT/2,WINDOW_HEIGHT/2))

        if self.paused:
            self.display_surface.fill('black')
            self.display_surface.blit(pause_text,pause_text_rect)


    def spawn_organs(self):

        self.organs_positions = {
            "heart":(WINDOW_WIDHT/2,100),
            "liver":(200,300),
            "stomach":(600,300),
            "llung":(200,50),
            "rlung":(600,50)}
        
        self.targets = [(WINDOW_WIDHT/2,100),(WINDOW_WIDHT/2,100),(WINDOW_WIDHT/2,100),
                        (200,50),(200,50),(200,50),(200,50),(600,50),(600,50),(600,50),(600,50),(200,300),(600,300),(600,300)]
        # probablity stuff don't know If  did it right
        

        self.heart = Organ((self.all_sprites,self.organ_sprites),self.organs_positions['heart'],"heart")
        self.liver = Organ((self.all_sprites,self.organ_sprites),self.organs_positions['liver'],"liver")
        self.stomach = Organ((self.all_sprites,self.organ_sprites),self.organs_positions['stomach'],"stomach")
        self.R_lung = Organ((self.all_sprites,self.organ_sprites),self.organs_positions['rlung'],"right_lung")
        self.L_lung = Organ((self.all_sprites,self.organ_sprites),self.organs_positions['llung'],"left_lung")
        
        # look I could actually use nested-loops and modify some functions like the colisions and other func to get it to work but for later updates ;)
        # and these modification would increidibly reduce the memory useage




        

        






    def runGame(self):
        while self.running:

            dt = self.clock.tick()/1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == self.germ_event:
                    Germ((self.all_sprites,self.germs),self.targets,germ_positions)

            self.display_surface.fill('#4A0E17')

            # general sprite displaying using all_sprites group & camera
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.camera)
            self.camera.update(self.player)

            # UI displaying

            # fancy stuff
            health_bar_bg = pygame.Surface((500,16))
            HBR_rect = health_bar_bg.get_frect(center=(WINDOW_WIDHT/2,20))
            self.display_surface.blit(health_bar_bg,HBR_rect)
            # yeah I'll keep it black
            self.UI.draw(self.display_surface)
            self.UI.update(dt)
            self.input()
         
            self.show_score()
            self.colisons()
            pygame.display.update()

    def setup(self):


        # the health bar

        self.health_bar = HealthBar(self.UI)
       
        self.spawn_organs()

        # camera
        self.camera = Camera(WINDOW_WIDHT,WINDOW_HEIGHT)


        
        if self.health_bar.length == 10 :
            self.running = False

        

        # player
        self.player = Player(self.all_sprites)










if __name__ == '__main__':
    game = Game()
    game.runGame()