import curses
import time

from life import GameOfLife
from ui import UI
import os
import sys
import math


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
            #print ("\n" * 100)
            #screen.clear()
            #os.system('clear')
            #os.system('CLS')
            #os.system('cls' if os.name == 'nt' else 'clear')
            '''Оптимальная работа программы возможна только в командной строке windows и linux
            (!!!Не в терминале pycharm или VS Code и т.п!!!)'''
            if os.name == 'nt':
                os.system('cls')
            elif os.name == 'posix':
                os.system('clear')
        #curses.endwin()

if len(sys.argv) == 1:
    life = GameOfLife((24, 80), max_generations=math.inf)
    ui = Console(life)
    ui.run()
rows = 24
cols = 80
gen = math.inf
try:
    if sys.argv[1] == '--help':
        print('\n'"Для запуска игры необходимо ввести параметры:", '\n', '--rows', '\n', '--cols', '\n', '--max-generations',
                '\n', 'Для запуска игры с параметрами по умолчанию необходимо прописать', '\n',  '"python life_console.py"')
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
        life = GameOfLife((rows, cols), max_generations=gen)
        ui = Console(life)
        ui.run()
except IndexError:
    pass