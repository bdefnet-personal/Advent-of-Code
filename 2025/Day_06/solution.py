def get_num_digits_per_equation(operations_dirty):
    num_digits_per_equation = []

    num_digits = 0
    for i in range(len(operations_dirty)):
        if i == 0:
            num_digits += 1
            continue
        if operations_dirty[i] == " ":
            num_digits += 1
        else:
            num_digits_per_equation.append(num_digits-1)
            num_digits = 1
    num_digits_per_equation.append(num_digits)
    return num_digits_per_equation

operations = []
operands = []
operations_dirty = []
operands_dirty = []

with open('input.txt', 'r') as f:
    content = f.read()
    lines = content.split('\n')
    num_lines = len(lines)
    for i in range(num_lines):
        if i == num_lines - 1:
            operations = lines[i].split()
            operations_dirty = lines[i]
        else:
            elements = lines[i].strip().split()
            numbers = [int(number) for number in elements]
            operands.append(numbers)
            operands_dirty.append(lines[i])

grand_total = 0

for i in range(len(operations)):
    if operations[i] == "+":
        total = 0
        for j in range(len(operands)):
            total += operands[j][i]
        grand_total += total
    elif operations[i] == "*":
        total = 1
        for j in range(len(operands)):
            total *= operands[j][i]
        grand_total += total

print(f"Part 1: {grand_total}")

grand_total = 0

num_equations = len(operations)
num_digits_per_equation = get_num_digits_per_equation(operations_dirty)

offset = 0
for eq_idx in range(num_equations):
    if operations[eq_idx] == "+":
        total = 0
        for digit_idx in range(num_digits_per_equation[eq_idx]):
            num_operands = len(operands)
            operand_value = 0
            for operand_idx in range(num_operands):
                if operands_dirty[operand_idx][offset + digit_idx] != " ":
                    operand_value = operand_value * 10 + int(operands_dirty[operand_idx][offset + digit_idx])
            total += operand_value
        grand_total += total
    elif operations[eq_idx] == "*":
        total = 1
        for digit_idx in range(num_digits_per_equation[eq_idx]):
            num_operands = len(operands)
            operand_value = 0
            for operand_idx in range(num_operands):
                if operands_dirty[operand_idx][offset + digit_idx] != " ":
                    operand_value = operand_value * 10 + int(operands_dirty[operand_idx][offset + digit_idx])
            total *= operand_value
        grand_total += total
    
    offset += num_digits_per_equation[eq_idx] + 1

print(f"Part 2: {grand_total}")