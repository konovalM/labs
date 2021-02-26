import curses
import time

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self) -> None:
        """ Отобразить рамку. """
        print('+', end='')
        for i in range(self.life.cols):
            print('-', end='')
        print('+')


    def draw_grid(self) -> None:
        """ Отобразить состояние клеток. """
        for i in range(self.life.rows):
            print('|', end='')
            for j in range(self.life.cols):
                if life.curr_generation[i][j] == 1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print('|')

    def run(self) -> None:
        #screen = curses.initscr()
        # PUT YOUR CODE HERE
        while life.is_max_generations_exceed and life.is_changing:
            self.draw_borders()
            self.draw_grid()
            self.draw_borders()
            self.life.step()
            print()
            time.sleep(0.3)
        #curses.endwin()
life = GameOfLife((24, 80), max_generations=10)
ui = Console(life)
ui.run()
