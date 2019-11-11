### SRC - Nearly there, just need to fix the direction and add colour attribute.

import pygame
import random

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
pygame.display.set_caption("My First Flipbook")


# -- My Classes

class Ball():
    def __init__(self, x, y, speed,num, x_direction, y_direction,colour):
        self.x = x
        self.y = y
        self.speed = speed
        self.num = num
        self.x_direction = x_direction
        self.y_direction = y_direction
        self.colour = colour

    def move(self):
        ### SRC - The problem here is that you only have one direction attribute...
        ### The ball can be moving +ve in x but -ve in y
        
        if self.x >= -1+rad[self.num] and self.x<= 641-rad[self.num]:
            
            self.x = self.x + (self.x_direction*self.speed)               
        else:
            self.x_direction = self.x_direction * -1
            self.x = self.x + (self.x_direction*self.speed)
            
        if self.y >= -1+rad[self.num] and self.y<= 481-rad[self.num]:
            
            self.y = self.y + (self.y_direction*self.speed)
        else:
            self.y_direction = self.y_direction * -1
            self.y = self.y + (self.y_direction*self.speed)

        
            
    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), rad[self.num], 0)
        
    
direction = [-1,1]            
balls = []
rad = []
for ball in range(0,10):
    rad.append(random.randint(8,24))
    balls.append(Ball(random.randint(rad[ball], 640-rad[ball]), random.randint(rad[ball], 480-rad[ball]), random.randint(1,5), ball, random.choice(direction),random.choice(direction),random.choice(COLOUR)))
#next ball

game_over = False

### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event
                 
    # -- Game logic goes after this comment
    for ball in balls:
        ball.move()
    
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
