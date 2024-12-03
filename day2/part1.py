import csv
from enum import Enum, auto

reports = list(csv.reader(open("./input.txt"), delimiter=" "))


class Direction(Enum):
    POSITIVE = auto()
    NEGATIVE = auto()


def is_level_value_safe(x: int, y: int) -> bool:
    return 0 < abs(x - y) < 4


def is_report_safe(report: list[str]) -> bool:
    checks = zip(report[0:-1], report[1:])
    changes = [int(r) - int(l) for l, r in checks]

    direction = Direction.NEGATIVE if changes[0] < 0 else Direction.POSITIVE

    for c in changes:
        if direction == Direction.NEGATIVE and c > 0:
            return False

        if direction == Direction.POSITIVE and c < 0:
            return False

        if not 0 < abs(c) < 4:
            return False

    return True


safe_reports = [r for r in reports if is_report_safe(r)]

print(len(safe_reports))
