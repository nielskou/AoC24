from itertools import pairwise
from operator import sub

def safe(line) -> bool:
    inc = set(map(sub, line, line[1:]))
    # inc = {x - y for x, y in pairwise(line)}
    return {1, 2, 3} >= inc or inc <= {-1, -2, -3}


data = [[int(x) for x in line.split()] for line in open("2.txt")]

if __name__ == '__main__':
    print(sum(map(safe, data)))
