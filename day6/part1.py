from enum import Enum, auto
from dataclasses import dataclass


SAMPLE = "./sample.txt"
INPUT = "./input.txt"

file = open(INPUT)
lines = file.readlines()

raw_map = [[c for c in line.rstrip()] for line in lines]


type Coordinate = tuple[int, int]


INITIAL_GUARD = "^"


class Direction(Enum):
    UP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()


turning = {
    Direction.UP: Direction.RIGHT,
    Direction.RIGHT: Direction.DOWN,
    Direction.DOWN: Direction.LEFT,
    Direction.LEFT: Direction.UP,
}


class Map:
    guard_location: Coordinate

    def __init__(self, initial_matrix: list[list[str]]):
        self._map = initial_matrix
        self.guard_location = self.get_guard_start()

    def get_guard_start(self) -> Coordinate:
        for i in range(0, len(self._map)):
            for j in range(0, len(self._map[i])):
                if self._map[i][j] == INITIAL_GUARD:
                    return i, j

        raise ValueError("No guard found!")

    def in_bounds(self, coordinate: Coordinate) -> bool:
        y, x = coordinate

        if y < 0 or y >= len(self._map):
            return False

        row = self._map[y]
        if x < 0 or x >= len(row):
            return False

        return True

    def is_obstacle(self, coordinate: Coordinate) -> bool:
        y, x = coordinate
        return self.in_bounds(coordinate) and self._map[y][x] == "#"


@dataclass
class Guard:
    direction: Direction

    def turn(self):
        self.direction = turning[self.direction]

    def next_coordinate(self, current_location: Coordinate) -> Coordinate:
        cy, cx = current_location
        match self.direction:
            case Direction.UP:
                return (cy - 1, cx)
            case Direction.RIGHT:
                return (cy, cx + 1)
            case Direction.DOWN:
                return (cy + 1, cx)
            case Direction.LEFT:
                return (cy, cx - 1)


m = Map(raw_map)
guard = Guard(direction=Direction.UP)
print(m.guard_location)
visited: set[Coordinate] = {m.guard_location}
while (n := guard.next_coordinate(m.guard_location)) and m.in_bounds(n):
    if m.is_obstacle(n):
        guard.turn()
        continue
    visited.add(n)
    m.guard_location = n

print(len(visited))
