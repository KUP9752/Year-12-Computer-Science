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

# -- Font
font = pygame.font.Font('freesansbold.ttf',20)
bigfont = pygame.font.Font('freesansbold.ttf', 32)

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()


# -- Blank Screen

size = (500,560)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("PAC MAN")


# Maze Generation from json file
f = open('maze.json','rt')
maze = json.load(f)
f.close()

score = 0

    

# -- My Classes

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image= pygame.Surface([20,20])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Points(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface([2,2])
        self.image.fill(WHITE)
        self.rect =self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y

class PowerUp(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface([8,8])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
         
        
class Ghost(pygame.sprite.Sprite):
    def __init__(self,x,y,colour):
        super().__init__()
        self.image = pygame.Surface([12,12])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
##class B_Ghost(pygame.sprite.Sprite):
##    def __init__(self,x,y):
##        super().__init__()
##        self.image = pygame.Surface([12,12])
##        self.image.fill(AQUA)
##        self.rect = self.image.get_rect()
##        self.rect.x = x
##        self.rect.y = y


class PacMan(pygame.sprite.Sprite):
    def __init__(self,x,y, colour):
        super().__init__()
        self.speed = 2
        self.state = 0
        
        self.image = pygame.Surface([12,12])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction_x = 0
        self.direction_y=0

    def set_state(self,val):
        self.state = val
        if self.state == 1:
            self.image.fill(AQUA)
        elif self.state == 0:
            self.image.fill(YELLOW)
       
    def set_direction_x(self,val):
        
        self.direction_x = val


        
    def set_direction_y(self,val):
        self.direction_y = val

    def update(self):
        
        self.rect.x += self.direction_x*self.speed
        self.rect.y += self.direction_y*self.speed
        wall_hit_group = pygame.sprite.groupcollide(player_group,wall_group,False,False)

        for player in wall_hit_group:
            if self.direction_x == 1:
                self.rect.x-= self.speed*self.direction_x
            elif self.direction_x ==-1:
                self.rect.x -=self.speed*self.direction_x
            elif self.direction_y ==1:
                self.rect.y -= self.speed*self.direction_y
            elif self.direction_y ==-1:
                self.rect.y -=self.speed*self.direction_y
                
        

        if self.rect.y <=0 and (self.rect.x>=240 and self.rect.x<=260):
            self.rect.y = 490
        elif self.rect.y>=500 and (self.rect.x>=240 and self.rect.x<=260):
            self.rect.y = 0
        elif (self.rect.y>=240 and self.rect.y<=260) and self.rect.x<=0:
           self.rect.x =490
        elif (self.rect.y>=240 and self.rect.y<=260) and self.rect.x>=500:
            self.rect.x =0





#--Sprite groups
all_sprites_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
points_group = pygame.sprite.Group()
ghost_group = pygame.sprite.Group()
power_group = pygame.sprite.Group()

player = PacMan(245,305,YELLOW)

player_group.add(player)
all_sprites_group.add(player) 

ghostR = Ghost(245,250,RED)
ghost_group.add(ghostR)
all_sprites_group.add(ghostR)

#- Maze creation logic
for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] ==1:
            wall = Wall(x*20,y*20)
            all_sprites_group.add(wall)
            wall_group.add(wall)
            
        elif maze[y][x] == 0 and not((y>=11 and y<=13) and (x>= 10 and x <=15)):
            if (y == 1 and (x== 1 or x ==23)) or (y ==23 and x ==1) or (y ==22 and x ==23):
                powerUp = PowerUp(((x*20)+6),((y*20)+6))
                power_group.add(powerUp)
                all_sprites_group.add(powerUp)
            else:
                point = Points(((x*20)+8),((y*20)+8))
                points_group.add(point)
                all_sprites_group.add(point)
            
            
            
        
    
#next index

timer = 0
max_power = 4










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
    points_group.update()

    point_hit_group = pygame.sprite.groupcollide(player_group,points_group,False,True)
    power_hit_group = pygame.sprite.groupcollide(player_group,power_group,False,True)
    
    
    for elem in point_hit_group:
        score += 10
    #next elem
    for elem in power_hit_group:
        score += 100
        
    #next elem

    if len(power_group)<max_power:
        timer += 1
        
    if len(power_group)<max_power and timer <250:
        player.set_state(1)
        
    elif timer == 250:
        player.set_state(0)
        max_power -= 1
        timer = 0
        
    if player.state == 0:
        ghost_hit_group = pygame.sprite.groupcollide(player_group,ghost_group,True,False)
    #End if
    


    # -- Screen background is BLACK
    screen.fill(BLACK)
    # -- Text
    textScore = font.render('Score:' + str(score), False, WHITE)
    textScoreRect = textScore.get_rect()
    textScoreRect.center = (55,550)

    textPower = font.render('Usage of Power-Up:',False,GREEN)
    textPowerRect = textPower.get_rect()
    textPowerRect.center = (350, 550)

    textOver = bigfont.render('GAME OVER',False,RED)
    textOverRect = textOver.get_rect()
    textOverRect.center = (250,250)

    textLost = font.render('YOU LOST!',False, RED)
    textLostRect = textLost.get_rect()
    textLostRect.center = (250,280)

    textTime = font.render('None',False,RED)
    textTimeRect = textTime.get_rect()
    textTimeRect.center = (475,550)
    # -- Display text
    
    if len(points_group)+ len(power_group)<=0:
        all_sprites_group.empty()
        screen.blit(textOver,textOverRect)
        textScore = font.render('Your Score is: ' + str(score),False, BLUE)
        textScoreRect.center = (210, 280)
    elif len(player_group) == 0:
        all_sprites_group.empty()
        screen.blit(textOver,textOverRect)
        textScore = font.render('Your Score is: ' + str(score),False, BLUE)
        textScoreRect.center = (210,310)
        screen.blit(textLost,textLostRect)
    if len(power_group)<max_power:
        perc = int((100/250)*timer)
        textTime = font.render(str(perc)+'%',False,GREEN)
        

    screen.blit(textTime,textTimeRect)    
    screen.blit(textScore,textScoreRect)
    screen.blit(textPower,textPowerRect)
    # -- Draw here
    
    all_sprites_group.draw(screen)


    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()

##while not game_over:

