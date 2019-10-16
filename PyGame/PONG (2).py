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
pygame.display.set_caption("PONG 2.0")


#//displaying text on the screen
font = pygame.font.Font("freesansbold.ttf",32)
text = font.render("Game Over", True, RED, WHITE)
textRect = text.get_rect()
textRect.center = (320, 240)




game_over = False
game_end = 0
block_x = 4
block_y = size[1]//2

speed = 5
direction_x = 0
direction_y = 0

cpu_speed = 0



cpu_block_x = 640-(4+8)
cpu_block_y = size[1]//2

circ_x = 320
circ_y = 240

Cdir_x = 4
Cdir_y = 4

ball_speed = 2

hp_left= 3

score_1=0   #//score of PLAYER 1
### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            game_end = 1
                           
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
 
    #If cpu_speed!=0:
     #//Cpu paddle movement and calculations (+20 for centering the paddle) 
        if cpu_block_y+20 > circ_y:
            cpu_block_y = cpu_block_y + cpu_speed *-1
        elif cpu_block_y+20 < circ_y:
            cpu_block_y = cpu_block_y + cpu_speed * 1
        #end if 
            
        if circ_x == cpu_block_x-8 and (circ_y<=cpu_block_y+40 and circ_y>=cpu_block_y):
            Cdir_x = Cdir_x * -1
            circ_x = circ_x + (Cdir_x*ball_speed)
            
        if circ_x ==640-8:
            score_1 +=1
        #end if


            
        #//PLAYER 1 paddle movement and calculations
        if block_y <0:
            block_y = 0
        elif block_y > 440:
            block_y = 440
        else:
            block_y = block_y + direction_y * speed
        #end if
            
        if circ_x == 0 +8:
            hp_left = hp_left - 1
        #end if
            
        if circ_x == block_x+8+8 and (circ_y<=block_y+40 and circ_y>=block_y):
            Cdir_x = Cdir_x * -1
            circ_x = circ_x + (Cdir_x*ball_speed)
            
        

            
        elif circ_x == 0 + 8 or circ_x==640 - 8: 
            circ_x = 320            #//variables reset so that game restarts
            circ_y = 240
            direction_x = 0
            direction_y = 0
            Cdir_x = 4
            Cdir_y = 4
            
            
            
            if hp_left == 0:
                game_over = True    #//ends game after losing 3 times
                screen.blit(text, textRect)
                pygame.display.update()
                print("Score of PLAYER 1:",score_1)
                enter_name = input("Please enter your name for the scoreboard")
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
    else:
        cpu_speed= int(input("Please enter the CPU speed you want (Higher speed, Higher difficulty)"))
        
    # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    pygame.draw.rect(screen, WHITE, (block_x, block_y, 8, 40))
    pygame.draw.rect(screen, BLUE, (cpu_block_x, cpu_block_y, 8, 40))
    pygame.draw.circle(screen, RED, (circ_x, circ_y), 8, 0)


    # Make the mouse pointer appear in the middle of the square...
        # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop
if game_over ==True and game_end == 1:
    pygame.quit()
#end if
    
while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #end if
    #next event
#end while

