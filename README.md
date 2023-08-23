# Sudoku Game / Solver

> *This is a project for Aritficial Intelligence course (1319104) at Amirkabir University of Thechnology. This course aligns with CS188 Artificial Intelligence at UC Berkeley.*

This project implements a Sudoku puzzle engine along with an enhanced backtracking solver. You can find out more about the game on [Wikipedia](https://en.wikipedia.org/wiki/Sudoku)

## Dependencies
This package requires some libraries:
 - numpy
 - colorama
 - PySimpleGUI

## Sudoku Engine
The engine is located in `./sudoku/game/sudoku.py`. You can import the engine and create a Sudoku game using:
```python
from sudoku.game import SudokuGame
my_game = SudokuGame() # this will create an empty 9x9 Sudoku board
```
You can also pass a numpy array to the constructor to initialize a board with some fixed values. For example:
```python
from sudoku.game import SudokuGame
my_game = SudokuGame(arr=some_custom_9x9_numpy_array)
```

`sudoku.game` also provides some preloaded sample Sudoku games which you can use. For example:
```python
from sudoku.game import SudokuGame
from sudoku.game import SudokuSamples as ss
sample = ss.medium_9 # a medium 9x9 game
my_game = SudokuGame(arr=sample)
```

### `sudoku.game.sudoku`
This module provides the `SudokuGame` class. This class is a general implementation for custom sized sudoku games. It also provides some methods to check for game constraints.
- `SudokuGame.validate` method can be used to validate the board and check if the game is solved. If false, it can return the number of occurances of each value for each row, column and grid.
- `SudokuGame.possible_values` method returns possible numbers that can be placed on a certain cell.
- `SudokuGame.draw` method draws the current state of the game in a graphical manner.

There are a few more utility methods available to help you with your implementation of the game. This package provides all necessary tools to implement your own GUI and AR versions. For more information, please check out the docstrings and comments.

## Sudoku Solver
I have also implemented a simple [backtracking algorithm](https://en.wikipedia.org/wiki/Backtracking) to solve sudoku games. The algorithm can be improved by employing Minimum Remaining Value (MRV) enhancements on top of the core solver. First, you can use the solver as follows:
```python
from sudoku.solver import BackTrackSolver # core backtrack solver
from sudoku.solver import SelectionMethod as sm # solver options

solver = BackTrackSolver(game=some_SudokuGame_object)
reults = solver.solve(step_by_step=True, # this prints the steps as the
                                         # algorithm tries to solve the game
                      selection=sm.MOST_CONSTRAINED # how to select the next
                                                    # candidate cell in backtracking stack
                      )
```

The solver checks whether the game is solvable. If true, it will solve the game and return a dictionary containing the solved instance of the game, the original instance, time, number of total steps and number of backtracks taken to solve the game. There are a few utility methods provided by the backtrack solver as well to reproduce the steps, go forward/backward in the solver stack etc. which you can check out.

### `sudoku.solver.solver.SelectionMethod`
This `Enum` class provides some options for solver's selection method. This includes:
- `SelectionMethod.ROW`: Ordered from left-to-right, top-to-bottom
- `SelectionMethod.COLUMN`: Ordered from top-to-bottom, left-to-right
- `SelectionMethod.GRID`: Ordered first on grids (ltr, ttb) then the same as `SelectionMethod.ROW` within each grid
- `SelectionMethod.RANDOM`: Randomly selects the next cell to fill
- `SelectionMethod.LEAST_CONSTRAINED`: Cells that have more possible values to fill in have more priority. If two cells have the same number of possible values, ltr ttb order is used/.
- `SelectionMethod.MOST_CONSTRAINED`: Same as `SelectionMethod.LEAST_CONSTRAINED` but cells that have the least number of possible values are prioritized.

The solver is also able to continue a partially solved sudoku puzzle by setting `reset_solver=False` when calling `BackTrackSolver.solve` method.

You can learn more about how the backtrack solver works by checking out the docstrings and comments.

### `sudoku.solver.solver.genetic`
This module is a work in progress and implements a sudoku solver based on [genetic algorithms](https://en.wikipedia.org/wiki/Genetic_algorithm).