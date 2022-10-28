from gates import Gate

puz_input = []
with open("input.txt", "r") as f:
    for line in f:
        cleaned_data = line.strip()
        left, right = cleaned_data.split(" -> ")
        if "NOT" in cleaned_data:
            enter, output = left.split()[1], right
            puz_input.append(Gate("NOT", enter, output))
        else:
            if len(left.split()) == 1:
                gate_type = "BUFFER"
            else:
                gate_type = left.split()[1]
            enter, output = left.split()[::2], right
            puz_input.append(Gate(gate_type, enter, output))


def simulate_circuit(wires=None):
    if wires is None:
        wires = {}
    # Prevent mutation
    wires = wires.copy()
    unevaluated_gates = set(puz_input)
    evaluated_gates = set()
    while len(unevaluated_gates) > 0:
        unevaluated_gates_new = set()
        for gate in unevaluated_gates:
            inputs = []
            for wire in gate.input:
                if isinstance(wire, str):
                    if wire not in wires:
                        unevaluated_gates_new.add(gate)
                        break
                    inputs.append(wires[wire])
                else:
                    # Not a wire, but a number literal
                    inputs.append(wire)
            else:
                value = gate.eval(inputs)
                if gate.output not in wires:
                    wires[gate.output] = value
                evaluated_gates.add(gate)
        unevaluated_gates = unevaluated_gates_new
    return wires


def part1():
    return simulate_circuit()["a"]


def part2():
    wire_a = simulate_circuit()["a"]
    return simulate_circuit({"b": wire_a})["a"]


def main():
    print(part1())
    print(part2())


main()
