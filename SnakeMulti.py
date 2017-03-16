import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

display_width = 1200
display_height = 1000

block_size = 20
fps = 10
font = pygame.font.SysFont("arialback", 50)
smallfont = pygame.font.SysFont("arialblack", 25)
largefont = pygame.font.SysFont("arialblack", 80)
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Snake")

img = pygame.image.load("snakeHead.png")

icon = pygame.image.load("Snake-Pixel2.png")
pygame.display.set_icon(icon)

def snake(block_size, snakelist, slot):
    if slot == 1:
        color = white
    elif slot == 2:
        color = blue
    elif slot == 3:
        color = blue
    elif slot == 4:
        color = blue
    elif slot == 5:
        color = blue
    gameDisplay.blit(img, (snakelist[-1] [0], snakelist[-1] [1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, color, [XnY[0], XnY[1],block_size,block_size])

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = font.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return  textSurface, textSurface.get_rect()
        
def message(msg, color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(textSurf, textRect)

def startScreen():
    gameDisplay.fill(black)
    intro = True
    while intro:
        message("Snake",red,-70,"large")
        message("Use arrows to move and collect apples",red,0,"medium")
        message("Press any button to continue",red,50,"small")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    gameExit = True
            if event.type == pygame.KEYDOWN:
                        intro = False
        pygame.display.update()
    
"""def applePoz(snakeList):
    randAppleX = round(random.randrange(0, display_width-block_size)/20.0)*20.0
    randAppleY = round(random.randrange(0, display_height-block_size)/20.0)*20.0
    appleList  = [randAppleX, randAppleY]
    if appleList in snakeList:
         applePoz(snakeList)
    else:
        return appleList"""

def gameLoop():
    slot = 1
    #sprawdz czy jest wolny slot
    #jesli nie wypisz wolne sloty
    global direction
    start=0
    snakeList = []
    snakeList2 = []
    snakeList3 = []
    snakeList4 = []
    snakeList5 = []
    snakeLenght = 3
    #wylosuj spawn poz
    #losuj az trafi na wolne miejsce
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    gameExit = False
    gameOver = False
    
    randAppleX = round(random.randrange(0, display_width-block_size)/20.0)*20.0
    randAppleY = round(random.randrange(0, display_height-block_size)/20.0)*20.0


    #zapis pozycji do pliku
    #odcczyt pozycji innych graczy
    #zapis pozycji jablka
    
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(black)
            message("Game Over", red, -50,"large")
            message("Score: "+str(snakeLenght-3), red, 50, size = "medium")
            message("Game Over, press C to play again or Q to quit", red, 100, size="small")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameLoop()
                    elif event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                start = 1
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
        if lead_x == randAppleX and lead_y == randAppleY:
            
            randAppleX = round(random.randrange(0, display_width-block_size)/20.0)*20.0
            randAppleY = round(random.randrange(0, display_height-block_size)/20.0)*20.0
            snakeLenght += 1
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY,block_size,block_size])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLenght:
            del snakeList[0]
        if start != 0:
            if snakeHead in snakeList[:-1] or snakeHead in snakeList2 or snakeHead in snakeList3 or snakeHead in snakeList4 or snakeHead in snakeList5:
                gameOver = True

        snake(block_size, snakeList, slot)
        
        pygame.display.update()

        #zapis pozycji do pliku
        #odcczyt pozycji innych graczy
        
        clock.tick(fps)
        
    pygame.quit()
    quit()

startScreen()
#gameLoop(slot, password)
gameLoop()
