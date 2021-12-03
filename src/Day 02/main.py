with open("input.txt", "r") as f:
    data = [tuple(map(lambda x: int(x), line.split("x"))) for line in f.readlines()]


def part1():
    def fun(x):
        s = sorted(x)
        return s[0] * s[1] * 3 + s[0] * s[2] * 2 + s[1] * s[2] * 2
    return sum(map(fun, data))


def part2():
    def fun(x):
        s = sorted(x)
        return (s[0] + s[1]) * 2 + s[0] * s[1] * s[2]
    return sum(map(fun, data))


print(data)
print(part1())
print(part2())
