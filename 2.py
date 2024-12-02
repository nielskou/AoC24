from itertools import pairwise


def safe(line: list[int]) -> bool:
    all_bigger = True
    all_smaller = True
    for left, right in pairwise(line):
        if not (1 <= abs(left - right) <= 3):
            return False
        if right > left:
            all_smaller = False
        if right < left:
            all_bigger = False
    return all_smaller or all_bigger


def safe_with_dampener(line: list[int]) -> bool:
    if safe(line):
        return True
    for removed in range(len(line)):
        copy = line.copy()
        del copy[removed]
        if safe(copy):
            return True
    return False


if __name__ == '__main__':
    lines = [[int(x) for x in line.split()] for line in open("2.txt")]
    print(sum(safe(line) for line in lines))
    print(sum(safe_with_dampener(line) for line in lines))
