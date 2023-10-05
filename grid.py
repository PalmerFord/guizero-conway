"""CS 108 Final Project

Model for Conway's Game of Life

@author: Palmer Ford (pjf5)
@date: fall, 2021
"""

import copy 

class Grid:
    """Grid models a nested list of cell objects that may be rendered to a canvas."""

    def __init__(self, grid):
        """Instantiate a grid object."""
        self.grid = grid
        
        
    def __str__(self):
        """Returns a printable version of the grid."""
        grid_str = ''
        
        for row_index in range(len(self.grid)):
            if row_index != 0:
                grid_str = grid_str + '\n'
            for column_index in self.grid[row_index]:
                grid_str = grid_str + str(column_index)
                
        return grid_str
        
        
    def next_gen(self):
        """Takes the current nested list of cells and returns the next generation."""
        new_grid = copy.deepcopy(self.grid)
        num_rows = len(self.grid)
        num_columns = len(self.grid[0])

        for row_index in range(num_rows):
            for column_index in range(num_columns):
                # Gets the number of living cells surounding the current cell
                alive_cells = (self.grid[(row_index + 1) % num_rows][(column_index + 1) % num_columns].status + # South-east
                               self.grid[(row_index + 1) % num_rows][column_index].status +                     # South
                               self.grid[(row_index + 1) % num_rows][(column_index - 1) % num_columns].status + # South-west
                               self.grid[row_index][(column_index + 1) % num_columns].status +                  # East
                               self.grid[row_index][(column_index - 1) % num_columns].status +                  # West
                               self.grid[(row_index - 1) % num_rows][(column_index + 1) % num_columns].status + # North-east
                               self.grid[(row_index - 1) % num_rows][column_index].status +                     # North
                               self.grid[(row_index - 1) % num_rows][(column_index - 1) % num_columns].status   # North-west
                               )
                # Any live cell with two or three live neighbours survives.
                if self.grid[row_index][column_index].status == 1 and (alive_cells == 2 or alive_cells == 3):
                    continue
                # Any dead cell with three live neighbours becomes a live cell.
                elif self.grid[row_index][column_index].status == 0 and alive_cells == 3:
                    new_grid[row_index][column_index].status = 1
                # All other live cells die in the next generation. Similarly, all other dead cells stay dead.
                else:
                    new_grid[row_index][column_index].status = 0
                    
        return new_grid
        
        
        
class Cell:
    """Cell models a single cell object that may be instantiated to a grid."""

    def __init__(self, x=0, y=0, side=0, status=0):
        """Instantiate a cell object."""
        self.x = x
        self.y = y
        self.side = side
        self.status = status
        
        
    def __str__(self):
        """Returns a printable '0' or '1' depending on the status of the cell."""
        return str(self.status)
        
        
    def is_clicked(self, x, y):
        """Returns whether a point is inside the bounds of the cell object."""
        # Checks if the mouse cursor is inside the bounds of the cell
        return ((x > self.x) and (x < (self.x + self.side))) and ((y > self.y) and (y < (self.y + self.side)))
