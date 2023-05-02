from sudoku.solver.solver import SudokuSolver
from sudoku.game import SudokuGame



class GeneticSolver(SudokuSolver):
    def __init__(self, game: SudokuGame = None, log=True) -> None:
        super().__init__(game, log)

    