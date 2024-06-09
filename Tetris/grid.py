import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        for r in range(row, 0, -1):
            for column in range(self.num_cols):
                self.grid[r][column] = self.grid[r - num_rows][column]
                self.grid[r - num_rows][column] = 0

    def clear_full_rows(self):
        complete = 0
        for row in range(self.num_rows - 1, -1, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                self.move_row_down(row, 1)
                complete += 1
        return complete

    def reset(self):
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.cell_size + 11, row * self.cell_size + 11, self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

    def is_inside(self, row, column):
        return 0 <= row < self.num_rows and 0 <= column < self.num_cols
