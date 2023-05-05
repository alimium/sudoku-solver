from dataclasses import dataclass
import numpy as np


@dataclass
class SudokuSamples:
    arto_inkala_9 = np.array(
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

    david_filmer_9 = np.array(
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

    medium_9 = np.array(
        [
            [0, 0, 0, 7, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 9, 0],
            [6, 0, 2, 0, 0, 1, 0, 0, 8],
            [0, 0, 0, 0, 0, 4, 0, 0, 5],
            [0, 0, 9, 0, 0, 0, 7, 0, 0],
            [4, 0, 0, 5, 0, 0, 0, 0, 0],
            [1, 0, 0, 9, 0, 0, 5, 0, 3],
            [0, 2, 0, 0, 0, 0, 0, 7, 0],
            [0, 0, 4, 0, 0, 8, 0, 0, 0],
        ]
    )

    easy_9 = np.array(
        [
            [0, 0, 0, 0, 0, 7, 0, 8, 0],
            [0, 7, 0, 0, 0, 0, 0, 3, 0],
            [0, 0, 0, 5, 0, 0, 0, 0, 9],
            [0, 4, 0, 0, 0, 0, 0, 0, 0],
            [9, 0, 2, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 6, 0, 0, 0, 0],
            [7, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 5, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 4, 0, 0, 0],
        ]
    )

    easy_16 = np.array(
        [
            [15, 0, 0, 11, 6, 0, 0, 4, 3, 0, 0, 1, 12, 0, 0, 16],
            [0, 7, 0, 0, 0, 14, 0, 3, 4, 0, 12, 0, 0, 0, 15, 0],
            [0, 3, 5, 8, 11, 16, 0, 1, 13, 0, 6, 10, 7, 14, 9, 0],
            [0, 0, 14, 6, 2, 15, 0, 0, 0, 0, 8, 5, 1, 4, 0, 0],
            [0, 12, 0, 15, 0, 9, 0, 0, 0, 0, 16, 0, 8, 0, 14, 0],
            [9, 1, 0, 3, 0, 2, 14, 0, 0, 4, 11, 0, 5, 0, 12, 13],
            [0, 2, 4, 0, 0, 12, 0, 0, 0, 0, 9, 0, 0, 10, 11, 0],
            [0, 11, 0, 0, 15, 0, 10, 0, 0, 3, 0, 12, 0, 0, 1, 0],
            [0, 0, 0, 7, 0, 4, 0, 10, 5, 0, 1, 0, 6, 0, 0, 0],
            [0, 6, 0, 13, 0, 5, 11, 15, 8, 14, 2, 0, 10, 0, 4, 0],
            [0, 0, 0, 10, 0, 13, 0, 16, 7, 0, 4, 0, 14, 0, 0, 0],
            [0, 5, 12, 4, 0, 0, 6, 7, 9, 10, 0, 0, 11, 3, 16, 0],
            [1, 8, 6, 0, 7, 0, 0, 14, 16, 0, 0, 4, 0, 13, 10, 12],
            [13, 0, 15, 0, 8, 1, 0, 0, 0, 0, 10, 9, 0, 16, 0, 5],
            [11, 0, 0, 12, 10, 3, 16, 0, 0, 5, 13, 14, 9, 0, 0, 8],
            [0, 0, 3, 0, 13, 0, 15, 9, 12, 1, 0, 8, 0, 11, 0, 0],
        ]
    )