from sudoku.solver import BackTrackSolver, SelectionMethod
from sudoku import SudokuGame

import os

import numpy as np
from colorama import Fore


def parse_input():
    os.system("cls" if os.name == "nt" else "clear")
    size: int = int(input(f"{Fore.CYAN}Enter size of sudoku (Ex: 9):{Fore.RESET} "))
    game: np.array = np.zeros((size, size), dtype=int)
    for i in range(size):
        row: str = input(f"Enter row {i + 1}: ").split(" ")
        while len(row) != size:
            row: str = input(
                f"{Fore.RED}Invalid input. Enter the row again:{Fore.RESET} "
            ).split(" ")
        for j in range(size):
            game[i][j] = int(row[j])
    return game


def main():
    arto_inkala = np.array(
        [
            [8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 6, 0, 0, 0, 0, 0],
            [0, 7, 0, 0, 9, 0, 2, 0, 0],
            [0, 5, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 4, 5, 7, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 3, 0],
            [0, 0, 1, 0, 0, 0, 0, 6, 8],
            [0, 0, 8, 5, 0, 0, 0, 1, 0],
            [0, 9, 0, 0, 0, 0, 4, 0, 0],
        ]
    )

    david_filmer = np.array(
        [
            [0, 0, 9, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 6, 0, 3, 0],
            [0, 0, 0, 8, 0, 0, 0, 0, 2],
            [0, 8, 0, 0, 0, 4, 0, 0, 0],
            [0, 0, 0, 0, 7, 0, 5, 0, 0],
            [6, 0, 0, 9, 0, 0, 0, 0, 0],
            [0, 0, 7, 0, 1, 0, 9, 0, 0],
            [0, 4, 0, 0, 0, 3, 0, 0, 8],
            [0, 0, 0, 2, 0, 0, 0, 6, 0],
        ]
    )

    sdk = david_filmer

    # uncomment next line for custom input
    # sdk = parse_input()

    game = SudokuGame(sdk)
    bt_solver = BackTrackSolver(game)
    # gt_solver = GeneticSolver(game)
    result = bt_solver.solve(
        step_by_step=True, selection=SelectionMethod.MOST_CONSTRAINED
    )
    print("\n" + str(result["solved"]))


if __name__ == "__main__":
    main()
