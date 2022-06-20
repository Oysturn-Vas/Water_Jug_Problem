"""Water Jug Problem using Pygame by Oysturn Vas"""
import os
import time
import pygame
pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Water Jug Problem!")

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BACKGROUND_IMAGE = pygame.image.load(os.path.join('assets', 'background.jpg'))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (900, 500))

WATER_JUG_IMAGE = pygame.image.load(os.path.join('assets', 'water_jug.png'))
WATER_JUG = pygame.transform.scale(WATER_JUG_IMAGE, (80, 160))

JUG_1_VALUES = [0, 4]
JUG_2_VALUES = [0, 2, 3]

JUG_1 = 0
JUG_2 = 0
COUNT = 0


def render_text(text, size, color, position):
    FONT = pygame.font.Font("freesansbold.ttf", size)
    text_main = FONT.render(text, True, color)
    textRect = text_main.get_rect()
    textRect.center = position
    WIN.blit(text_main, textRect)


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y,
                         self.width, self.height), 0)
        if self.text != '':
            font = pygame.font.SysFont('montserrat', 16)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                     self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


START = button(WHITE, 400, 430, 70, 30, 'START')
empty_jar_1 = button(WHITE, 750, 0, 150, 50, 'Empty Jar 1')
empty_jar_2 = button(WHITE, 750, 50, 150, 50, 'Empty Jar 2')
fill_jar_1 = button(WHITE, 750, 100, 150, 50, 'Fill Jar 1')
fill_jar_2 = button(WHITE, 750, 150, 150, 50, 'Fill Jar 2')
empty_jar_1_into_2 = button(WHITE, 700, 200, 200, 50, 'Empty Jar 1 into Jar 2')
empty_jar_2_into_1 = button(WHITE, 700, 250, 200, 50, 'Empty Jar 2 into Jar 1')
PLAY_AGAIN = button(WHITE, 300, 430, 120, 30, 'PLAY AGAIN')
QUIT = button(WHITE, 470, 430, 70, 30, 'QUIT')


def draw_values():
    global JUG_1
    global JUG_2
    global JUG_1_VALUES
    global JUG_2_VALUES
    if JUG_1 in JUG_1_VALUES:
        render_text(str(JUG_1), 32, BLACK, (343, 380))
    else:
        render_text("?", 32, BLACK, (343, 380))
    if JUG_2 in JUG_2_VALUES:
        render_text(str(JUG_2), 32, BLACK, (543, 380))
    else:
        render_text("?", 32, BLACK, (543, 380))
    render_text(str(COUNT), 18, BLACK, (177, 11))


def draw_start_window():
    WIN.blit(BACKGROUND, (0, 0))
    render_text("Welcome to Water Jug problem", 40, BLACK, (450, 200))
    render_text(
        "Rules : 1. There are 2 Water Jugs, One of Capacity = 4 and the Other of Capacity = 2", 16, BLACK, (440, 300))
    render_text(
        "2. The Capacity of the Jar will be displayed only when it is EMPTY or FULL", 16, BLACK, (462, 320))
    render_text(
        "3. ? Symbol indicates that the jar is filled to some (unknown) capacity", 16, BLACK, (462, 340))
    render_text(
        "4. Moves that can be played are : a. Empty Either Jar on Ground", 16, BLACK, (420, 360))
    render_text("b. Empty Either Jar into other Jar", 16, BLACK, (560, 380))
    render_text("c. Fill Either Jar", 16, BLACK, (492, 4000))
    START.draw(WIN)


def draw_game_window():
    WIN.blit(BACKGROUND, (0, 0))
    render_text("TO WIN, JAR 2 MUST HAVE THE CAPACITY OF 2",
                15, BLACK, (180, 50))
    WIN.blit(WATER_JUG, (300, 280))
    render_text("JAR 1", 18, BLACK, (342, 450))
    WIN.blit(WATER_JUG, (500, 280))
    render_text("JAR 2", 18, BLACK, (542, 450))
    render_text("Number of Moves : ", 18, BLACK, (87, 10))
    empty_jar_1.draw(WIN)
    empty_jar_2.draw(WIN)
    fill_jar_1.draw(WIN)
    fill_jar_2.draw(WIN)
    empty_jar_1_into_2.draw(WIN)
    empty_jar_2_into_1.draw(WIN)
    draw_values()


def draw_error_window(text):
    error = button(WHITE, 350, 150, 200, 100, text)
    error.draw(WIN)
    pygame.display.update()
    pygame.time.delay(450)


