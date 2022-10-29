import re
from Node import *

puz_input = []
with open("input.txt", "r") as f:
    for line in f:
        puz_input.append(line.strip())


nodes = {}


def construct_graph():
    for instruction in puz_input:
        result = re.search(r"(.*) to (.*) = (\d*)", instruction)
        if result is not None:
            start, end, dst_str = result.groups()
            dst = int(dst_str)
            add_neighbour(start, end, dst)
        else:
            print("Failed to parse", instruction)


def create_node(name):
    node = Node(name)
    nodes[name] = node
    return node


def add_neighbour(str1, str2, distance):
    node1 = create_node(str1) if str1 not in nodes.keys() else nodes[str1]
    node2 = create_node(str2) if str2 not in nodes.keys() else nodes[str2]
    nb1, nb2 = Neighbour(node1, distance), Neighbour(node2, distance)
    node1.add_neighbour(nb2)
    node2.add_neighbour(nb1)


def find_min_dist(nbs):
    if len(nbs) == 0:
        return 0
    minimum = None
    nb_nodes = set(map(lambda neighbour: neighbour.node, nbs))
    for nb in nbs:
        distance, node = nb.distance, nb.node
        other_nbs = set()
        for other_nb in node.get_neighbour():
            if other_nb.node in nb_nodes:
                other_nbs.add(other_nb)
        min_dst = find_min_dist(other_nbs) + distance
        if minimum is None or min_dst < minimum:
            minimum = min_dst
    return minimum


def find_max_dist(nbs):
    if len(nbs) == 0:
        return 0

    maximum = 0
    nb_nodes = set(map(lambda neighbour: neighbour.node, nbs))
    for nb in nbs:
        distance, node = nb.distance, nb.node
        other_nbs = set()
        for other_nb in node.get_neighbour():
            if other_nb.node in nb_nodes:
                other_nbs.add(other_nb)
        max_dst = find_max_dist(other_nbs) + distance
        maximum = max(maximum, max_dst)
    return maximum


def part1():
    min_dst = 10000000
    for node in nodes.values():
        dst = find_min_dist(node.get_neighbour())
        min_dst = min(min_dst, dst)
    return min_dst


def part2():
    max_dst = 0
    for node in nodes.values():
        dst = find_max_dist(node.get_neighbour())
        max_dst = max(max_dst, dst)
    return max_dst


def main():
    construct_graph()
    print(part1())
    print(part2())


main()
