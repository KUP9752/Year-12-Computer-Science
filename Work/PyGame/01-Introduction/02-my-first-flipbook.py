import pygame
import pygame.gfxdraw
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
GREY =(128,128,128)
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

circle_x_pos, circle_y_pos= 0, 150

### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event
            
    # -- Game logic goes after this comment
    if circle_x_pos < 600:
        circle_x_pos = circle_x_pos + 1
        circle_y_pos = int(round((1/500)*(circle_x_pos -320)**2+40))
    
    else:
        circle_x_pos = 40
        circle_y_pos = 100
    
    # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    pygame.draw.rect(screen, YELLOW, (200, 200, 50, 50), 0)
    pygame.draw.rect(screen, BLUE, (220,165,200,150))
    pygame.draw.circle(screen, YELLOW, (circle_x_pos, circle_y_pos),40,0)
    pygame.draw.aaline(screen, WHITE, (300,300), (600,450))
    pygame.gfxdraw.pie(screen,100,200,100,55, 125, GREY)

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