def check_jug_2_value():
    global JUG_2
    if JUG_2 == 2:
        return False
    return True


def draw_winner_window():
    global COUNT
    WIN.blit(BACKGROUND, (0, 0))
    render_text("CONGRATULATIONS, YOU WON", 40, BLACK, (450, 200))
    if COUNT == 4:
        render_text("You won in the most optimal moves", 32, BLACK, (440, 300))
        render_text("Thank you for Playing", 32, BLACK, (440, 340))
    else:
        render_text("This Solution can be achieved with Lesser Moves",
                    32, BLACK, (440, 300))
    PLAY_AGAIN.draw(WIN)
    QUIT.draw(WIN)
    pygame.display.update()

def game_loop():
    global JUG_1
    global JUG_2
    global COUNT
    JUG_1 = 0
    JUG_2 = 0
    COUNT = 0
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        draw_game_window()
        run = check_jug_2_value()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if empty_jar_1.isOver(pos):
                    if JUG_1 > 0:
                        JUG_1 = 0
                        COUNT += 1
                        draw_game_window()
                    else:
                        draw_error_window("Jar 1 is Empty")
                if empty_jar_2.isOver(pos):
                    if JUG_2 > 0:
                        JUG_2 = 0
                        COUNT += 1
                        draw_game_window()
                    else:
                        draw_error_window("Jar 2 is Empty")
                if fill_jar_1.isOver(pos):
                    if JUG_1 == 4:
                        draw_error_window("Jar 1 is Full")
                    else:
                        JUG_1 = 4
                        COUNT += 1
                        draw_game_window()
                if fill_jar_2.isOver(pos):
                    if JUG_2 == 3:
                        draw_error_window("Jar 2 is Full")
                    else:
                        JUG_2 = 3
                        COUNT += 1
                        draw_game_window()
                if empty_jar_1_into_2.isOver(pos):
                    if JUG_2 == 3 or JUG_1 == 0:
                        draw_error_window("Jar 2 is Full")
                    else:
                        JUG_2 += JUG_1
                        if JUG_2 > 3:
                            JUG_1 = JUG_2 - 3
                            JUG_2 = 3
                        else:
                            JUG_1 -= JUG_2
                        COUNT += 1
                        draw_game_window()
                if empty_jar_2_into_1.isOver(pos):
                    if JUG_1 == 4 or JUG_2 == 0:
                        draw_error_window("Jar 1 is Full")
                    else:
                        JUG_1 += JUG_2
                        if JUG_1 > 4:
                            JUG_2 = JUG_1 - 4
                            JUG_1 = 4
                        else:
                            JUG_2 -= JUG_1
                        COUNT += 1
                        draw_game_window()
            if event.type == pygame.MOUSEMOTION:
                if empty_jar_1.isOver(pos):
                    empty_jar_1.color = (128, 128, 128)
                else:
                    empty_jar_1.color = WHITE
                if empty_jar_2.isOver(pos):
                    empty_jar_2.color = (128, 128, 128)
                else:
                    empty_jar_2.color = WHITE
                if fill_jar_1.isOver(pos):
                    fill_jar_1.color = (128, 128, 128)
                else:
                    fill_jar_1.color = WHITE
                if fill_jar_2.isOver(pos):
                    fill_jar_2.color = (128, 128, 128)
                else:
                    fill_jar_2.color = WHITE
                if empty_jar_1_into_2.isOver(pos):
                    empty_jar_1_into_2.color = (128, 128, 128)
                else:
                    empty_jar_1_into_2.color = WHITE
                if empty_jar_2_into_1.isOver(pos):
                    empty_jar_2_into_1.color = (128, 128, 128)
                else:
                    empty_jar_2_into_1.color = WHITE
        pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        draw_start_window()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START.isOver(pos):
                    run = False
            if event.type == pygame.MOUSEMOTION:
                if START.isOver(pos):
                    START.color = (128, 128, 128)
                else:
                    START.color = WHITE

            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
    game_loop()
    draw_winner_window()
    run = True
    while run:
        clock.tick(FPS)
        draw_winner_window()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_AGAIN.isOver(pos):
                    print("Play Again")
                    game_loop()
                if QUIT.isOver(pos):
                    run = False
                    pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                if PLAY_AGAIN.isOver(pos):
                    PLAY_AGAIN.color = (128, 128, 128)
                else:
                    PLAY_AGAIN.color = WHITE
                if QUIT.isOver(pos):
                    QUIT.color = (128, 128, 128)
                else:
                    QUIT.color = WHITE

            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()

if __name__ == "__main__":
    main()