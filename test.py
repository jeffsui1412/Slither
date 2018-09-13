import pygame
from pygame.locals import *
pygame.init()

display_width = 800
display_height = 600

green = (0, 200, 0)
bright_red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

largeText = pygame.font.SysFont("comicsansms", 90)
smallText = pygame.font.SysFont("comicsansms", 45)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

class Buttons:
    def __init__(self, x, y, w, h, ac_color, ic_color, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.ac_color = ac_color
        self.ic_color = ic_color
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def show_ac(self):
        pygame.draw.rect(gameDisplay, self.ac_color, self.rect)

    def show_ic(self):
        pygame.draw.rect(gameDisplay, self.ic_color, self.rect)

    def collide(self):
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            return True
        else:
            return False

    def click(self):
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            return True

    def write(self):
        smallText = pygame.font.SysFont("comicsansms", 45)
        TitleSurf, TitleRect = text_objects(self.text,smallText)
        TitleRect.center = (self.x+(self.w/2), self.y+(self.h/2))
        gameDisplay.blit(TitleSurf, TitleRect)

button1 = Buttons(0, 0, 100, 100, green, bright_red, "go")
button_back = Buttons(100, 100, 100, 100, green, bright_red, "Back")

def back_button(obj, x, y, w, h, a, i, text):
    obj = Buttons(x, y, w, h, a, i, text)
    if obj.collide():
        obj.show_ac()
        obj.write()
        if obj.click():
            return True
    if not obj.collide():
        obj.show_ic()
        obj.write()

def set_button(obj, x, y, w, h, a, i, text):
    obj = Buttons(x, y, w, h, a, i, text)
    if obj.collide():
        obj.show_ac()
        obj.write()
        print("Hi")
    if not obj.collide():
        obj.show_ic()
        obj.write()

def loop():
    while True:
        gameDisplay.fill(white)
        set_button("button_back", 0, 0, 100, 100, green, bright_red, "hi")
        if back_button("button_back", 100, 100, 100, 100, green, bright_red, "Back"):
            return True
        for event in pygame.event.get():
            pass
        pygame.display.update()
        clock.tick(30)

def intro():
    while True:
        gameDisplay.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_l:
                    loop()
        pygame.display.update()
        clock.tick(30)

intro()
