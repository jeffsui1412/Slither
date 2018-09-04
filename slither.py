import pygame
import random

pygame.init()

display_width = 800
display_height = 600
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
block_color = (53,115,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

pause = False

def quitgame():
    pygame.quit()
    quit()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_point(points):
    font = pygame.font.SysFont("comicsansms", 30)
    text = font.render("Game Points: " + str(points), True, black)
    gameDisplay.blit(text, (0, 0))

def snake_block(color, x, y, w, h):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])

def apple(color, x, y, w, h):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])

def apple_ran():
    return 20 * random.randint(3, 29)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 100)
        TextSurf, TextRect = text_objects("A Snake Game", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(40)

def unpause():
    global pause
    pause = False

def crashed():
    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 100)
        TextSurf, TextRect = text_objects("---- Game Over ---- ", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        button("Play Again!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(40)

def pause():
    largeText = pygame.font.SysFont("comicsansms", 90)
    TextSurf, TextRect = text_objects("You have paused ", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    while pause:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        button("Keep playing!",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(40)

def game_loop():
    global pause
    fps = 11
    snake_width = 20
    snake_x = 0
    snake_y = 0
    snake_body = [[80, 100], [80, 120], [80, 140], [80, 160]]
    x_change = snake_width
    y_change = 0
    apple_width = 20

    apple_x = apple_ran()
    apple_y = apple_ran()

    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
    dir = RIGHT

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    pause()
                if event.key == pygame.K_a:
                    if dir != 2:
                        x_change = -snake_width
                        y_change = 0
                        dir = LEFT
                if event.key == pygame.K_d:
                    if dir != 4:
                        x_change = snake_width
                        y_change = 0
                        dir = RIGHT
                if event.key == pygame.K_s:
                    if dir != 1:
                        y_change = snake_width
                        x_change = 0
                        dir = DOWN
                if event.key == pygame.K_w:
                    if dir != 3:
                        y_change = -snake_width
                        x_change = 0
                        dir = UP

        snake_x = x_change + snake_body[0][0]
        snake_y = y_change + snake_body[0][1]
        points = len(snake_body)-4
        s_block = [snake_x, snake_y]
        eat = False
        #white game display
        gameDisplay.fill(white)

        #add head
        snake_body.insert(0, s_block)

        #blit snake body
        for each in snake_body:
            snake_block(red, each[0], each[1], snake_width, snake_width)

        #check wall
        if snake_body[0][0] < 0 or snake_body[0][0] > display_width - snake_width or snake_body[0][1] < 0 or snake_body[0][1] > display_height - snake_width:
            crashed()

        #check apple
        if snake_body[0][0] == apple_x and snake_body[0][1] == apple_y:
            apple_x = apple_ran()
            apple_y = apple_ran()
            eat = True
        #check snake body
        if snake_body[0] in snake_body[1:]:
            crashed()

        #remove tail
        if not eat:
            snake_body.pop()
        #add apple
        apple(green, apple_x, apple_y, apple_width, apple_width)

        #show text
        game_point(points)

        pygame.display.update()
        clock.tick(fps)

game_intro()
