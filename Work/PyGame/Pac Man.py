### SRC - Nearly there, just need to fix the direction and add colour attribute.

import pygame
import random
import math
import json


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

size = (500,500)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("PAC MAN")


# Maze Generation from json file
f = open('maze.json','rt')
maze = json.load(f)
f.close()



    

# -- My Classes

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        #self.colour = BLUE
        #self.w= 20
        #self.h= 20
        self.image= pygame.Surface([20,20])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
##    def update(self):
##        self.rect.x = self.rect.x
##        self.rect.y = self.rect.y
##        
        




class PacMan(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.speed = 2
        self.surface = screen
        self.colour = YELLOW
        self.image = pygame.Surface([10,10])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction_x = 0
        self.direction_y=0
        

  
        

    def set_direction_x(self,val):
        
        self.direction_x = val


        
    def set_direction_y(self,val):
        self.direction_y = val

    def update(self):
        self.rect.x += self.direction_x*self.speed
        self.rect.y += self.direction_y*self.speed

        if self.rect.y <=0 and (self.rect.x>=240 and self.rect.x<=260):
            self.rect.y = 490
        elif self.rect.y>=500 and (self.rect.x>=240 and self.rect.x<=260):
            self.rect.y = 0
        elif (self.rect.y>=240 and self.rect.y<=260) and self.rect.x<=0:
           self.rect.x =490
        elif (self.rect.y>=240 and self.rect.y<=260) and self.rect.x>=500:
            self.rect.x =0
        



#Sprite groups
all_sprites_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()

player = PacMan(250,305)

for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] == 1:
            wall = Wall(x*20,y*20)
            wall_group.add(wall)
            all_sprites_group.add(wall)
            
        
    
#next index



all_sprites_group.add(player) 

game_over = False


### -- Game Loop
while not game_over:
    # -- User input and controls

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                player.set_direction_y(0)
                player.set_direction_x(-1)
            elif event.key == pygame.K_RIGHT:
                player.set_direction_y(0)
                player.set_direction_x(1)
            elif event.key == pygame.K_UP:
                player.set_direction_x(0)
                player.set_direction_y(-1)
            elif event.key == pygame.K_DOWN:
                player.set_direction_x(0)
                player.set_direction_y(1)
            #end if

    
                 
    # -- Game logic goes after this comment
    all_sprites_group.update()

    
    # -- Text
    font = pygame.font.Font('freesansbold.ttf',15)
        
    

    # -- Screen background is BLACK
    screen.fill(BLACK)
    # -- Display text
    
    # -- Draw here
    
    all_sprites_group.draw(screen)


    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()

##while not game_over:

