from collections import defaultdict

puz_input = []
with open("input.txt", "r") as f:
    for line in f:
        puz_input.append(line.strip())


def light_gen(start, end):
    xmin, xmax = min(start[0], end[0]), max(start[0], end[0])
    ymin, ymax = min(start[1], end[1]), max(start[1], end[1])
    for i in range(xmin, xmax+1):
        for j in range(ymin, ymax+1):
            yield i, j


def parse_ord(string):
    return tuple(map(int, string.split(",")))


def part1():
    on = set()
    for instruction in puz_input:
        arr_ins = instruction.split()
        if arr_ins[0] == "toggle":
            start, end = parse_ord(arr_ins[1]), parse_ord(arr_ins[3])
            for light in light_gen(start, end):
                if light in on:
                    on.remove(light)
                else:
                    on.add(light)
            continue
        start, end = parse_ord(arr_ins[2]), parse_ord(arr_ins[4])
        for light in light_gen(start, end):
            if arr_ins[1] == "on":
                on.add(light)
            elif light in on:
                on.remove(light)
    return len(on)


def part2():
    on = defaultdict(lambda: 0)
    for instruction in puz_input:
        arr_ins = instruction.split()
        if arr_ins[0] == "toggle":
            start, end = parse_ord(arr_ins[1]), parse_ord(arr_ins[3])
            for light in light_gen(start, end):
                on[light] = on[light] + 2
            continue
        start, end = parse_ord(arr_ins[2]), parse_ord(arr_ins[4])
        for light in light_gen(start, end):
            if arr_ins[1] == "on":
                on[light] = on[light] + 1
            else:
                on[light] = max(0, on[light] - 1)
    return sum(on.values())


def main():
    print(part1())
    print(part2())


main()
