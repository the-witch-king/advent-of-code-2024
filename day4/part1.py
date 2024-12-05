from copy import deepcopy
import re

SAMPLE = "./sample_input.txt"
INPUT = "./input.txt"
file = open(INPUT)
lines = file.readlines()

type Matrix = list[list[str]]


def get_columns(matrix: Matrix) -> Matrix:
    size = len(matrix)

    result: list[list[str]] = [["" for n in range(size)] for m in range(size)]

    for i in range(0, size):
        for j in range(0, size):
            result[j][i] = matrix[i][j]

    return result


def in_bounds(m: Matrix, coordinate: tuple[int, int]) -> bool:
    x, y = coordinate

    if x < 0 or x >= len(m):
        return False

    row = m[x]
    if y < 0 or y >= len(row):
        return False

    return True


def get_diagonals(
    m: Matrix,
    start: tuple[int, int],
    traverse: tuple[int, int],
    start_traverse: tuple[int, int],
) -> Matrix:
    next_start = start
    start_dx, start_dy = start_traverse
    result = []
    while in_bounds(m, next_start):
        x, y = next_start
        next_coordinate = (x, y)
        diagonal = []
        while in_bounds(m, next_coordinate):
            cx, cy = next_coordinate
            tx, ty = traverse
            next_coordinate = (cx + tx, cy + ty)
            diagonal.append(m[cy][cx])

        next_start = (x + start_dx, y + start_dy)
        result.append(diagonal)
    return result


def print_matrix(matrix: Matrix):
    print("".join([line for row in matrix for line in row]))


original_matrix = [list(line.rstrip()) for line in lines]

left_to_right = deepcopy(original_matrix)
right_to_left = [list(reversed(line)) for line in deepcopy(left_to_right)]

columns = get_columns(original_matrix)
top_to_bottom = deepcopy(columns)
bottom_to_top = [list(reversed(c)) for c in deepcopy(columns)]

length = len(original_matrix)
topLeft_to_bottomRight = [
    *get_diagonals(
        original_matrix,
        start=(0, 0),
        start_traverse=(1, 0),
        traverse=(1, 1),
    ),
    *get_diagonals(
        original_matrix,
        start=(0, 1),
        start_traverse=(0, 1),
        traverse=(1, 1),
    ),
]
bottomRight_to_topLeft = [list(reversed(d)) for d in topLeft_to_bottomRight]

topRight_to_bottomLeft = [
    *get_diagonals(
        original_matrix,
        traverse=(-1, 1),
        start=(len(original_matrix) - 1, 0),
        start_traverse=(-1, 0),
    ),
    *get_diagonals(
        original_matrix,
        start=(length - 1, 1),
        start_traverse=(0, 1),
        traverse=(-1, 1),
    ),
]
bottomLeft_to_topRight = [list(reversed(d)) for d in topRight_to_bottomLeft]


all_combos = [
    *left_to_right,
    *right_to_left,
    *top_to_bottom,
    *bottom_to_top,
    *topLeft_to_bottomRight,
    *bottomRight_to_topLeft,
    *topRight_to_bottomLeft,
    *bottomLeft_to_topRight,
]


all_strings = ["".join(c) for c in all_combos]

xmas = re.compile("XMAS")
total_count = sum([len(xmas.findall(s)) for s in all_strings])

print("TOTAL: ", total_count)

"""
LtR
RtL
TtB
BtT

TLtBR
TRtBL
BLtTR
BRtTL

"""
