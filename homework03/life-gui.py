import pygame
from pygame.locals import *

from life import GameOfLife
from ui import UI
import random


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



    def run(self) -> None:
        # Copy from previous assignment
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_lines()
            self.draw_grid()
            self.life.step()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()
life = GameOfLife((40, 40), max_generations=10)
ui = GUI(life, cell_size=30, speed=10)
ui.run()


