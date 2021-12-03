with open("input.txt", "r") as f:
    dat = [1 if c == "(" else -1 for c in f.readlines()[0]]


def part1():
    return sum(dat)


def part2():
    pos = 0
    sum = 0
    while sum != -1:
        sum += dat[pos]
        pos += 1
    return pos


print(part1())
print(part2())
