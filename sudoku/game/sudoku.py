import math
import numpy as np
from typing import List, Tuple, Union, Dict
import PySimpleGUI as sg
from colorama import Fore


class Sudoku:
    def __init__(self, arr: Union[List, np.array] = None) -> None:
        self.size: int = arr.shape[0]
        self.grid_size: int = int(np.sqrt(self.size))
        self.array_board: np.ndarray = (
            np.zeros((self.size, self.size), dtype=int)
            if arr is None
            else np.array(arr)
        )
        self.rows: np.ndarray = self._get_rows()
        self.columns: np.ndarray = self._get_columns()
        self.grids: np.ndarray = self._get_grids()
        self.constants: Dict[Tuple[int, int], int] = self._get_constants()

    def _get_rows(self) -> np.ndarray:
        return [self.array_board[i] for i in range(self.size)]

    def _get_columns(self) -> np.ndarray:
        return [self.array_board[:, i] for i in range(self.size)]

    def _get_grids(self) -> np.ndarray:
        return [
            self.array_board[i : i + self.grid_size, j : j + self.grid_size]
            for i in range(0, self.size, self.grid_size)
            for j in range(0, self.size, self.grid_size)
        ]

    def _get_constants(self) -> np.ndarray:
        return {
            (i, j): self.array_board[i, j]
            for i in range(len(self.array_board))
            for j in range(len(self.array_board))
            if self.array_board[i, j] != 0
        }

    # ---------- utility funcitons ----------
    def __repr__(self) -> str:
        out = ""
        out += Fore.CYAN + "-" * (self.size * 3 + self.grid_size + 1) + "\n"
        for i in range(self.size):
            # print a vertical line
            out += Fore.CYAN + "|"
            # loop through each column
            for j in range(self.size):
                if (i, j) in self.constants.keys():
                    out += Fore.RED
                elif self.array_board[i, j] == 0:
                    out += Fore.LIGHTBLACK_EX
                else:
                    out += Fore.YELLOW
                out += f" {self.array_board[i, j]} "
                # print a vertical line after every third column
                if (j + 1) % self.grid_size == 0:
                    out += Fore.CYAN + "|"
            out += "\n"
            if (i + 1) % self.grid_size == 0:
                out += Fore.CYAN + "-" * (self.size * 3 + self.grid_size + 1) + "\n"
                out += Fore.RESET
        return out

    def draw(self) -> None:
        # 0 represents an empty cell
        # get the size of the board
        board = self.array_board
        n = self.size
        # create a Graph element with a canvas size of 400x400 pixels and a graph coordinate system of 0 to n
        graph = sg.Graph(
            canvas_size=(int(math.sqrt(n) * 120), int(math.sqrt(n) * 120))
            if n <= 25
            else (850, 850),
            graph_bottom_left=(0, 0),
            graph_top_right=(n, n),
            background_color="white",
            key="graph",
        )
        # create a layout for the window with the Graph element
        layout = [[graph]]
        # create a window with the layout and finalize it
        window = sg.Window("Sudoku", layout, finalize=True)
        # loop through each row
        for i in range(n):
            # loop through each column
            for j in range(n):
                # get the number or a space if empty
                if board[i, j] == 0:
                    text = " "
                else:
                    text = str(board[i, j])
                # draw a text element at the center of the cell with a font size of 18
                graph.draw_text(
                    text,
                    (j + 0.5, n - i - 0.5),
                    font=("Arial", int(math.sqrt(n) + 15)),
                    color="red" if (i, j) in self.constants.keys() else "black",
                )
        # loop through each line position
        for i in range(n + 1):
            width = 5 if (i % self.grid_size) == 0 else 1
            # draw a horizontal line across the canvas with a width of 2 pixels
            graph.draw_line((0, i), (n, i), width=width)
            # draw a vertical line across the canvas with a width of 2 pixels
            graph.draw_line((i, 0), (i, n), width=width)
        # read the window events and values until closed
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
        # close the window
        window.close()

    def validate(self, ignore_empty_cells=False, detail=False) -> Dict[str, List[bool]]:
        row_details = {}
        column_details = {}
        grid_details = {}

        for i, row in enumerate(self.rows):
            uniques = np.unique(row, return_counts=True)
            row_details[i] = dict(zip(uniques[0], uniques[1]))
            for j in range(self.size + 1):
                if j not in row_details[i].keys():
                    row_details[i][j] = 0

        for i, column in enumerate(self.columns):
            uniques = np.unique(column, return_counts=True)
            column_details[i] = dict(zip(uniques[0], uniques[1]))
            for j in range(self.size + 1):
                if j not in column_details[i].keys():
                    column_details[i][j] = 0

        for i, grid in enumerate(self.grids):
            uniques = np.unique(grid, return_counts=True)
            grid_details[i] = dict(zip(uniques[0], uniques[1]))
            for j in range(self.size + 1):
                if j not in grid_details[i].keys():
                    grid_details[i][j] = 0

        if ignore_empty_cells:
            for i in row_details.keys():
                row_details[i].pop(0)
            for i in column_details.keys():
                column_details[i].pop(0)
            for i in grid_details.keys():
                grid_details[i].pop(0)

        if detail:
            return {
                "rows": row_details,
                "columns": column_details,
                "grids": grid_details,
            }
        else:
            return {
                "rows": [
                    all([row_details[i][j] <= 1 for j in row_details[i].keys()])
                    for i in row_details.keys()
                ],
                "columns": [
                    all([column_details[i][j] <= 1 for j in column_details[i].keys()])
                    for i in column_details.keys()
                ],
                "grids": [
                    all([grid_details[i][j] <= 1 for j in grid_details[i].keys()])
                    for i in grid_details.keys()
                ],
            }

    def possible_values(self, row, column):
        # get the possible values for a cell
        # get the values in the row
        validity = self.validate(ignore_empty_cells=True, detail=True)
        row_values = [i for i in validity["rows"][row] if validity["rows"][row][i] == 0]
        column_values = [
            i
            for i in validity["columns"][column]
            if validity["columns"][column][i] == 0
        ]
        grid_values = [
            i
            for i in validity["grids"][self.get_grid(row, column)]
            if validity["grids"][self.get_grid(row, column)][i] == 0
        ]

        return list(set(row_values) & set(column_values) & set(grid_values))

    def get_grid(self, row, column):
        # get the grid number for a cell
        return (row // self.grid_size) * self.grid_size + (column // self.grid_size)
