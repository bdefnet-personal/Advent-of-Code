UP = [-1, 0]
DOWN = [1, 0]
LEFT = [0, -1]
RIGHT = [0, 1]

def turn_right(dir):
    if dir == UP:
        return RIGHT
    elif dir == DOWN:
        return LEFT
    elif dir == LEFT:
        return UP
    else:
        return DOWN

def traverse_map(my_map, trail, check_for_loop):
    guard_pos = []
    for row, line in enumerate(my_map):
        for col, char in enumerate(line):
            if char == '^':
                guard_pos = [row, col]
                break
    dir = UP
    max_col = len(my_map[0])
    max_row = len(my_map)

    while True:
        my_map[guard_pos[0]][guard_pos[1]] = 'X'

        if check_for_loop and tuple(guard_pos) in trail and dir in trail[tuple(guard_pos)]:
            #my_map = '\n'.join(''.join(row) for row in my_map)
            #print(my_map)
            #print("\n")
            return True
        
        if tuple(guard_pos) not in trail:
            trail[tuple(guard_pos)] = []
        trail[tuple(guard_pos)].append(dir)

        next_pos = [guard_pos[0] + dir[0], guard_pos[1] + dir[1]]
        
        if next_pos[0] < 0 or next_pos[0] >= max_row or next_pos[1] < 0 or next_pos[1] >= max_col:
            break
        if my_map[next_pos[0]][next_pos[1]] == '#':
            dir = turn_right(dir)
        else:
            my_map[guard_pos[0]][guard_pos[1]] = 'X'
            guard_pos = next_pos

    #my_map = '\n'.join(''.join(row) for row in my_map)
    #print(my_map)
    #print("\n")
    return False


with open('input.txt', 'r') as f:
    content = f.read()
    original_map = [[char for char in line] for line in content.strip().split('\n')]

    my_map = [[char for char in row] for row in original_map]

    trail = {}

    traverse_map(my_map, trail, False)
    count = sum(row.count('X') for row in my_map)
    
    loop_count = 0
    first = True
    for idx, pos in enumerate(trail.keys()):
        print(f"Index: {idx}")
        if first:
            first = False
            continue
        my_map = [[char for char in row] for row in original_map]
        my_map[pos[0]][pos[1]] = '#'
        new_trail = {}
        if traverse_map(my_map, new_trail, True):
            loop_count += 1

    print(f"Number of X's: {count}")
    print(f"Number of loops: {loop_count}")
