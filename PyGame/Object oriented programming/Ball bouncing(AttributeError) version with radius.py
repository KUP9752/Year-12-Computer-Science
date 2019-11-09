import pygame
import random

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


# -- My Classes

class Ball():
    def __init__(self, radius, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius
        

    #def move(self):
        

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius, 0)
        


game_over = False

balls = []
for ball in range(0,5):
    balls.append(Ball(random.randint(8,24),random.randint(ball.radius, 640-ball.radius), random.randint(ball.radius, 480-ball.radius), random.randint(1,10)))
#next ball


### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event

            
            
    # -- Game logic goes after this comment
##    for ball in balls:
##        ball.move()        
    # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    for ball in balls:
        ball.draw()
    # Make the mouse pointer appear in the middle of the square...
    


    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
