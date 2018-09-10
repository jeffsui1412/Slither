import pygame
import random

pygame.init()

display_width = 800
display_height = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
block_color = (53, 115, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

snake_body = [[80, 100], [80, 120], [80, 140], [80, 160]]

paused = False


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
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def game_point(points, x, y, text):
    font = pygame.font.SysFont("comicsansms", 30)
    text = font.render(text + str(points), True, black)
    gameDisplay.blit(text, (x, y))


def snake_block(color, x, y, w, h):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])

def apple(color, x, y, w, h):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])

def apple_ran():
    return 20 * random.randint(3, 29)

def crashed():
    global snake_body
    global highest_point
    largeText = pygame.font.SysFont("comicsansms", 80)
    TextSurf, TextRect = text_objects("---- Game Over ---- ", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    high(len(snake_body) - 4)
    game_point(len(snake_body)-4, 0, 0, "Game Points: ")
    game_point((highest_point), 0, 40, "Highest Game Score: ")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Play Again!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(40)

def high(point):
    global highest_point
    if highest_point <= point:
        highest_point = point
        with open("point.txt", "w") as file:
            file.write(str(highest_point))

def pause():
    largeText = pygame.font.SysFont("comicsansms", 90)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Keep playing!",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(40)

def unpause():
    global paused
    paused = False

def quitgame():
    pygame.quit()
    quit()

<<<<<<< HEAD
=======
def settings():
    global left
    largeText = pygame.font.SysFont("comicsansms", 90)
    TextSurf, TextRect = text_objects("Setttings", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    while True:
        mouse_pos = pygame.mouse.get_pos()

        gameDisplay.fill(white)
        gameDisplay.blit(TextSurf, TextRect)

        button1 = pygame.Rect(200, 200, 100, 100)
        pygame.draw.rect(gameDisplay, green, button1)

        if button1.collidepoint(mouse_pos):
            print("mouse over button1")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(10)
>>>>>>> ba34160a13e3f8179dd1e6ee7b6e1085318a5c7a

def game_intro():
    intro = True
    gameDisplay.fill(white)
    largeText = pygame.font.SysFont("comicsansms", 100)
    TextSurf, TextRect = text_objects("Snake Game", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    settings()
        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(40)

def game_loop():
    global paused
    global highest_point
    global snake_body
    global left
    snake_body = [[80, 100], [80, 120], [80, 140], [80, 160]]
    fps = 11
    snake_width = 20
    snake_x = 0
    snake_y = 0
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

    #open file
    file = open("point.txt", "r")
    file_num = file.read()
    highest_point = int(file_num)
    #close file
    file.close()

    while True:
        count = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pause()
                if event.key == left:
                    if dir != 2:
                        if count:
                            x_change = -snake_width
                            y_change = 0
                            count = False
                            dir = LEFT
                if event.key == pygame.K_d:
                    if dir != 4:
                        if count:
                            x_change = snake_width
                            y_change = 0
                            count = False
                            dir = RIGHT
                if event.key == pygame.K_s:
                    if dir != 1:
                        if count:
                            y_change = snake_width
                            x_change = 0
                            count = False
                            dir = DOWN
                if event.key == pygame.K_w:
                    if dir != 3:
                        if count:
                            y_change = -snake_width
                            x_change = 0
                            count = False
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

        #check apple
        if snake_body[0][0] == apple_x and snake_body[0][1] == apple_y:
            apple_x = apple_ran()
            apple_y = apple_ran()
            eat = True

        #remove tail
        if not eat:
            snake_body.pop()

        #blit snake body
        for each in snake_body:
            snake_block(red, each[0], each[1], snake_width, snake_width)

        #check wall
        if snake_body[0][0] < 0 or snake_body[0][0] > display_width - snake_width or snake_body[0][1] < 0 or snake_body[0][1] > display_height - snake_width:
            crashed()

        #check snake body
        if snake_body[0] in snake_body[1:]:
            crashed()

        #add apple
        apple(green, apple_x, apple_y, apple_width, apple_width)

        #show point
        game_point(points, 0, 0, "Game Points: ")
        game_point(highest_point, 0, 40, "Highest Game Score: ")
        pygame.display.update()
        clock.tick(fps)

settings()
