#!/usr/bin/env python3
import random
import os

def clear_screen():
    # Safe fallback if clear command not available
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        pass

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        if mines >= width * height:
            raise ValueError("Number of mines must be less than total cells.")
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        # Track win condition
        self.total_safe = width * height - mines
        self.revealed_safe = 0
        self.game_over = False

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(f"{i:2d}" for i in range(self.width)))
        for y in range(self.height):
            print(f"{y:2d} ", end='')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        cell = '*'
                    else:
                        count = self.count_mines_nearby(x, y)
                        cell = str(count) if count > 0 else ' '
                else:
                    cell = '.'
                print(cell, end=' ')
            print()
        print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue  # don't count the cell itself
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # Bounds check
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True  # Ignore out-of-bounds clicks without ending game
        cell_index = y * self.width + x
        # If already revealed, nothing changes
        if self.revealed[y][x]:
            return True
        # Hit a mine -> lose
        if cell_index in self.mines:
            self.game_over = True
            return False
        # Reveal this safe cell
        self.revealed[y][x] = True
        self.revealed_safe += 1
        # Auto-expand if no adjacent mines
        if self.count_mines_nearby(x, y) == 0:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.reveal(nx, ny)
        return True

    def has_won(self):
        return self.revealed_safe == self.total_safe

    def play(self):
        while True:
            self.print_board()
            if self.has_won():
                self.print_board(reveal=True)
                print("Congratulations! You cleared all safe cells. You win!")
                break
            try:
                raw = input("Enter coordinates as x y (or q to quit): ").strip()
                if raw.lower() in ('q', 'quit', 'exit'):
                    print("Goodbye!")
                    break
                parts = raw.split()
                if len(parts) != 2:
                    print("Please enter exactly two integers separated by space.")
                    continue
                x, y = map(int, parts)
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
            except KeyboardInterrupt:
                print("\nInterrupted. Exiting.")
                break

if __name__ == "__main__":
    game = Minesweeper()
    game.play()