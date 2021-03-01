import pygame
from pygame.locals import *
from os import environ
from life import GameOfLife
from ui import UI
import random
import sys
import math


class GUI(UI):

    def __init__(self, life: GameOfLife, cell_size: int=10, speed: int=10) -> None:
        super().__init__(life)

        # Размер клетки
        self.cell_size = cell_size

        # Ширина и высота окна
        self.width = self.life.cols * self.cell_size
        self.height = self.life.rows * self.cell_size
        self.screen_size = self.width, self.height

        # Инициализация окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Скорость игры
        self.speed = speed
    def draw_lines(self) -> None:
        # Copy from previous assignment
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color(0, 0, 0), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color(0, 0, 0), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        # Copy from previous assignment
        for i in range(self.life.rows):
            for j in range(self.life.cols):
                if self.life.curr_generation[i][j] == 1:
                    y = i * self.cell_size
                    x = j * self.cell_size
                    pygame.draw.rect(self.screen, pygame.Color(random.randint(0, 254), random.randint(0, 254),
                                    random.randint(0, 254)),
                                     (x + 1, y + 1, self.cell_size - 1, self.cell_size - 1))
                else:
                    y = i * self.cell_size
                    x = j * self.cell_size
                    pygame.draw.rect(self.screen, pygame.Color(255, 255, 255),
                                     (x + 1, y + 1, self.cell_size - 1, self.cell_size - 1))

    def mouse_click(self, xy: (int, int)):

            #self.life.prev_generation = self.life.curr_generation
            if self.life.curr_generation[xy[1] // self.cell_size][xy[0] // self.cell_size] == 0:
                self.life.curr_generation[xy[1] // self.cell_size][xy[0] // self.cell_size] = 1
            else:
                self.life.curr_generation[xy[1] // self.cell_size][xy[0] // self.cell_size] = 0


    def run(self) -> None:
        # Copy from previous assignment
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        running = True
        pause = True

        while running:

            if self.life.n_generation > self.life.max_generations:
                running = False




            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        if not pause:
                            pause = True
                        else:
                            pause = False
                if event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_click(pygame.mouse.get_pos())
                    self.draw_grid()
                    pygame.display.flip()
            if pause:
                self.draw_lines()
                self.draw_grid()
                self.life.step()
                pygame.display.flip()
                clock.tick(self.speed)
        pygame.quit()



if len(sys.argv) == 1:
    life = GameOfLife((40, 40), max_generations=math.inf)
    ui = GUI(life, cell_size=30, speed=10)
    ui.run()
rows = 40
cols = 40
gen = math.inf
size = 30
speed1 = 10
try:
    if sys.argv[1] == '--help':
        print('\n'"Для запуска игры необходимо ввести параметры:", '\n', '--rows', '\n', '--cols', '\n', '--max-generations',
                '\n', '--cell-size', '\n', '--speed', '\n', 'Для запуска игры с параметрами по умолчанию необходимо прописать', '\n',  '"python life-gui.py"')
    else:
        if '--rows' in sys.argv:
            n_rows = sys.argv.index('--rows')
            rows = int(sys.argv[n_rows+1])
        if '--cols' in sys.argv:
            n_cols = sys.argv.index('--cols')
            cols = int(sys.argv[n_cols+1])
        if '--max-generations' in sys.argv:
            n_gen = sys.argv.index('--max-generations')
            gen = int(sys.argv[n_gen+1])
        if '--cell-size' in sys.argv:
            n_size = sys.argv.index('--cell-size')
            size = int(sys.argv[n_size+1])
        if '--speed' in sys.argv:
            n_speed = sys.argv.index('--speed')
            speed1 = int(sys.argv[n_speed+1])
        life = GameOfLife((rows, cols), max_generations=gen)
        ui = GUI(life, cell_size=size, speed=speed1)
        ui.run()
except IndexError:
    pass

'''
--rows 10 --cols 10 --max-generations 50
--width 640 --height 480 --cell-size 10
'''


