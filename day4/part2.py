from functools import partial
from typing import Literal

SAMPLE = "./sample_input.txt"
INPUT = "./input.txt"
file = open(INPUT)
lines = file.readlines()

type Matrix = list[list[str]]
type Coordinate = tuple[int, int]
type DiagonalDirection = (
    tuple[Literal[-1], Literal[-1]]
    | tuple[Literal[1], Literal[1]]
    | tuple[Literal[-1], Literal[1]]
    | tuple[Literal[1], Literal[-1]]
)


def in_bounds(m: Matrix, coordinate: Coordinate) -> bool:
    x, y = coordinate

    if x < 0 or x >= len(m):
        return False

    row = m[x]
    if y < 0 or y >= len(row):
        return False

    return True


def left_to_right_diagonal(m: Matrix, coordinate: Coordinate) -> bool:
    cx, cy = coordinate

    tl_x = cx - 1
    tl_y = cy - 1
    br_x = cx + 1
    br_y = cy + 1

    if not in_bounds(m, (tl_x, tl_y)) or not in_bounds(m, (br_x, br_y)):
        return False

    tl_char = m[tl_y][tl_x]
    br_char = m[br_y][br_x]

    return (tl_char == "M" and br_char == "S") or (tl_char == "S" and br_char == "M")


def right_to_left_diagonal(m: Matrix, coordinate: Coordinate) -> bool:
    cx, cy = coordinate

    tr_x = cx + 1
    tr_y = cy - 1
    bl_x = cx - 1
    bl_y = cy + 1

    if not in_bounds(m, (tr_x, tr_y)) or not in_bounds(m, (bl_x, bl_y)):
        return False

    tl_char = m[tr_y][tr_x]
    br_char = m[bl_y][bl_x]

    return (tl_char == "M" and br_char == "S") or (tl_char == "S" and br_char == "M")


m = [list(line.rstrip()) for line in lines]
ltr = partial(left_to_right_diagonal, m=m)
rtl = partial(right_to_left_diagonal, m=m)

count = 0
for y, row in enumerate(m):
    for x, column in enumerate(row):
        coord = (x, y)
        if m[y][x] == "A" and ltr(coordinate=coord) and rtl(coordinate=coord):
            count = count + 1

print(count)
