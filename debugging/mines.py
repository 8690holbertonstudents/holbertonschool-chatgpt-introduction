#!/usr/bin/python3
import random
import os


def clear_screen():
    # Clear screen on Windows or Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')


class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.total_cells = width * height
        self.mine_count = mines
        self.non_mine_cells = self.total_cells - mines
        self.mines = set(random.sample(range(self.total_cells), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.revealed_count = 0  # Count of revealed cells

    def print_board(self, reveal=False):
        # Display the board with an optional flag to reveal all mines
        clear_screen()
        print('   ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        # Count mines in adjacent cells
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # Validate coordinates are within bounds
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False

        # Check if the cell is a mine
        if (y * self.width + x) in self.mines:
            return False

        # Mark the cell as revealed
        if not self.revealed[y][x]:
            self.revealed[y][x] = True
            self.revealed_count += 1

        # If there are no adjacent mines, reveal surrounding cells
        if self.count_mines_nearby(x, y) == 0:
            to_reveal = [(x, y)]
            while to_reveal:
                cx, cy = to_reveal.pop(0)
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx = cx + dx
                        ny = cy + dy
                        if (
                            0 <= nx < self.width
                            and 0 <= ny < self.height
                            and not self.revealed[ny][nx]
                        ):
                            self.revealed[ny][nx] = True
                            self.revealed_count += 1
                            if self.count_mines_nearby(nx, ny) == 0:
                                to_reveal.append((nx, ny))

        return True

    def play(self):
        while True:
            self.print_board()

            # Check if the player has revealed all non-mine cells
            if self.revealed_count == self.non_mine_cells:
                print("Congratulations! You've revealed \
                      all non-mine cells. You win!")
                break

            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                # Validate bounds
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of bounds. Please try again.")
                    continue

                # If the player hits a mine, end the game
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue  # Continue loop after invalid input


if __name__ == "__main__":
    game = Minesweeper()
    game.play()
