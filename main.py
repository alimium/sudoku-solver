from sudoku.solver import BackTrackSolver, SelectionMethod
from sudoku import SudokuSamples, SudokuGame
import os
import numpy as np
from colorama import Fore


def parse_input():
    os.system("cls" if os.name == "nt" else "clear")
    size: int = int(
        input(f"{Fore.CYAN}Enter size of sudoku (Ex: 9):{Fore.RESET} "))
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

    sdk = SudokuSamples.arto_inkala_9

    # uncomment next line for custom input
    sdk = parse_input()

    game = SudokuGame(sdk)
    # game.draw()
    solver = BackTrackSolver(game)
    result = solver.solve(
        step_by_step=False, selection=SelectionMethod.MOST_CONSTRAINED
    )

    print(result['solved'])

    # solver.display_step_by_step(manual=True) # uncomment this line to see the steps of the solver
    # print("\n" + str(result["solved"])) # uncomment this line to see the solved sudoku
    # result["solved"].draw() # uncomment this line to see the solved sudoku in a GUI window


if __name__ == "__main__":
    main()
