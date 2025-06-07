#!/usr/bin/env python3

# ===============================================
# Conway's Game of Life
# -----------------------------------------------
# Description   : Simulating the Conway's Game of Life
# Author(s)     : aditya-an1l
# Created       : 06/07/2025
# Last Modified : 06/07/2025 15:49 (aditya-an1l)
# Comment       : To run the script, execute the following
#                 commands in your terminal
#                 $ python3 gof.py
#
#                 Here are some hotkeys -
#                 - "q" or "Esc" to quit the game
#                 - Up/Down key to modify the cell cell
#                 - Left/Right to modify simulation speed
# ===============================================

import curses
import random
import time
import signal


def create_grid(rows: int, cols: int) -> list[list[int]]:
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]


def count_neighbors(grid: list[list[int]], x: int, y: int, rows: int, cols: int) -> int:
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = (x + dx) % rows, (y + dy) % cols
        count += grid[nx][ny]
    return count


def update(grid: list[list[int]], rows: int, cols: int) -> list[list[int]]:
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            neighbors = count_neighbors(grid, i, j, rows, cols)
            if grid[i][j] == 1 and neighbors in [2, 3]:
                new_grid[i][j] = 1
            elif grid[i][j] == 0 and neighbors == 3:
                new_grid[i][j] = 1
    return new_grid


def resize_grid(grid: list[list[int]], new_rows: int, new_cols: int) -> list[list[int]]:
    return create_grid(new_rows, new_cols)


def main(stdscr) -> None:
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(0)
    stdscr.keypad(True)

    cell_size = 1
    delay = 100

    rows, cols = stdscr.getmaxyx()
    rows, cols = rows // cell_size, cols // cell_size
    grid = create_grid(rows, cols)

    while True:
        stdscr.clear()

        new_rows, new_cols = stdscr.getmaxyx()
        new_rows, new_cols = new_rows // cell_size, new_cols // cell_size
        if new_rows != len(grid) or new_cols != len(grid[0]):
            grid = create_grid(new_rows, new_cols)
            rows, cols = new_rows, new_cols

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    for dy in range(cell_size):
                        for dx in range(cell_size):
                            y = i * cell_size + dy
                            x = j * cell_size + dx
                            max_y, max_x = stdscr.getmaxyx()
                            if 0 <= y < max_y and 0 <= x < max_x - 1:
                                try:
                                    stdscr.addch(y, x, "█")
                                except curses.error:
                                    pass

        stdscr.refresh()
        time.sleep(delay / 1000.0)
        grid = update(grid, rows, cols)

        key = stdscr.getch()
        if key == ord("q") or key == 27:
            break
        elif key == curses.KEY_UP and cell_size < 5:
            cell_size += 1
        elif key == curses.KEY_DOWN and cell_size > 1:
            cell_size -= 1
        elif key == curses.KEY_RIGHT and delay > 10:
            delay -= 10
        elif key == curses.KEY_LEFT:
            delay += 10


if __name__ == "__main__":
    curses.wrapper(main)
