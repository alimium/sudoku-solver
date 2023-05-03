from sudoku.solver import BackTrackSolver, SelectionMethod
from sudoku import SudokuSamples, SudokuGame
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

    sdk = SudokuSamples.arto_inkala

    # uncomment next line for custom input
    # sdk = parse_input()

    game = SudokuGame(sdk)
    solver = BackTrackSolver(game)
    result = solver.solve(step_by_step=True, selection=SelectionMethod.MOST_CONSTRAINED)
    # solver.display_step_by_step(manual=True)
    # print("\n" + str(result["solved"]))
    # result["solved"].draw()


if __name__ == "__main__":
    main()
