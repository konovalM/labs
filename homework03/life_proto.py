import pygame
import random

from pygame.locals import *
from typing import List, Tuple

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:

    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed
        self.grid = self.create_grid(randomize=True)

    def draw_lines(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y), (self.width, y))

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        # PUT YOUR CODE HERE

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_lines()

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            # PUT YOUR CODE HERE
            self.draw_grid()
            self.grid = self.get_next_generation()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        """
        Создание списка клеток.

        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """
        grid = []
        for i in range(self.cell_height):
            new_row = []
            for j in range(self.cell_width):
                if randomize:
                    new_row.append(random.choice([0, 1]))
                else:
                    new_row.append(0)
            grid.append(new_row)
        return grid

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if self.grid[i][j] != 0:
                    y = i * self.cell_size
                    x = j * self.cell_size
                    pygame.draw.rect(self.screen, pygame.Color('green'), (x+1, y+1, self.cell_size-1, self.cell_size-1))
                else:
                    x = j * self.cell_size
                    y = i * self.cell_size
                    pygame.draw.rect(self.screen, pygame.Color('white'),
                                     (x+1, y+1, self.cell_size-1, self.cell_size-1))

    def get_neighbours(self, cell: Cell) -> int:
        """
        Вернуть список соседних клеток для клетки `cell`.

        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.

        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.

        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """
        cells = []
        for i in range(cell[0] - 1, cell[0] + 2):
            if i >= self.cell_height or i < 0:
                continue
            for j in range(cell[1] - 1, cell[1] + 2):
                if j >= self.cell_width or j < 0:
                    continue
                if i == cell[0] and j == cell[1]:
                    continue
                cells.append(self.grid[i][j])

        return cells

    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        next_grid = []
        for i in range(self.cell_height):
            new_line = []
            for j in range(self.cell_width):
                new_line.append([])
            next_grid.append(new_line)

        for i in range(self.cell_height):
            for j in range(self.cell_width):
                cell = i, j
                if self.grid[i][j] == 1:
                    if 2 <= sum(self.get_neighbours((cell))) <= 3:
                        next_grid[i][j] = 1
                    else:
                        next_grid[i][j] = 0
                else:
                    if sum(self.get_neighbours((cell))) == 3:
                        next_grid[i][j] = 1
                    else:
                        next_grid[i][j] = 0
        return next_grid



game = GameOfLife(1250, 1250, 10, 10)
game.run()



