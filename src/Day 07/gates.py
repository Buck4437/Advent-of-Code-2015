import math


class Gate:

    def __init__(self, type, entered, output):
        self.type = type
        self.input = []
        if isinstance(entered, list):
            for enter in entered:
                if enter.isdecimal():
                    self.input.append(int(enter))
                else:
                    self.input.append(enter)
        else:
            self.input.append(entered)
        self.output = output

    def eval(self, args):
        op = self.type
        if op == "BUFFER":
            return args[0]
        if op == "NOT":
            return 0xffff ^ args[0]
        if op == "AND":
            return args[0] & args[1]
        if op == "OR":
            return args[0] | args[1]
        if op == "LSHIFT":
            return args[0] * pow(2, args[1])
        if op == "RSHIFT":
            return math.floor(args[0] * pow(2, -args[1]))
        print("Not supported operation", op)
        return -1

    def __str__(self):
        return f"{self.type}, {self.input}, {self.output}"


gate = Gate("NOT", "a", "aa")
