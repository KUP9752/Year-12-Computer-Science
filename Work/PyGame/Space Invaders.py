### SRC - Nearly there, just need to fix the direction and add colour attribute.

import pygame
import random
import math

# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (46,204,113)
ORANGE = (211,84,0)
PURPLE = (125,60,152)
AQUA = (22,160,133)
PINK = (255,89,222)
COLOUR = [WHITE,BLUE,YELLOW,RED,GREEN,ORANGE,PURPLE,AQUA,PINK]

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()


# -- Blank Screen

size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Space Invaders")


# -- My Classes

        
class Invader(pygame.sprite.Sprite):
    def __init__(self,colour, width,height,speed,):
        super().__init__()
        self.speed = speed
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,640)
        self.rect.y = random.randrange(-50,0)

    def update(self):
        self.rect.y = self.rect.y + self.speed
        
class Player(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
       super().__init__()
       self.bullet_count = 10
       self.speed = 0
       self.image = pygame.Surface([width,height])
       self.image.fill(colour)
       self.rect = self.image.get_rect()
       self.rect.x = 320
       self.rect.y = (480-height)
       
    def bullet_decrease(self):
        self.bullet_count -= 1
        
    def player_set_speed(self,val):
        self.speed = val
        
    def update(self):
        self.rect.x += self.speed
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__()
        self.speed = -10
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 3 
        self.rect.y = player.rect.y

    def update(self):
        self.rect.y += self.speed
        
class Wall(pygame.sprite.Sprite):
    def __init__(self,colour,x,y):
        super().__init__()
        self.image = pygame.Surface([1,480])
        self.rect = self.image.get_rect()
        self.image.fill(colour)
        self.rect.x = x
        self.rect.y = y
    
       
        
       
       

    
            
   
#Sprite Groups

all_sprites_group = pygame.sprite.Group()
invader_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
wall_group =pygame.sprite.Group()

#set walls
wall = Wall(RED,-1,0)
wall1 = Wall(RED, 641,0)
wall_group.add(wall)
wall_group.add(wall1)
all_sprites_group.add(wall)
all_sprites_group.add(wall1)
#add player
player = Player(YELLOW,10,10)
all_sprites_group.add(player)

#add 10 invaders
for i in range(10):
    invader = Invader(AQUA,10,10,1) #10px x 10px
    invader_group.add(invader)
    all_sprites_group.add(invader)
#next i



game_over = False


### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.player_set_speed(-5)
            elif event.key == pygame.K_RIGHT:
                player.player_set_speed(5)
            elif event.key == pygame.K_SPACE:
                if player.bullet_count !=0:
                    bullet = Bullet(RED,6,4)
                    bullet_group.add(bullet)
                    all_sprites_group.add(bullet)
                    player.bullet_decrease()
                else:
                    print("no bullets left")
                    
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.player_set_speed(0)
        #End If
    
                 
    # -- Game logic goes after this comment
    all_sprites_group.update()
    bullet_hit_group = pygame.sprite.groupcollide(bullet_group,invader_group,True,True)
    player_hit_group = pygame.sprite.spritecollide(player,invader_group,True)
    
    
    # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    all_sprites_group.draw(screen)

    


    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(30)

#End While - End of game loop

pygame.quit()

##while not game_over:

