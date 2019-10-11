import pygame
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()


# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My First Flipbook")

game_over = False
block_x = 4
block_y = size[1]//2

speed = 5
direction_x = 0
direction_y = 0

circ_x = 320
circ_y = 240

Cdir_x = 4
Cdir_y = 4

hp_left= 3
### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
                            
        ### -- Keys are also game logic -- ###
                
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction_y = -1
            elif event.key == pygame.K_DOWN:
                direction_y = 1
            
        elif event.type == pygame.KEYUP:
            direction_x, direction_y = 0, 0
            
            #End If
        #End If
    #Next event

            
    # -- Game logic goes after this comment




    
    block_y = block_y + direction_y * speed
    if circ_x == 12+8 and (circ_y<=block_y+40 and circ_y>=block_y):
        Cdir_x = Cdir_x * -1
        circ_x = circ_x + (Cdir_x*2)
    elif circ_x == 0 + 8: 
        circ_x = 320            #//variables reset so that game restarts
        circ_y = 240
        direction_x = 0
        direction_y = 0
        Cdir_x = 4
        Cdir_y = 4
        
        hp_left = hp_left -1
        
        if hp_left == 0:
            game_over = True    #//ends game after losing 3 times
        #end if  
    else:
        if circ_x != 0+8 and circ_x != 640-8:
            circ_x = circ_x + Cdir_x
        else:
            Cdir_x = Cdir_x * -1
            circ_x = circ_x + (Cdir_x*2)
        #end if
        if circ_y != 0 + 8 and circ_y != 480-8:
            circ_y = circ_y + Cdir_y
        else:
            Cdir_y = Cdir_y * -1
            circ_y = circ_y+ (Cdir_y*2)
        #end if
    #end if

        
    # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    pygame.draw.rect(screen, WHITE, (block_x, block_y, 8, 40))
    pygame.draw.circle(screen, RED, (circ_x, circ_y), 8, 0)


    # Make the mouse pointer appear in the middle of the square...
        # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
