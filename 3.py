import re
from math import prod

mul = re.compile(r'mul\((\d+),(\d+)\)')
text = open("3.example").read()
muls = mul.findall(text)
print(muls)
total = sum(prod(map(int, args)) for args in muls)
print(total)

mul_and_enable = re.compile(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))")
part2 = mul_and_enable.findall(text)
# print(part2)

def process(stream):
    enabled = True
    for item in stream:
        if item == "don't()":
            enabled = False
        elif item == "do()":
            enabled = True
        else:
            match = mul.match(item)
            ints = map(int, match.groups())
            if enabled:
                yield prod(ints)

print(sum(process(part2)))


if __name__ == '__main__':
    pass
