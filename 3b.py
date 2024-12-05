import re
from math import prod


def process(stream, always=False):
    enabled = True
    for token in stream:
        match token:
            case "don't()", _, _:
                enabled = False
            case "do()", _, _:
                enabled = True
            case _, a, b:
                if enabled or always:
                    yield int(a) * int(b)


tokens = re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", open("3.example").read())
print(sum(process(tokens, always=True)))
print(sum(process(tokens)))
