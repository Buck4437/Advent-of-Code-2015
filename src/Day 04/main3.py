import hashlib


def hash(string):
    return hashlib.md5(string.encode()).hexdigest()


# printing the equivalent hexadecimal value.

def part1(puz_in):
    val = 0
    while True:
        key = puz_in + str(val)
        if hash(key)[:5] == "00000":
            return val
        val += 1


def part2(puz_in):
    val = 0
    while True:
        key = puz_in + str(val)
        if hash(key)[:6] == "000000":
            return val
        val += 1


def main():
    puz_in = "iwrupvqb"
    print(part1(puz_in))
    print(part2(puz_in))


main()
