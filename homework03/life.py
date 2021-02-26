import pathlib
import random
from typing import List, Optional, Tuple

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: Tuple[int, int],
        randomize: bool = True,
        max_generations: Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.n_generation = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        """Создание первого игрового поля"""
        grid = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.cols):
                if randomize:
                    new_row.append(random.choice([0, 1]))
                else:
                    new_row.append(0)
            grid.append(new_row)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:

        cells = []
        for i in range(cell[0] - 1, cell[0] + 2):
            if i >= self.rows or i < 0:
                continue
            for j in range(cell[1] - 1, cell[1] + 2):
                if j >= self.cols or j < 0:
                    continue
                if i == cell[0] and j == cell[1]:
                    continue
                cells.append(self.curr_generation[i][j])

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
        for i in range(self.rows):
            new_line = []
            for j in range(self.cols):
                new_line.append([])
            next_grid.append(new_line)

        for i in range(self.rows):
            for j in range(self.cols):
                cell = i, j
                if self.curr_generation[i][j] == 1:
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

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        self.n_generation += 1

    @property
    def is_max_generations_exceed(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return not (self.n_generation > self.max_generations)

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return not (self.prev_generation == self.curr_generation)

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        field = []
        file = open(filename, "r")
        for row in file:
            line = []
            if row == '\n':
                break
            else:
                for letter in row:
                    if letter == ("\n"):
                        continue
                    else:
                        line.append(int(letter))
                field.append(line)
        continued_game = GameOfLife((len(field), len(field[0])))
        continued_game.curr_generation = field
        #print(field)

        return continued_game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        file = open(filename, "w")
        for i in range(self.rows):
            for j in range(self.cols):
                file.write(str(self.curr_generation[i][j]))
            file.write('\n')

life = GameOfLife.from_file('glider.txt')
print(life.curr_generation)
for _ in range(4):
    life.step()
print(life.curr_generation)
life.save(pathlib.Path('glider-4-steps.txt'))


