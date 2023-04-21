import os
from colorama import Fore
from typing import Dict, Union, List
from sudoku.solver.solver import SudokuSolver, SelectionMethod
from sudoku.game import Sudoku
import random
import time


class BackTrackSolver(SudokuSolver):
    def __init__(self, game: Sudoku = None, log=True) -> None:
        super().__init__(game, log)

    def solve(
        self, step_by_step=False, selection=SelectionMethod.ROW
    ) -> Dict[str, Union[Sudoku, List[Sudoku], int, int, int]]:
        os.system("cls" if os.name == "nt" else "clear")
        solved = None
        if self.game is None:
            self.log("No Game To Solve")
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
                solved = self._solve(
                    self.game, step_by_step=step_by_step, selection=selection
                )
                time_e = time.time()
                self._time = time_e - time_s

                if solved is None:
                    self.log(
                        f"{Fore.RED}Game is not Solvable.{Fore.RESET} Backtracking Stopped in {Fore.YELLOW}{self._time} Seconds{Fore.RESET}.{Fore.RESET}"
                    )
                else:
                    self.log(
                        f"{Fore.GREEN}Game Solved{Fore.RESET} Using {Fore.YELLOW}{selection.value} Selection{Fore.RESET} in {Fore.YELLOW}{self._steps} Steps{Fore.RESET} and {Fore.YELLOW}{self._backtracks} Backtracks{Fore.RESET} in {Fore.YELLOW}{self._time} Seconds{Fore.RESET}!{Fore.RESET}"
                    )

        return {
            "solved": solved,
            "original": self.original_game,
            "time": self._time,
            "steps": self._steps,
            "backtracks": self._backtracks,
        }

    def _solve(
        self, game, step_by_step=False, selection=SelectionMethod.ROW
    ) -> Union[Sudoku, None]:
        next_empty = self._get_next_empty(game, method=selection)

        if next_empty is None:
            return game

        row, col, possible_values = next_empty
        for i in possible_values:
            self._steps += 1

            if self._steps % 200 == 0:
                self.log(f"Steps: {self._steps} | Backtracks: {self._backtracks}")

            game.array_board[row, col] = i
            g_cpy = Sudoku(game.array_board)
            g_cpy.constants = self.original_game.constants
            if step_by_step:
                os.system("cls" if os.name == "nt" else "clear")
                print(g_cpy)
                print(f"\nSteps: {self._steps} | Backtracks: {self._backtracks}\n\n")
            self.solve_history.append(g_cpy)
            s = self._solve(g_cpy, step_by_step=step_by_step, selection=selection)
            if s is not None:
                return s
            game.array_board[row, col] = 0
            self._backtracks += 1

        return None

    def display_step_by_step(self, manual=False) -> None:
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