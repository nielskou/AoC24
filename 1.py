lists = zip(*(map(int, line.split()) for line in open("1.txt")) )
left, right = map(sorted, lists)
print(sum(abs(l-r) for l, r in zip(left, right)))

print(sum(l * right.count(l) for l in left))





if __name__ == '__main__':
    pass
