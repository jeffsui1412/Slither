import pygame
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

class Button:
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
            return True
        else:
            pygame.draw.rect(gameDisplay, self.ic_color, button)
            return False

    def click(self):
        click = pygame.mouse.get_pressed()
        if self.show():
            if click[0] == 1:
                print("click")

    def word(self):
        TitleSurf, TitleRect = text_objects(self.text, smallText)
        TitleRect.center = (self.x+(self.w/2), self.y+(self.h/2))
        gameDisplay.blit(TitleSurf, TitleRect)

def text_objects(text, font):
    textSurface = font.render(text, True, bright_red)
    return textSurface, textSurface.get_rect()

left_button = Button(0, 0, 100, 100, green, black, "hi")
right_button = Button(300, 0, 100, 100, green, black, "jeff")
while True:
    gameDisplay.fill(white)
    left_button.show()
    left_button.click()
    left_button.word()
    right_button.show()
    right_button.click()
    right_button.word()
    for event in pygame.event.get():
        pass
    pygame.display.update()
    clock.tick(30)





                # if button.click():
                    # if event.type == pygame.KEYDOWN:
                    #     num = buttons.index(button)
                    #     if not event.key in keys:
                    #         keys[num] = event.key
                    #         with open("keys.txt", "w") as file:
                    #             file.write(','.join(map(str, keys)))
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         quit()
        # for each in range(4):
        #     if buttons[each].show():
        #         index = buttons.index(each)
        #         keys[index] = event.key
        #         with open("keys.txt", "w") as file:
        #             file.write(','.join(map(str, keys)))
        #
        #     buttons[each].word()
        #
        #
        # #     if event.type == pygame.KEYDOWN:
        # #         for button in buttons:
        # #             if button.collidepoint(mouse_pos):
        # #                 index = buttons.index(button)
        # #                 if not event.key in keys:
        # #                     keys[index] = event.key
        # #                     with open("keys.txt", "w") as file:
        # #                         file.write(','.join(map(str, keys)))
        # # active_button("Back",150,540,100,50,green,bright_green,game_intro)
        # # active_button("Start Game",550,540,100,50,red,bright_red,game_loop)
