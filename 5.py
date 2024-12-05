
order_text, update_text = open("5.txt").read().split("\n\n")

order = dict()

for line in order_text.splitlines():
    left, right = map(int, line.split("|"))
    order.setdefault(left, set()).add(right)

updates = [
    tuple(map(int, line.split(","))) for line in update_text.splitlines()
]



print(order)
# print(updates)

def check(update):
    pages = {page: idx for idx, page in enumerate(update)}
    for page, idx in pages.items():
        if page not in order:
            continue
        rules = order[page]
        if any(pages.get(rule, idx) < idx for rule in rules):
            return False
    return True

def correct(update):
    if check(update):
        return update
    pages = {page: idx for idx, page in enumerate(update)}
    for page, idx in pages.items():
        if page not in order:
            continue
        rules = order[page]
        for rule in rules:
            if rule not in pages:
                continue
            other = pages[rule]
            if other < idx:
                # print("in", update, "swap", pages[rule], pages[page])
                pages[rule], pages[page] = pages[page], pages[rule]
                return correct(sorted(pages, key=pages.get))
    return update


def part1():
    return sum(update[len(update)//2] for update in updates if check(update))

def part2():
    incorrect = [update for update in updates if not check(update)]
    corrected = [correct(update) for update in incorrect]
    # print(*corrected, sep="\n")
    return sum(update[len(update)//2] for update in corrected)

print(part1())
print(part2())