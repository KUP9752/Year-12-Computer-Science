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

        

class Wall(pygame.sprite.Sprite):
    def __init__():
        




class PacMan(pygame.sprite.Sprite):
    def __init__(self,colour):
        super().__init__()
    
        






    
game_over = False


### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
               
            elif event.key == pygame.K_RIGHT:

            elif event.key == pygame.K_UP:

            elif event.key == pygame.K_DOWN:

            #end if
        elif event.type == pygame.KEYUP:
            
                
        #End If
    
                 
    # -- Game logic goes after this comment
    all_sprites_group.update()
    bullet_hit_group = pygame.sprite.groupcollide(bullet_group,invader_group,True,True)
    player_hit_group = pygame.sprite.spritecollide(player,invader_group,True)
    
    # -- Text
    font = pygame.font.Font('freesansbold.ttf',15)
    textBullets = font.render('Bullets:' + str(player.get_bullet_count()
                                               ) ,False,WHITE)
    textLives = font.render('Lives:' + str(player.get_lives()),False,WHITE)
    textLivesRect = textLives.get_rect()
    textLivesRect.center = (50,30)
    textRect = textBullets.get_rect()
    textRect.center = (50,50)
    bigfont = pygame.font.Font('freesansbold.ttf',32)
    noBullets =bigfont.render('No Bullets Left',False,RED)
    noBulletRect = noBullets.get_rect()
    noBulletRect.center = (320,200)
    
    

    # -- Screen background is BLACK
    screen.fill (BLACK)
    # -- Display text
    screen.blit(textBullets,textRect)
    screen.blit(textLives, textLivesRect)
    if player.bullet_count ==0:
        screen.blit(noBullets,noBulletRect)
    # -- Draw here
    all_sprites_group.draw(screen)

    


    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()

##while not game_over:

