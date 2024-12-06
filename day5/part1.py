from collections import defaultdict
from functools import partial

SAMPLE = "./sample.txt"
INPUT = "./input.txt"

file = open(INPUT)
txt = file.read()

rule_txt, pages_txt = txt.split("\n\n")
rule_lines = rule_txt.rstrip().split("\n")

pages_lines = pages_txt.rstrip().split("\n")
all_pages = [line.split(",") for line in pages_lines]

type Rules = dict[str, list[str]]


def make_rules(lines: list[str]) -> Rules:
    rules = defaultdict(list)
    for line in lines:
        before, after = line.split("|")

        rules[before].append(after)

    return rules


def is_in_order(pages: list[str], rules: Rules) -> bool:
    for i, p in enumerate(pages):
        seen = pages[:i]
        for s in seen:
            if s in rules[p]:
                return False

    return True


rules = make_rules(rule_lines)

iio = partial(is_in_order, rules=rules)

middle_pages: list[int] = []
for page in all_pages:
    if iio(page):
        middle = len(page) // 2
        middle_pages.append(int(page[middle]))

print(sum(middle_pages))
