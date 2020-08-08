import pygame
import time
import random as rd

pygame.init()
pygame.display.set_caption('Do leave us a 5 star rating :)')

window = pygame.display.set_mode((500, 750))

backgroundImage = pygame.image.load("./externals/flappyBirdBackground.jpg")

flappyBird = pygame.image.load("./externals/flappyBird.png")
flappyBird_X = 50
flappyBird_Y = 300
del_flappyBird_Y = 0

def displayBird(x, y):
    window.blit(flappyBird, (x, y))

obstacleWidth = 70
obstacleHeight = rd.randint(150, 400)
obstacleColour = (211, 253, 117)
del_obstacleDist = -4
obstacleDist = 500

def displayObstacle(height):
    pygame.draw.rect(window, obstacleColour, (obstacleDist, 0, obstacleWidth, height))
    bottomObstacleHeight = 635 - height - 150
    pygame.draw.rect(window, obstacleColour, (obstacleDist, 635, obstacleWidth, - bottomObstacleHeight))

def collisionDetection(obstacleDist, obstacleHeight, flappyBird_y, bottomObstacleHeight):
    if(obstacleDist >= 50 and obstacleDist <= (50 + 64)):
        if(flappyBird_y <= obstacleHeight or flappyBird_Y >= (bottomObstacleHeight - 64)):
            return True
    return False

score = 0
score_font = pygame.font.Font("freesansbold.ttf", 32)

def displayScore(score):
    window.blit(score_font.render(f"Score: {score}", True, (255, 0, 0)), (10, 10))

startFont = pygame.font.Font("freesansbold.ttf", 32)

def startScreen():
    window.blit(startFont.render(f"PRESS SPACEBAR TO START", True, (255, 255, 255)), (15, 200))
    pygame.display.update()

play = True
waiting = True

while(play):
    window.fill((0, 0, 0))

    window.blit(backgroundImage, (0,0))

    while(waiting):
        startScreen()

        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE):
                    waiting = False

    time.sleep(0.003)

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            play = False

        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE):
                del_flappyBird_Y = -6

        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_SPACE):
                del_flappyBird_Y = 3

    flappyBird_Y += del_flappyBird_Y

    if(flappyBird_Y <= 0):
        flappyBird_Y = 0
    if(flappyBird_Y >= 576):
        flappyBird_Y = 576

    obstacleDist += del_obstacleDist
    if(obstacleDist <= -10):
        score += 1
        obstacleDist = 500
        obstacleHeight = rd.randint(200, 400)
    displayObstacle(obstacleHeight)

    if(collisionDetection(obstacleDist, obstacleHeight, flappyBird_Y, obstacleHeight + 150)):
        pygame.quit()

    displayBird(flappyBird_X, flappyBird_Y)

    displayScore(score)

    pygame.display.update()

pygame.quit()
