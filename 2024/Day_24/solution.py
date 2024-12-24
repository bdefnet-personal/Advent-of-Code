'''
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
'''
import re

def solve_gate(inputs, gates, output):
    if output in inputs and inputs[output] != "?":
        return inputs[output], 1
    else:
        gate_inputs, gate_type = gates[output]
        if inputs[gate_inputs[0]] == "?":
            inputs[gate_inputs[0]] = solve_gate(inputs, gates, gate_inputs[0])
        if inputs[gate_inputs[1]] == "?":
            inputs[gate_inputs[1]] = solve_gate(inputs, gates, gate_inputs[1])

        if gate_type == "AND":
            return inputs[gate_inputs[0]] & inputs[gate_inputs[1]]
        elif gate_type == "OR":
            return inputs[gate_inputs[0]] | inputs[gate_inputs[1]]
        elif gate_type == "XOR":
            return inputs[gate_inputs[0]] ^ inputs[gate_inputs[1]]
        

def solve_all_gates(inputs, gates, final_outputs):
    global num_new_inputs
    
    sorted_outputs = sorted(final_outputs, key=lambda x: x[0])
    for output in sorted_outputs:
        output[1] = solve_gate(inputs, gates, output[0])

def get_numbers_to_add(inputs):
    num1 = 0
    num2 = 0

    sorted_inputs = sorted(inputs.items(), key=lambda x: x[0], reverse=True)
    for key, value in sorted_inputs:
        if key.startswith('x'):
            num1 = num1 << 1 | value
        elif key.startswith('y'):
            num2 = num2 << 1 | value
    return num1, num2

pattern = r'(.*)\s(AND|OR|XOR)\s(.*)\s->\s(.*)'

inputs = {}
gates = {}
patched_gates = {}
final_outputs = []

arg1 = 0
arg2 = 0

with open('input.txt', 'r') as f:
    state = "INPUT_WIRES"
    for line in f.readlines():
        if state == "INPUT_WIRES":
            if line == '\n':
                arg1, arg2 = get_numbers_to_add(inputs)
                state = "GATES"
            else:
                line = line.strip()
                pivot = line.find(':')
                inputs[line[:pivot]] = int(line[pivot+1:])
        elif state == "GATES":
            line = line.strip()
            gate_type = ""
            new_inputs = []
            output = ""
            match = re.match(pattern, line)
            new_inputs = [match.group(1), match.group(3)]
            if new_inputs[0] not in inputs:
                inputs[new_inputs[0]] = "?"
            if new_inputs[1] not in inputs:
                inputs[new_inputs[1]] = "?"
            gate_type = match.group(2)
            output = match.group(4)
            gates[output] = (new_inputs, gate_type)

#To come up with this list of patches, I tried a variety to things including:
# 1. The gate depth for each output increases by 2 (1, 2, 4, 6, 8, ....).  this helped me find where some things were
#    going wrong
# 2. I noticed that the first gate wired to a z output, should always be an XOR gate, so I set a break when this wasn't true
# 3. I noticed that odd gate depths should always be AND gates, so I set a break when this wasn't true
# 4. I noticed that we should always introduce 4 new non-x, non-y inputs for each z we are calculating, so I
#    added a break when this wasn't true
# 5. For each zN, we should encounter an XOR with xN and yN as inputs at depth 2 and an AND with xN-1 and yN-1 at depth 3, so 
#    I added a break when this wasn't true
# 6. Using the above, plus a lot of visual inspection, I found the 4 pairs of wires that needed to be swapped
            if output == 'z10':
                output = 'gpr'
            elif output == 'gpr':
                output = 'z10'
            if output == 'cpm':
                output = 'krs'
            elif output == 'krs':
                output = 'cpm'
            if output == 'z21':
                output = 'nks'
            elif output == 'nks':
                output = 'z21'
            if output == 'z33':
                output = 'ghp'
            elif output == 'ghp':
                output = 'z33'
            patched_gates[output] = (new_inputs, gate_type)
            if output.startswith('z'):
                final_outputs.append([output, "?"])

final_outputs2 = final_outputs.copy()
inputs2 = inputs.copy()

solve_all_gates(inputs, gates, final_outputs)          
answer = 0
final_outputs.sort(key=lambda x: x[0], reverse=True)
for output in final_outputs:
    answer = answer << 1 | output[1]
print(f"Part 1: {answer}")

solve_all_gates(inputs2, patched_gates, final_outputs2)
answer = 0
final_outputs.sort(key=lambda x: x[0], reverse=True)
for output in final_outputs:
    answer = answer << 1 | output[1]
print(f"Part 2: Expected: {arg1 + arg2}, Actual: {answer}, Diff: {arg1 + arg2 - answer} (Should be 0 if patched correctly)")



