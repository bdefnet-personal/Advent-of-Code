'''
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

94a + 22b = 8400
34a + 67b = 5400

Multiply top by 34 and bottom by -94

3196a + 748b = 285600
-3196a -6298b = -507600
-5550b = -222000
b = -222000 / -5550
b = 40

Now substitute b = 40 into the first equation to get a = 80
'''

def solve_equations(a, b, p):

    if (b[0]*a[1] - b[1]*a[0]) == 0:
        if (p[0]*a[1] - p[1]*a[0]) == 0:
            #infinite solutions - pick one that maximizes the B button presses
            #the test data set doesn't hit this case, so ignoring
            pass
        else:
            return None
    
    tmp_b = (p[0]*a[1] - p[1]*a[0]) / (b[0]*a[1] - b[1]*a[0])
    tmp_a = (p[0] - (b[0] * tmp_b)) / a[0]

    if not tmp_b.is_integer():
        return None
    if not tmp_a.is_integer():
        return None
    
    return (tmp_a, tmp_b)


with open('input.txt', 'r') as f:
    content = f.read()
    
    a_buttons = []
    b_buttons = []
    prizes = []

    import re
    pattern = r'Button A: X\+(\d+), Y\+(\d+)'
    for m in re.finditer(pattern, content):
        a_buttons.append((int(m[1]), int(m[2])))

    pattern = r'Button B: X\+(\d+), Y\+(\d+)'
    for m in re.finditer(pattern, content):
        b_buttons.append((int(m[1]), int(m[2])))

    pattern = r'Prize: X=(\d+), Y=(\d+)'
    for m in re.finditer(pattern, content):
        prizes.append((int(m[1]), int(m[2])))

    coins = 0
    for i in range(len(prizes)):
        answer = solve_equations(a_buttons[i], b_buttons[i], prizes[i])
        if answer:
            coins += int(3 * answer[0] + answer[1])

    print(f"Part 1: {coins} Coins")

    coins = 0
    for i in range(len(prizes)):
        answer = solve_equations(a_buttons[i], b_buttons[i], (prizes[i][0] + 10000000000000, prizes[i][1] + 10000000000000))
        if answer:
            coins += int(3 * answer[0] + answer[1])

    print(f"Part 2: {coins} Coins")
