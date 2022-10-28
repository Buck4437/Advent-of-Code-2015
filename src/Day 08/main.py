import re

puz_input = []
with open("input.txt", "r") as f:
    for line in f:
        puz_input.append(line.strip())


def part1():
    dif = 0
    for literal in puz_input:
        og_len = len(literal)
        content = literal[1:-1]
        content = content.replace("\\\\", "1")
        content = content.replace("\\\"", "2")
        content = re.sub("\\\\"+ "x..", "3", content)
        dif += og_len - len(content)
    return dif


def part2():
    dif = 0
    for literal in puz_input:
        new = literal
        new = new.replace("\\x", "111")
        new = new.replace("\"", "22")
        new = new.replace("\\", "33")
        new = f"\"{new}\""
        dif += len(new) - len(literal)
    return dif


def main():
    print(part1())
    print(part2())


main()
