"""CS 108 Final Project

A recreation of Conway's Game of Life

@author: Palmer Ford (pjf5)
@date: fall, 2021
"""

from guizero import App, Drawing, PushButton, TextBox, Box, Window
from grid import Grid, Cell

class Life:

    def __init__(self, app):
        """Instantiate the simulation GUI app."""

        app.title = "Conway's Game of Life"
        UNIT = 900
        app.width = UNIT * 2
        app.height = UNIT

        # Add the widgets for the main window.
        self.drawing = Drawing(app, width=UNIT * 2, height=UNIT)
        self.draw_grid()                  
        self.drawing.bg = "white"
        
        self.control = Window(app, title='Control Panel')
        self.control.height = 100
        self.control.width = 325
        
        # Add the widgets for the control panel.
        box = Box(self.control, layout='grid', width=self.control.width, height=self.control.height)
        self.build_button = PushButton(box, command=self.build, text='Build', grid=[3,2])
        self.run_button = PushButton(box, command=self.run, text='Run', grid=[3,1])
        self.clear_button = PushButton(box, command=self.clear, text='Clear', grid=[4,2])
        self.reset_button = PushButton(box, command=self.reset, text='Reset', grid=[5,2])
        self.save_button = PushButton(box, command=self.save_to_file, text='Save', grid=[2,1])
        self.load_button = PushButton(box, command=self.load_from_file, text='Load', grid=[1,1])
        self.file_name = TextBox(box, grid=[1, 2, 2, 1], height='fill', width='fill')
        
        self.build_mode = True
        self.build_button.enabled = False
        
        # Creates a starter grid
        self.grid = Grid(self.new_grid())        
        
        # Check which cell is clicked if the program is in build mode
        if self.build_mode == True:
            self.drawing.when_clicked = self.check_is_clicked
        
        app.repeat(200, self.draw_frame)
        
    def draw_frame(self):
        """Draws each generation of the grid to the canvas if the program is in run mode."""
        if not self.build_mode:
            self.drawing.clear()
            self.grid.grid = self.grid.next_gen()
            # This is optional and prints a representation of the grid to the shell using ones and zeros
            # Its pretty neat actually
            # print(self.grid)
            # print('')
            for row_index in range(len(self.grid.grid)):
                for column_index in self.grid.grid[row_index]:
                    if column_index.status == 1:
                        self.drawing.rectangle(column_index.x,
                                               column_index.y,
                                               (column_index.x + column_index.side),
                                               (column_index.y + column_index.side),
                                               color="black")
                        
    def build(self):
        """Allow cell placement and redraws the grid."""
        self.drawing.clear()
        self.draw_grid()
        for row_index in range(len(self.grid.grid)):
            for column_index in self.grid.grid[row_index]:
                if column_index.status == 1:
                    self.drawing.rectangle(column_index.x,
                                           column_index.y,
                                           (column_index.x + column_index.side),
                                           (column_index.y + column_index.side),
                                           color="black")
        self.build_mode = True
        self.run_button.enabled = True
        self.clear_button.enabled = True
        self.reset_button.enabled = True
        self.save_button.enabled = True
        self.load_button.enabled = True
        self.build_button.enabled = False
        
        
    def run(self):
        """Start the animation."""
        self.last_grid = self.grid.grid[:]
        self.build_mode = False
        self.run_button.enabled = False
        self.clear_button.enabled = False
        self.reset_button.enabled = False
        self.save_button.enabled = False
        self.load_button.enabled = False
        self.build_button.enabled = True
        
        
    def new_grid(self):
        """Returns an grid of dead cells."""
        grid_blank = []
        for row_index in range(36):
            grid_blank.append([])
            for column_index in range(72):
                grid_blank[row_index].append(Cell(x=(column_index * 25), y=(row_index * 25), side=25))
        return grid_blank
    
    def clear(self):
        """Clears the current canvas of any living cells."""
        self.grid.grid = self.new_grid()
        self.drawing.clear()
        self.draw_grid()
        for row_index in range(len(self.grid.grid)):
            for column_index in self.grid.grid[row_index]:
                if column_index.status == 1:
                    self.drawing.rectangle(column_index.x,
                                           column_index.y,
                                           (column_index.x + column_index.side),
                                           (column_index.y + column_index.side),
                                           color="black")
    
    def reset(self):
        """Reverts the grid back to what it was the last time the program switched into run mode."""
        self.grid.grid = self.last_grid
        self.drawing.clear()
        self.draw_grid()
        for row_index in range(len(self.grid.grid)):
            for column_index in self.grid.grid[row_index]:
                if column_index.status == 1:
                    self.drawing.rectangle(column_index.x,
                                           column_index.y,
                                           (column_index.x + column_index.side),
                                           (column_index.y + column_index.side),
                                           color="black")
                    
                    
    def save_to_file(self):
        """Saves the current grid to a .txt file"""
        if self.build_mode:
            if self.file_name.value != '':
                file = open('saves\\' + self.file_name.value + '.txt', 'w')
                file.write(str(self.grid))
                file.close()
        
        
    def load_from_file(self):
        """Takes a grid from a .txt file and sets the current grid equal to it."""
        if self.build_mode:
            # First time using try/except
            # Pleased that I got it to work
            try:
                file = open('saves\\' + self.file_name.value + '.txt', 'r')
                loaded = (file.readlines())
                file.close()
                for i in range(len(loaded)):
                    loaded[i] = list(loaded[i].strip())
                loaded_grid = []
                for row_index in range(36):
                    loaded_grid.append([])
                    for column_index in range(72):
                        loaded_grid[row_index].append(Cell(x=(column_index * 25), y=(row_index * 25), side=25, status=int(loaded[row_index][column_index])))
                self.grid.grid = loaded_grid
                self.drawing.clear()
                self.draw_grid()
                for row_index in range(len(self.grid.grid)):
                    for column_index in self.grid.grid[row_index]:
                        if column_index.status == 1:
                            self.drawing.rectangle(column_index.x,
                                                   column_index.y,
                                                   (column_index.x + column_index.side),
                                                   (column_index.y + column_index.side),
                                                   color="black")
            except:
                print('Error: That file does not exist')

                
    def draw_grid(self):
        """Draws the grid of lines that outline the cells."""
        self.drawing.line(0, 0, 0, 900, color="#9e9e9e", width=2)
        self.drawing.line(1800, 0, 1800, 900, color="#9e9e9e", width=2)
        self.drawing.line(0, 0, 1800, 0, color="#9e9e9e", width=2)
        self.drawing.line(0, 900, 1800, 900, color="#9e9e9e", width=2)
        for row_index in range(36):
            self.drawing.line(0, (row_index * 25), 1800, (row_index * 25), color="#9e9e9e", width=2)                     
            for column_index in range(72):
                self.drawing.line((column_index * 25), 0, (column_index * 25), 900, color="#9e9e9e", width=2)
        
    def check_is_clicked(self, event):
        """Switches the status of a cell if it is clicked and the program is in build mode."""
        if self.build_mode:
            for row_index in range(len(self.grid.grid)):
                for column_index in self.grid.grid[row_index]:
                    if column_index.is_clicked(event.x, event.y):
                        if column_index.status == 0:
                            column_index.status = 1
                        else:
                            column_index.status = 0
            self.drawing.clear()
            self.draw_grid()
            for row_index in range(len(self.grid.grid)):
                for column_index in self.grid.grid[row_index]:
                    if column_index.status == 1:
                        self.drawing.rectangle(column_index.x,
                                               column_index.y,
                                               (column_index.x + column_index.side),
                                               (column_index.y + column_index.side),
                                               color="black")                    

app = App()
Life(app)
app.display()