class Node:

    def __init__(self, name):
        self.name = name
        self.neighbour = set()

    def add_neighbour(self, neighbour):
        self.neighbour.add(neighbour)

    def get_neighbour(self):
        return self.neighbour.copy()

    def __str__(self):
        neigh_name = []
        for neighbour in self.neighbour:
            neigh_name.append(neighbour.node.name)
        return f"Node {self.name}, with neighbour {', '.join(neigh_name)}"


class Neighbour:

    def __init__(self, node, distance):
        self.node = node
        self.distance = distance

    def __str__(self):
        return f"Neighbour {self.node.name} with distance {self.distance}"
