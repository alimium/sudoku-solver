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

> There are a few more utility methods available to help you with your implementation of the game. This package provides all necessary tools to implement GUI and AR versions of the game. For more information, please check out the docstrings and comments.