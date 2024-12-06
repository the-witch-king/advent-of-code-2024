from collections import defaultdict
from functools import partial
import functools
from typing import Callable

SAMPLE = "./sample.txt"
INPUT = "./input.txt"

file = open(INPUT)
txt = file.read()

rule_txt, pages_txt = txt.split("\n\n")
rule_lines = rule_txt.rstrip().split("\n")

pages_lines = pages_txt.rstrip().split("\n")
all_pages = [line.split(",") for line in pages_lines]

type Rules = dict[str, list[str]]
type Pages = list[str]


def make_rules(lines: list[str]) -> Rules:
    rules = defaultdict(list)
    for line in lines:
        before, after = line.split("|")

        rules[before].append(after)

    return rules


def is_in_order(pages: Pages, rules: Rules) -> bool:
    for i, p in enumerate(pages):
        seen = pages[:i]
        for s in seen:
            if s in rules[p]:
                return False

    return True


def comparison(x: str, y: str, rules: Rules) -> int:
    if y in rules[x]:
        return -1

    if x in rules[y]:
        return 1

    return 0


def order_list(pages: Pages, comparitor: Callable[[str, str], int]) -> Pages:
    return sorted(pages, key=functools.cmp_to_key(comparitor))


rules = make_rules(rule_lines)
iio = partial(is_in_order, rules=rules)
compare = partial(comparison, rules=rules)
order_page = partial(order_list, comparitor=compare)

now_ordered = [order_page(page) for page in all_pages if not iio(page)]

middle_pages: list[int] = []
for page in now_ordered:
    middle = len(page) // 2
    middle_pages.append(int(page[middle]))

print(sum(middle_pages))
