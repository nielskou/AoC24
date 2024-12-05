import re
from math import prod


def process(stream, always=False):
    enabled = True
    for token in stream:
        match token:
            case "don't()":
                enabled = False
            case "do()":
                enabled = True
            case _:
                total = prod(map(int, re.findall(r"\d+", token)))
                if enabled or always:
                    yield total


tokens = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", open("3.example").read())
print(sum(process(tokens, always=True)))
print(sum(process(tokens)))
