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
    def __init__(self, x, y, speed,num, direction):
        self.x = x
        self.y = y
        self.speed = speed
        self.num = num
        self.direction = direction

    def move(self):
        if self.x == 0+rad[self.num] or self.x == 640-rad[self.num] or self.y== 0+rad[self.num] or self.y == 480-rad[self.num]:  
            self.direction = self.direction*-1
            self.x = self.x + (self.direction*self.speed)
            self.direction = self.direction*-1
            self.y = self.y + (self.direction*self.speed)
        else:
            self.x = self.x + self.direction*self.speed
            self.y = self.y + self.direction*self.speed
    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), rad[self.num], 0)
        
    
direction = [-1,1]            
balls = []
rad = []
for ball in range(0,5):
    rad.append(random.randint(8,24))
    balls.append(Ball(random.randint(rad[ball], 640-rad[ball]), random.randint(rad[ball], 480-rad[ball]), random.randint(1,10), ball, random.choice(direction)))
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
