import pygame
import time
import random as rd

pygame.init()
#Initialising the pygame modules.
pygame.display.set_caption('Do leave us a 5 star rating :)')

window = pygame.display.set_mode((500, 750))
#The dimension of the game window in pixels (width, length).

backgroundImage = pygame.image.load("./externals/flappyBirdBackground.jpg")
#Loads the background. This background conveniently has image dimensions 500px * 750px

flappyBird = pygame.image.load("./externals/flappyBird.png")
#Loads the flappy bird image. The image that I have chosen has dimensions 64px * 64px
flappyBird_X = 50
flappyBird_Y = 300
#Initial position of flappyBird
del_flappyBird_Y = 0
#As in flappy bird, the bird only moves along the Y axis.
#The del is short for delta, commonly used in calculus to indicate a small change.

def displayBird(x, y):
    window.blit(flappyBird, (x, y))
    #Displays the bird at the input arguments

obstacleWidth = 70
#Obstacle width in pixels
obstacleHeight = rd.randint(150, 400)
#To get a random obstacle height in [150, 400]
obstacleColour = (211, 253, 117)
#A light green colour
del_obstacleDist = -4
#Moving the obstacles towards the left of the window
obstacleDist = 500
#The obstacle starts at the 500th pixel. The right most pixel on the window.

def displayObstacle(height):
    pygame.draw.rect(window, obstacleColour, (obstacleDist, 0, obstacleWidth, height))
    #Drawing the top rectangle
    bottomObstacleHeight = 635 - height - 150
    #150 is the gap between the obstacles
    pygame.draw.rect(window, obstacleColour, (obstacleDist, 635, obstacleWidth, - bottomObstacleHeight))
    #Drawing the bottom obstacle, the negative height is because the obstacle starts at the bottom and goes up

def collisionDetection(obstacleDist, obstacleHeight, flappyBird_y, bottomObstacleHeight):
    if(obstacleDist >= 50 and obstacleDist <= (50 + 64)):
        #If the obstacle shares an x location with the 64pixel width bird
        if(flappyBird_y <= obstacleHeight or flappyBird_Y >= (bottomObstacleHeight - 64)):
            #If the obstacle shares a y location with the 64pixel height bird
            return True
    return False

score = 0
score_font = pygame.font.Font("freesansbold.ttf", 32)

def displayScore(score):
    window.blit(score_font.render(f"Score: {score}", True, (255, 0, 0)), (10, 10))
    #The displayed value changes everytime the score changes

startFont = pygame.font.Font("freesansbold.ttf", 32)

def startScreen():
    window.blit(startFont.render(f"PRESS SPACEBAR TO START", True, (255, 255, 255)), (15, 200))
    pygame.display.update()

play = True
#boolean expression needed to handle the while loop.
waiting = True
#Boolean expression to display start screen

while(play):
    window.fill((0, 0, 0))
    #The parameters are rgb values.
    #Fills the screen in black.

    window.blit(backgroundImage, (0,0))
    #Blit draws whatever you give it at the given pixel coordinate

    while(waiting):
        startScreen()

        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE):
                    waiting = False

    time.sleep(0.003)
    #So that the game doesn't run too fast to the point it's not fun

    for event in pygame.event.get():
        #Goes through every event in our pygame module.
        if(event.type == pygame.QUIT):
            #You exit from pygame.
            play = False
            #The condition for the while loop is now False, so it breaks.

        if(event.type == pygame.KEYDOWN):
            #checks for an event when a key is pressed
            if(event.key == pygame.K_SPACE):
                del_flappyBird_Y = -6
                #If the spacebar is pressed, flappy bird moves up by 6 pixels in the Y axis

        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_SPACE):
                del_flappyBird_Y = 3
                #Every "event" the spacebar isn't pressed, the bird falls down 3 pixels on the Y axis

    flappyBird_Y += del_flappyBird_Y

    if(flappyBird_Y <= 0):
        flappyBird_Y = 0
        #Defines the top boarder so that the bird doesn't translate out of frame
    if(flappyBird_Y >= 576):
        flappyBird_Y = 576
        #571 corresponds to the row of pixels which look like the floor in the image.
        #We want this to be our ground, not the bottom of the window.

    obstacleDist += del_obstacleDist
    if(obstacleDist <= -10):
        score += 1
        #If the bird passes the obstacle, score++
        obstacleDist = 500
        obstacleHeight = rd.randint(200, 400)
    displayObstacle(obstacleHeight)

    if(collisionDetection(obstacleDist, obstacleHeight, flappyBird_Y, obstacleHeight + 150)):
        pygame.quit()

    displayBird(flappyBird_X, flappyBird_Y)
    #Displays the bird at the new coordinates

    displayScore(score)
    #Displays the score

    pygame.display.update()
    #updates the display after every iteration of the while loop.

pygame.quit()
#quits the programme.
