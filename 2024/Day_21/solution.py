'''
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+

'''

import heapq
import sys
import functools

numeric_keypad = [["7", "8", "9"],
                  ["4", "5", "6"],
                  ["1", "2", "3"],
                  ["X", "0", "A"]]
directional_keypad = [["X", "^", "A"],
                      ["<", "v", ">"]]

@functools.cache
def find_paths_between_keys(keypad_type, start, end):
    keypad = numeric_keypad if keypad_type == "NUMERIC" else directional_keypad
    start_pos = None
    end_pos = None

    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] == start:
                start_pos = (r,c)
            if keypad[r][c] == end:
                end_pos = (r,c)
    
    candidates = []
    heapq.heappush(candidates, (0, (start_pos, "")))

    paths = []
    while len(candidates) > 0:
        candidate = heapq.heappop(candidates)
        score = candidate[0]
        pos = candidate[1][0]
        path = candidate[1][1]
        if pos == end_pos:
            paths.append(path+"A")
            continue

        if pos[0] > end_pos[0]:
            new_pos = (pos[0]-1, pos[1])
            if keypad[new_pos[0]][new_pos[1]] != "X":
                heapq.heappush(candidates, (score+1, (new_pos, path+"^")))
        elif pos[0] < end_pos[0]:
            new_pos = (pos[0]+1, pos[1])
            if keypad[new_pos[0]][new_pos[1]] != "X":
                heapq.heappush(candidates, (score+1, (new_pos, path+"v")))
        if pos[1] > end_pos[1]:
            new_pos = (pos[0], pos[1]-1)
            if keypad[new_pos[0]][new_pos[1]] != "X":
                heapq.heappush(candidates, (score+1, (new_pos, path+"<")))
        elif pos[1] < end_pos[1]:
            new_pos = (pos[0], pos[1]+1)
            if keypad[new_pos[0]][new_pos[1]] != "X":
                heapq.heappush(candidates, (score+1, (new_pos, path+">")))

    return paths

@functools.cache
def get_shortest_directional_path_length(sequence, robot_depth):
    if robot_depth == 0:
        return len(sequence)

    shortest = 0
    
    prev = "A"
    for c in sequence:
        paths = find_paths_between_keys("DIRECTIONAL", prev, c)
        shortest += min([get_shortest_directional_path_length(path, robot_depth-1) for path in paths])
        prev = c

    return shortest


def get_shortest_path_length(code, robot_depth):
    shortest = 0

    prev = "A"
    for c in code:
        paths = find_paths_between_keys("NUMERIC", prev, c)
        shortest += min([get_shortest_directional_path_length(path, robot_depth) for path in paths])
        prev = c

    return shortest

with open('input.txt', 'r') as f:
    content = f.read()

    codes = []
    for line in content.split("\n"):
        codes.append(line)

    complexity = 0
    for code in codes:
        length = get_shortest_path_length(code, 2)
        numeric = int(code[:-1] if code[0] != "0" else code[1:-1])
        complexity += length * numeric

    print(f"Part 1 - Complexity: {complexity}")


    complexity = 0
    for code in codes:
        length = get_shortest_path_length(code, 25)
        numeric = int(code[:-1] if code[0] != "0" else code[1:-1])
        complexity += length * numeric

    print(f"Part 2 - Complexity: {complexity}")

