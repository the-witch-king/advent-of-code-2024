import re

file = open("./input.txt")
lines = file.readlines()
input = "".join(line.rstrip() for line in lines)

command = re.compile(r"mul\(\d{0,3},\d{0,3}\)")
digit = re.compile(r"\d+")
do = re.compile(r"do\(\)")
dont = re.compile(r"don't\(\)")


def extract_do_commands(input: str) -> str:
    to_do = do.split(input)
    return "".join([dont.split(do)[0] for do in to_do])


def multiply(input: str) -> int:
    digits = digit.findall(input)
    return int(digits[0]) * int(digits[1])


do_commands = extract_do_commands(input)
results = [multiply(com) for com in command.findall(do_commands)]
print(sum(results))
