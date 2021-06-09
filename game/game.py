

import pygame, random

pygame.init()


display_width = 800
display_height = 600
black =(0,0,0)


gameDisplay =  pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Save Svam beard")
clock = pygame.time.Clock()

backgrundImage = pygame.image.load("backgrundBatroom.png")
brijacImg = pygame.image.load("brijac.jpg")
svamImage = pygame.image.load("svam1.png")
svamImage1 = pygame.image.load("brijac.jpg")



def scoreTable(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Izbegnuto: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def brijac(brijacX,brijacY):
    gameDisplay.blit(brijacImg,(brijacX,brijacY))


def playerImage(x,y):
    gameDisplay.blit(svamImage,(x,y))

def game_loop():
    x = 50
    y = (display_height / 2)

    x_change = 0
    y_change = 0
    brijacX = 900
    brijacY = random.randrange(0, display_width)
    brijacImgHeight = brijacImg.get_size()[1]
    svamImageHeight = svamImage.get_size()[1]
    svamImageWidth = svamImage.get_size()[0]
    brijacX_speed = 10
    izbegnuto = 0

    crashed = False

    while not crashed:
        for event in pygame.event.get():  # rad nad eventovima u pygame
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5  # brzine po osama
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    x_change = 0



        brijacX -= brijacX_speed
        x += x_change
        y += y_change
        gameDisplay.blit(backgrundImage, (0, 0))
        brijac(brijacX, brijacY)
        playerImage(x, y)
        scoreTable(izbegnuto)

        if brijacX < -100:
            brijacX = 900
            brijacY = random.randrange(0, (display_height - 100))
            izbegnuto += 1
            brijacX_speed += 1


        if y > brijacY - brijacImgHeight and y < brijacY or y + svamImageHeight > brijacY and y - svamImageHeight < brijacY - brijacImgHeight :

                if x > brijacX - svamImageWidth:
                    brijacX = 900
                    brijacY = random.randrange(0, (display_height - 100))
                    gameDisplay.blit(svamImage1, (x, y))
        pygame.display.update()
        clock.tick(30)


game_loop()
pygame.quit()
quit()


