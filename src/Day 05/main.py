import re

puz_input = []
with open("input.txt", "r") as f:
    for line in f:
        puz_input.append(line.strip())


def part1():
    count = 0
    for string in puz_input:
        if sum(map(lambda x: len(string.split(x))-1, "aeiou")) < 3:
            continue
        if len(re.findall("(ab)|(cd)|(pq)|(xy)", string)) > 0:
            continue
        if len(re.findall("([a-z])\\1", string)) > 0:
            count += 1
    return count


def part2():
    count = 0
    regexes = ("([a-z]{2}).*\\1", "([a-z])[a-z]\\1")
    for string in puz_input:
        for regex in regexes:
            result = re.findall(regex, string)
            if len(result) == 0:
                break
            print(result)
        else:
            print(string)
            count += 1
    return count


def main():
    print(part1())
    print(part2())


main()
