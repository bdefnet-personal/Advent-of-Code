from functools import cache
import math

g_seen_patterns = set()

def create_indicators_string(length, lights):
    indicators_string = "."*length
    for light in lights:
        indicators_string = indicators_string[:light] + "#" + indicators_string[light+1:]
    return indicators_string

@cache
def toggle_indicators(initial_state, toggle_pattern):
    new_state = ""
    for i in range(len(toggle_pattern)):
        if toggle_pattern[i] == "#":
            if initial_state[i] == "#":
                new_state += "."
            else:
                new_state += "#"
        else:
            new_state += initial_state[i]
    return new_state

def iterate_indicators_queue(indicators_goal, attempt_queue):
    while len(attempt_queue) > 0:
        attempt = attempt_queue.pop(0)
        if attempt[0] == indicators_goal:
            return attempt[1]
        else:
            for button in buttons:
                intermediate_indicators = create_indicators_string(len(indicators_goal), button)
                intermediate_indicators = toggle_indicators(attempt[0], intermediate_indicators)
                if intermediate_indicators in g_seen_patterns:
                    continue
                g_seen_patterns.add(intermediate_indicators)
                attempt_queue.append((intermediate_indicators, attempt[1] + 1))
    return 0

def solve_machine_indicators(indicators_goal, buttons):
    attempt_queue = []
    intermediate_indicators = "."*len(indicators_goal)
    g_seen_patterns.clear()
    g_seen_patterns.add(intermediate_indicators)
    attempt_queue.append((intermediate_indicators, 0))    
    return iterate_indicators_queue(indicators_goal, attempt_queue)

def gauss_jordan(matrix, eps=1e-12):
    """
    Solves a system of linear equations using Gauss-Jordan elimination.
    The function reduces the matrix to reduced row echelon form.
    Modifies the matrix in-place. Assumes the matrix is augmented, i.e.,
    the last column is the right-hand side.
    Returns a list of solutions.
    """
    n = len(matrix)
    m = len(matrix[0])
    for col in range(min(n, m - 1)):
        # Find the row with the largest absolute value in this column
        sel = max(range(col, n), key=lambda i: abs(matrix[i][col]))
        if abs(matrix[sel][col]) < eps:
            continue  # skip zero column, treated as free variable
        # Swap current row with selected row
        matrix[col], matrix[sel] = matrix[sel], matrix[col]

        # Normalize the pivot row
        factor = matrix[col][col]
        for j in range(col, m):
            matrix[col][j] /= factor

        # Eliminate the current column from other rows
        for i in range(n):
            if i != col:
                factor = matrix[i][col]
                for j in range(col, m):
                    matrix[i][j] -= factor * matrix[col][j]

    return matrix

def create_matrix_of_equations(buttons, joltages):
    matrix = []
    for i in range(len(joltages)):
        row = []
        for j in range(len(buttons)):
            if i in buttons[j]:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    for i in range(len(joltages)):
        matrix[i].append(joltages[i])
    return matrix

def create_final_equations(solution):
    #[button idx, [constant, (coeff, button idx), ...]]
    equations = []
    for row in solution:
        equation = []
        left = ""
        #find first 1 in row
        i = 0
        found = False
        for i in range(len(row)-1):
            if row[i] == 1:
                equation.append(i)
                equation.append(row[-1])
                left = f"x{i}"
                found = True
                break
        if not found:
            continue

        for i in range(i+1, len(row)-1):
            if row[i] != 0:
                equation.append((-row[i],i))

        equations.append(equation)        

    return equations

def evaluate_equation(joltages, attempt, buttons, equations):
    intermediate_joltages = [0]*len(joltages)
    total_presses = 0
    for button_idx in range(len(buttons)):
        button = buttons[button_idx]
        num_presses = 0
        if button_idx in attempt.keys():
            num_presses = attempt[button_idx]
        else:
            for equation in equations:
                if equation[0] == button_idx:
                    num_presses = equation[1]
                    for coeff, b_idx in equation[2:]:
                        num_presses += coeff * attempt[b_idx]
                    break

        if math.isclose(num_presses, 0, abs_tol=1e-9):
            num_presses = 0
        if num_presses < 0:
            return (False, 0)
        if not math.isclose(num_presses, round(num_presses), abs_tol=1e-9):
            return (False, 0)

        num_presses = round(num_presses)
        for j in range(len(button)):
            intermediate_joltages[button[j]] += num_presses
        total_presses += num_presses

    for i in range(len(joltages)):
        if intermediate_joltages[i] != joltages[i]:
            return (False, 0)
    return (True, total_presses)

def iterate_joltages_queue(joltages, attempt_queue, buttons, equations):
    best_solution = float('inf')
    while len(attempt_queue) > 0 and len(attempt_queue) < 1000000:
        attempt = attempt_queue.pop(0)
        bSolution, num_presses = evaluate_equation(joltages, attempt, buttons, equations)
        if bSolution:
            best_solution = min(best_solution, num_presses)
        for key in attempt.keys():
            new_attempt = attempt.copy()
            new_attempt[key] += 1
            if sum(new_attempt.values()) > best_solution:
                continue
            pattern = "-".join(str(x) for x in new_attempt.values())
            if pattern in g_seen_patterns:
                continue
            g_seen_patterns.add(pattern)
            attempt_queue.append(new_attempt)
    
    if best_solution == float('inf'):
        return 0
    return best_solution

def solve_machine_joltages(joltages, buttons, equations):
    #figure out the free variables
    free_variables = set()
    for equation in equations:
        for coeff, button_idx in equation[2:]:
            free_variables.add(button_idx)

    attempt = {}
    for free_variable in free_variables:
        attempt[free_variable] = 0
    g_seen_patterns.clear()
    g_seen_patterns.add("-".join(str(x) for x in attempt.values()))
    return iterate_joltages_queue(joltages, [attempt], buttons, equations)
    

#This is a pretty slow solution.  Part 1 is fast, but Part 2 can take over an hour to run.

with open('input.txt', 'r') as f:
    content = f.read()
    machines = content.strip().split('\n')

total_indicators_presses = 0
total_joltages_presses = 0

num_machines = 0
for machine_idx, machine in enumerate(machines):
    m = machine.split(' ')
    indicators = m[0][1:-1]
    buttons = []
    for i in range(1,len(m)-1):
        buttons.append([int(x) for x in m[i][1:-1].split(',')])
    joltages = [int(x) for x in m[len(m)-1][1:-1].split(',')]

    total_indicators_presses += solve_machine_indicators(indicators, buttons)

    matrix_of_equations = create_matrix_of_equations(buttons, joltages)
    solution = gauss_jordan(matrix_of_equations)
    equations = create_final_equations(solution)
    #print(f"Machine {machine_idx+1}")
    total_joltages_presses += solve_machine_joltages(joltages, buttons, equations)

print(f"Part 1: {total_indicators_presses}")
print(f"Part 2: {total_joltages_presses}")