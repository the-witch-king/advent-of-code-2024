import re

file = open("./input.txt")
lines = file.readlines()
input = "".join(line.rstrip() for line in lines)

command = re.compile(r"mul\(\d{0,3},\d{0,3}\)")
digit = re.compile(r"\d+")


def multiply(input: str) -> int:
    digits = digit.findall(input)
    return int(digits[0]) * int(digits[1])


results = [multiply(com) for com in command.findall(input)]
print(sum(results))
