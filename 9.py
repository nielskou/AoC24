import tqdm
inp = open("9.txt").read()

drive = []

it = iter(inp)
indexed = {}
filled = {}
free = {x: [] for x in range(10)}
pos = 0
for idx, chunk in enumerate(it):
    drive.extend([idx]*int(chunk))
    indexed[pos] = (idx, int(chunk))
    pos += int(chunk)
    filled[pos] = (idx, int(chunk))
    try:
        empty = next(it)
    except StopIteration:
        break
    drive.extend([None]*int(empty))
    indexed[pos] = (None, int(empty))
    free[int(empty)].append(pos)
    pos += int(empty)



# for step in tqdm.trange(drive.count(None)):
#     space = drive.index(None)
#     drive[space] = drive.pop()

for idx, item in enumerate(drive):
    if item is None:
        while (new := drive.pop()) is None:
            continue
        drive[idx] = new


print(sum(idx*idd for idx, idd in enumerate(drive) if idd))

# from pprint import pprint
#
# pprint(indexed)
todo = list(indexed.items())
todo.reverse()

# for idx, (name, width) in tqdm.tqdm(todo):
#     if idx is None:
#         continue
#     spot, spotsize = min(((section, flen) for section, (fid, flen) in indexed.items() if flen >= width and fid is None), default=(None, None))
#     if spot is None:
#         continue
#     if idx <= spot:
#         continue
#     indexed[idx] = (None, width)
#     indexed[spot] = (name, width)
#     if width < spotsize:
#         indexed[spot+width] = (None, spotsize-width)
    # print("".join(str("." if name is None else name) * width for pos, (name, width) in sorted(indexed.items())))

for idx, (name, width) in tqdm.tqdm(todo):
    pass

# pprint(indexed)


# print("00992111777.44.333....5555.6666.....8888..")
# print("".join(str("." if name is None else name)*width for pos, (name, width) in sorted(indexed.items())))
print(sum((0 if name is None else int(name))*(pos * width + (width-1)*width//2) for pos, (name, width) in sorted(indexed.items())))