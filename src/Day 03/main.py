with open("input.txt", "r") as f:
    data = [c for c in f.read()]


def run(coord, c):
    if c == ">":
        coord[0] += 1
    if c == "<":
        coord[0] -= 1
    if c == "^":
        coord[1] += 1
    if c == "v":
        coord[1] -= 1


def part1():
    coord = [0, 0]
    prev = set()
    for c in data:
        run(coord, c)
        prev.add(str(coord))
    return len(prev)


def part2():
    coord = [0, 0]
    coord2 = [0, 0]
    first = True
    prev = set()
    for c in data:
        co = coord if first else coord2
        run(co, c)
        prev.add(str(co))
        first = not first
    return len(prev)


print(data)
print(part1())
print(part2())
