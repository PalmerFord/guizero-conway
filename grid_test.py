"""Assert tests for Conway's Game of Life

@author: Palmer Ford 
@date: fall, 2021
"""

from grid import Grid, Cell

grid = Grid([[Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0)],
             [Cell(status=0), Cell(status=0), Cell(status=1), Cell(status=0), Cell(status=0)],
             [Cell(status=1), Cell(status=0), Cell(status=1), Cell(status=0), Cell(status=0)],
             [Cell(status=0), Cell(status=1), Cell(status=1), Cell(status=0), Cell(status=0)],
             [Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0)]])

expected_grid = Grid([[Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0)],
                      [Cell(status=0), Cell(status=1), Cell(status=0), Cell(status=0), Cell(status=0)],
                      [Cell(status=0), Cell(status=0), Cell(status=1), Cell(status=1), Cell(status=0)],
                      [Cell(status=0), Cell(status=1), Cell(status=1), Cell(status=0), Cell(status=0)],
                      [Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0)]])
 
grid.grid = grid.next_gen()
# Checks to make sure standard cell formations behave properly
assert (str(grid) == str(expected_grid))

grid = Grid([[Cell(status=1), Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=1)],
             [Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0)],
             [Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0)],
             [Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0)],
             [Cell(status=1), Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0)]])

expected_grid = Grid([[Cell(status=1), Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=1)],
                      [Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0)],
                      [Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0)],
                      [Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=0)],
                      [Cell(status=1), Cell(status=0), Cell(status=0), Cell(status=0), Cell(status=1)]])

grid.grid = grid.next_gen()
# Checks to make sure the cells wrap around the grid for both the x and the y 
assert (str(grid) == str(expected_grid))




