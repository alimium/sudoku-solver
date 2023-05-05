from sudoku.solver.solver import SudokuSolver, SelectionMethod
from sudoku.game import SudokuGame
import os, random, time
from typing import Dict, Union, List
from colorama import Fore


class BackTrackSolver(SudokuSolver):
    def __init__(self, game: SudokuGame = None, log=True) -> None:
        """
        Creates a solver object for the game.

        Parameters
        ----------
        game : Sudoku, optional
            The game to solve, by default None
        log : bool, optional
            Whether to log the solver steps, by default True
        """
        super().__init__(game, log)
        self._backtracks: int = 0

    def solve(
        self, reset_solver=True, step_by_step=False, selection=SelectionMethod.ROW
    ) -> Dict[str, Union[SudokuGame, List[SudokuGame], int, int, int]]:
        """
        Solves the game by backtracking algorithm. At each step, the algorithm will choose a number within valid possibilities for that cell.

        Parameters
        ----------
        step_by_step : bool, optional
            If True, the game will be printed after each step, by default False

        selection : SelectionMethod, optional
            The selection method to use, by default SelectionMethod.MOST_CONSTRAINED

            Possible options are:
                SelectionMethod.ROW: Selects elements from left to right, top to bottom
                SelectionMethod.COLUMN: Selects elements from top to bottom, left to right
                SelectionMethod.GRID: Selects elements from right to left, top to bottom but within the same grid. Grids are selected from left to right, top to bottom
                SelectionMethod.RANDOM: Selects elements randomly
                SelectionMethod.LEAST_CONSTRAINED: Selects elements with the most number of possibilities
                SelectionMethod.MOST_CONSTRAINED: Selects elements with the least number of possibilities


        Returns
        -------
        Dict[str, Union[Sudoku, List[Sudoku], int, int, int]]
            A dictionary containing the following keys:
                solved: The solved game, if it was solved, None otherwise
                original: The original game
                time: The time it took to solve the game
                steps: The number of steps it took to solve the game
                backtracks: The number of backtracks it took to solve the game

        Notes
        -----
        The game will be solved using the selection method
        specified in the selection parameter,
        which has significant effect in solver performance.
        Random selection is the slowest.
        Most constrained selection is the fastest.
        """

        os.system("cls" if os.name == "nt" else "clear")

        if reset_solver:
            self._reset_solver()
        if self.game is None:
            self.log("No Game To Solve")
        elif self._is_solved == True:
            self.log(f"{Fore.GREEN}Game Already Solved!{Fore.RESET}")
        else:
            self.log("Initializing Solver, Checking Solvability...")
            if not self._is_solvable():
                self.log(
                    f"{Fore.RED}Game Has Conflicting Constants and is not Solvable.{Fore.RESET}"
                )
            else:
                self.log(
                    f"Game Seems Solvable, Using {selection.value} Selection. Solving..."
                )
                time_s = time.time()
                self.game = self._solve(
                    self.game, step_by_step=step_by_step, selection=selection
                )
                time_e = time.time()
                self._time = time_e - time_s

                if self.game is None:
                    self.log(
                        f"{Fore.RED}Game is not Solvable.{Fore.RESET} Backtracking Stopped in {Fore.YELLOW}{self._time} Seconds{Fore.RESET}.{Fore.RESET}"
                    )
                else:
                    self._is_solved = True
                    self.log(
                        f"{Fore.GREEN}Game Solved{Fore.RESET} Using {Fore.YELLOW}{selection.value} Selection{Fore.RESET} in {Fore.YELLOW}{self._steps} Steps{Fore.RESET} and {Fore.YELLOW}{self._backtracks} Backtracks{Fore.RESET} in {Fore.YELLOW}{self._time} Seconds{Fore.RESET}!{Fore.RESET}"
                    )

        return {
            "solved": self.game,
            "original": self.original_game,
            "time": self._time,
            "steps": self._steps,
            "backtracks": self._backtracks,
        }

    def _solve(
        self, game, step_by_step=False, selection=SelectionMethod.ROW
    ) -> Union[SudokuGame, None]:
        next_empty = self._get_next_empty(game, method=selection)

        if next_empty is None:
            return game

        row, col, possible_values = next_empty
        for i in possible_values:
            self._steps += 1

            if self._steps % 200 == 0:
                self.log(f"Steps: {self._steps} | Backtracks: {self._backtracks}")

            game.array_board[row, col] = i
            g_cpy = SudokuGame(game.array_board)
            g_cpy.constants = self.original_game.constants
            if step_by_step:
                os.system("cls" if os.name == "nt" else "clear")
                print(game)
                print(f"\nSteps: {self._steps} | Backtracks: {self._backtracks}\n\n")
            self.solve_history.append(game)
            s = self._solve(g_cpy, step_by_step=step_by_step, selection=selection)
            if s is not None:
                return s
            game.array_board[row, col] = 0
            self._backtracks += 1

        return None

    def display_step_by_step(self, manual=False) -> None:
        """
        Prints the steps of the solver.

        **This method will only work if the game is already solved. Make sure to call the solve method first**

        Parameters
        ----------
        manual : bool, optional
            If True, the user will have to manually press a key to continue to the next step, by default False
        """
        for i in self.solve_history:
            os.system("cls" if os.name == "nt" else "clear")
            print(i)
            print(f"Steps: {self._steps} | Backtracks: {self._backtracks}")
            if manual:
                input("Press any key to continue...")

    def _get_next_empty(
        self, game, method=SelectionMethod.ROW
    ) -> Union[List, tuple, None]:
        next_empty = []
        if method == SelectionMethod.COLUMN:
            for i in range(game.size):
                for j in range(game.size):
                    if game.array_board[j, i] == 0:
                        next_empty.append((j, i, game.possible_values(j, i)))
        elif method == SelectionMethod.GRID:
            for g in range(game.size):
                for i in range(game.grid_size):
                    for j in range(game.grid_size):
                        true_i = i + (g // game.grid_size) * game.grid_size
                        true_j = j + (g % game.grid_size) * game.grid_size
                        if game.array_board[true_i, true_j] == 0:
                            next_empty.append(
                                (true_i, true_j, game.possible_values(true_i, true_j))
                            )
        else:
            for i in range(game.size):
                for j in range(game.size):
                    if game.array_board[i, j] == 0:
                        next_empty.append((i, j, game.possible_values(i, j)))

        if len(next_empty) > 0:
            if (
                method == SelectionMethod.ROW
                or method == SelectionMethod.COLUMN
                or method == SelectionMethod.GRID
            ):
                position = next_empty[0]
            elif method == SelectionMethod.RANDOM:
                position = random.choice(next_empty)
            elif method == SelectionMethod.MOST_CONSTRAINED:
                position = min(next_empty, key=lambda x: len(x[2]))
            elif method == SelectionMethod.LEAST_CONSTRAINED:
                position = max(next_empty, key=lambda x: len(x[2]))
            else:
                position = None
            return position

        return None
