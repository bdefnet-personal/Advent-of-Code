'''
The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 
to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) 
The result of the division operation is truncated to an integer and then written to the A register.

The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in 
register B.

The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes 
that value to the B register.

The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the 
instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after 
this instruction.

The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy
 reasons, this instruction reads an operand but ignores it.)

The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple
 values, they are separated by commas.)

The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator
 is still read from the A register.)

The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator
 is still read from the A register.)
'''
'''
Combo operands 0 through 3 represent literal values 0 through 3.
Combo operand 4 represents the value of register A.
Combo operand 5 represents the value of register B.
Combo operand 6 represents the value of register C.
Combo operand 7 is reserved and will not appear in valid programs.
'''
def get_combo_operand_value(operand, registerA, registerB, registerC):
    if operand <= 3:
        return operand
    if operand == 4:
        return registerA
    if operand == 5:
        return registerB
    if operand == 6:
        return registerC
    
    return "Error"

def run_program(program, registerA, registerB, registerC):
    output = []
    ic = 0
    while ic < len(program):
        jump = False
        opcode = program[ic]
        if opcode == 0:
            registerA = registerA // 2**(get_combo_operand_value(program[ic+1], registerA, registerB, registerC))
        elif opcode == 1:
            registerB = registerB ^ program[ic+1]
        elif opcode == 2:
            registerB = get_combo_operand_value(program[ic+1], registerA, registerB, registerC) % 8
        elif opcode == 3:
            if registerA != 0:
                ic = program[ic+1]
                jump = True
        elif opcode == 4:
            registerB = registerB ^ registerC
        elif opcode == 5:
            output.append(get_combo_operand_value(program[ic+1], registerA, registerB, registerC) % 8)
        elif opcode == 6:
            registerB = registerA // 2**(get_combo_operand_value(program[ic+1], registerA, registerB, registerC))
        elif opcode == 7:
            registerC = registerA // 2**(get_combo_operand_value(program[ic+1], registerA, registerB, registerC))
    
        if not jump:
            ic += 2
    return output

def recurse(program, registerA, registerB, registerC, idx):

    if idx < 0:
        return registerA
    
    output = []
    start = registerA
    #idx-th digit changes every 8**(idx) up to 7 times
    #we start with idx == the last idx of the program and recurse inward from there to 
    #match against each element of the program
    for j in range(8):
        registerA = start + j * 8**(idx)
        output = run_program(program, registerA, registerB, registerC)
        if program[idx] == output[idx]:
            result = recurse(program, registerA, registerB, registerC, idx-1)
            if result != "BAD":
                return result
    
    return "BAD"


def figure_out_A(program, registerB, registerC):
    return recurse(program, 8**(len(program)-1), registerB, registerC, len(program)-1)


with open('input.txt', 'r') as f:
    content = f.read()

    import re
    pattern = r'(\d+)'
    inputs = []
    for m in re.finditer(pattern, content):
        inputs.append(int(m[1]))

    registerA = inputs[0]
    registerB = inputs[1]
    registerC = inputs[2]
    program = inputs[3:]

    output = run_program(program, registerA, registerB, registerC)
    print("Part 1: " + ",".join([str(num) for num in output]))

    initialA = figure_out_A(program, registerB, registerC)
    print(f"Part 2: Register A == {initialA}")

    '''
    program: 2,4,1,1,7,5,0,3,1,4,4,4,5,5,3,0
    
    5,5,7,6,1,0,3,2
    1,5,6,4,1,0,3,2,5,5,5,2,1,1,3,2,1,5,4,0,1,1,3,2,5,5,3,6,0,2,3,2,1,5,2,4,0,2,3,2,5,5,1,2,0,3,3,2,1,5,0,0,0,3,3,2

    Add a digit at 0, 8, 64, 512, ...  so we'll have 16 digits starting at A == 8^15 == 35184372088832

    Last digit changes every 8**(n-1) up to 7 times    
    '''

