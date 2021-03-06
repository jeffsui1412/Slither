import pygame
from pygame.locals import *
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

BUTTON_W = 200
BUTTON_H = 60

class Button:
    
    family = []

    def __init__(self, x, y, w, h, ac_color, ic_color, key, index):
        self.ac_color = ac_color
        self.ic_color = ic_color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.key = key
        self.index = index
        __class__.family.append(self)

    def show(self):
        mouse = pygame.mouse.get_pos()
        button = pygame.Rect(self.x, self.y, self.w, self.h)
        if button.collidepoint(mouse):
            pygame.draw.rect(gameDisplay, self.ac_color, button)
            self.word()
            return True
        else:
            pygame.draw.rect(gameDisplay, self.ic_color, button)
            self.word()


    def word(self):
        TEXTS = ("Up", "Down", "Right", "Left")
        smallText = pygame.font.SysFont("comicsansms", 45)
        TitleSurf, TitleRect = text_objects(TEXTS[self.index] + ' : ' + str(self.key), smallText)
        TitleRect.center = (self.x+(self.w/2), self.y+(self.h/2))
        gameDisplay.blit(TitleSurf, TitleRect)

class BackButton:
    def __init__(self, x, y, w, h, ac_color, ic_color, text):
        self.ac_color = ac_color
        self.ic_color = ic_color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text

    def show(self):
        mouse = pygame.mouse.get_pos()
        button = pygame.Rect(self.x, self.y, self.w, self.h)
        if button.collidepoint(mouse):
            pygame.draw.rect(gameDisplay, self.ac_color, button)
            self.word()
            return True
        else:
            pygame.draw.rect(gameDisplay, self.ic_color, button)
            self.word()


    def word(self):
        smallText = pygame.font.SysFont("comicsansms", 30)
        TitleSurf, TitleRect = text_objects(self.text,smallText)
        TitleRect.center = (self.x+(self.w/2), self.y+(self.h/2))
        gameDisplay.blit(TitleSurf, TitleRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def active_button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x, y, w, h))
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
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    high(len(snake_body) - 4)
    game_point(len(snake_body) - 4, 0, 0, "Game Points: ")
    game_point((highest_point), 0, 40, "Highest Game Score: ")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        active_button("Play Again!", 150, 450, 100, 50, green, bright_green, game_loop)
        active_button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(40)

def high(point):
    global highest_point
    if highest_point <= point:
        highest_point = point
        with open("point.txt", "w") as file:
            file.write(str(highest_point))

def pause():
    global paused
    gameDisplay.fill(white)
    largeText = pygame.font.SysFont("comicsansms", 90)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    settings()
        active_button("Keep playing!", 150, 450, 100, 50, green, bright_green, unpause)
        active_button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(40)

def unpause():
    global paused
    paused = False

def quitgame():
    pygame.quit()
    quit()

def settings():
    Button.family = []
    gameDisplay.fill(white)
    texts = ("Up", "Down", "Right", "Left")
    button_width = 80
    back_button_width = 100
    back_button_height = 50
    largeText = pygame.font.SysFont("comicsansms", 90)
    smallText = pygame.font.SysFont("comicsansms", 45)
    #open file key.txt, read keys
    with open("keys.txt", "r") as file:
        keys = file.read().split(",")
    #display word
    TitleSurf, TitleRect = text_objects("Settings", largeText)
    TitleRect.center = ((display_width / 2), 100)
    gameDisplay.blit(TitleSurf, TitleRect)

    for i in texts:
        inx = texts.index(i)
        k_name = pygame.key.name(int(keys[inx]))
        button = Button((display_width - BUTTON_W) / 2,
                        240 + inx * (BUTTON_H + 10),
                        BUTTON_W, BUTTON_H,
                        bright_green, green,
                        k_name, inx)
    back_button = BackButton(display_width / 7 - back_button_width / 2, display_height / 4 * 3, back_button_width, back_button_height, bright_green, green, "Back")
    game_button = BackButton(display_width / 7 * 6 - back_button_width / 2, display_height / 4 * 3, back_button_width, back_button_height, bright_red, red, "Play")
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for button in Button.family:
            if button.show():
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        num = Button.family.index(button)
                        keys[num] = event.key
                        button.key = pygame.key.name(int(keys[num]))
        if back_button.show():
            return True
        if game_button.show():
            game_loop()

        with open("keys.txt", "w") as file:
            file.write(','.join(map(str, keys)))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(30)

def game_intro():
    intro = True
    gameDisplay.fill(white)
    largeText = pygame.font.SysFont("comicsansms", 100)
    TextSurf, TextRect = text_objects("Snake Game", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    settings()
                    game_intro()
        pygame.display.update()
        clock.tick(40)

def game_loop():
    global paused
    global highest_point
    global snake_body

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

    #open file point.txt
    file = open("point.txt", "r")
    file_num = file.read()
    highest_point = int(file_num)
    file.close()
    #open file keys.txt
    with open("keys.txt", "r") as file:
        keys = file.read().split(",")
    keys = map(int, keys)
    up, down, right, left = keys

    while True:
        count = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == K_p:
                    paused = True
                    pause()
                if event.key == K_q:
                    quitgame()
                if event.key == left:
                    if dir != 2:
                        if count:
                            x_change = -snake_width
                            y_change = 0
                            count = False
                            dir = LEFT
                if event.key == right:
                    if dir != 4:
                        if count:
                            x_change = snake_width
                            y_change = 0
                            count = False
                            dir = RIGHT
                if event.key == down:
                    if dir != 1:
                        if count:
                            y_change = snake_width
                            x_change = 0
                            count = False
                            dir = DOWN
                if event.key == up:
                    if dir != 3:
                        if count:
                            y_change = -snake_width
                            x_change = 0
                            count = False
                            dir = UP

        snake_x = x_change + snake_body[0][0]
        snake_y = y_change + snake_body[0][1]
        points = len(snake_body) - 4
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

try:
    game_intro()

except KeyboardInterrupt:
    quitgame()
