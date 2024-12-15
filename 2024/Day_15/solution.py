'''
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########

<^^>>>vv<v>>v<<

Answer = 2028
'''

def move_left(factory_map, position):
    who = factory_map[position[0]][position[1]]
    next_space = factory_map[position[0]][position[1] - 1]
    if next_space == '#':
        return False
    elif next_space == '.':
        factory_map[position[0]][position[1] - 1] = who
        factory_map[position[0]][position[1]] = '.'
        return True
    elif next_space in ['O', '[', ']']:
        if move_left(factory_map, (position[0], position[1] - 1)):
            factory_map[position[0]][position[1] - 1] = who
            factory_map[position[0]][position[1]] = '.'
            return True
    return False

def move_right(factory_map, position):
    who = factory_map[position[0]][position[1]]
    next_space = factory_map[position[0]][position[1] + 1]
    if next_space == '#':
        return False
    elif next_space == '.':
        factory_map[position[0]][position[1] + 1] = who
        factory_map[position[0]][position[1]] = '.'
        return True
    elif next_space in ['O', '[', ']']:
        if move_right(factory_map, (position[0], position[1] + 1)):
            factory_map[position[0]][position[1] + 1] = who
            factory_map[position[0]][position[1]] = '.'
            return True
    return False

def move_up(factory_map, position, just_check = False):
    who = factory_map[position[0]][position[1]]
    next_space = factory_map[position[0] - 1][position[1]]
    if next_space == '#':
        return False
    elif next_space == '.':
        if not just_check:
            factory_map[position[0] - 1][position[1]] = who
            factory_map[position[0]][position[1]] = '.'
        return True
    elif next_space == 'O':
        if move_up(factory_map, (position[0] - 1, position[1])):
            factory_map[position[0] - 1][position[1]] = who
            factory_map[position[0]][position[1]] = '.'
            return True
    elif next_space == '[':
        if (move_up(factory_map, (position[0] - 1, position[1]), just_check) and
            move_up(factory_map, (position[0] - 1, position[1] + 1), just_check)):
            if not just_check:
                factory_map[position[0] - 1][position[1]] = who
                factory_map[position[0]][position[1]] = '.'
            return True
    elif next_space == ']':
        if (move_up(factory_map, (position[0] - 1, position[1]), just_check) and
            move_up(factory_map, (position[0] - 1, position[1] - 1), just_check)):
            if not just_check:
                factory_map[position[0] - 1][position[1]] = who
                factory_map[position[0]][position[1]] = '.'
            return True
    return False

def move_down(factory_map, position, just_check = False):
    who = factory_map[position[0]][position[1]]
    next_space = factory_map[position[0] + 1][position[1]]
    if next_space == '#':
        return False
    elif next_space == '.':
        if not just_check:
            factory_map[position[0] + 1][position[1]] = who
            factory_map[position[0]][position[1]] = '.'
        return True
    elif next_space == 'O':
        if move_down(factory_map, (position[0] + 1, position[1])):
            factory_map[position[0] + 1][position[1]] = who
            factory_map[position[0]][position[1]] = '.'
            return True
    elif next_space == '[':
        if (move_down(factory_map, (position[0] + 1, position[1]), just_check) and
            move_down(factory_map, (position[0] + 1, position[1] + 1), just_check)):
            if not just_check:
                factory_map[position[0] + 1][position[1]] = who
                factory_map[position[0]][position[1]] = '.'
            return True
    elif next_space == ']':
        if (move_down(factory_map, (position[0] + 1, position[1]), just_check) and
            move_down(factory_map, (position[0] + 1, position[1] - 1), just_check)):
            if not just_check:
                factory_map[position[0] + 1][position[1]] = who
                factory_map[position[0]][position[1]] = '.'
            return True

    return False

def run_commands(factory_map, robot_position, commands, part2):
    for c in commands:
        if c == '<':
            if move_left(factory_map, robot_position):
                robot_position = (robot_position[0], robot_position[1] - 1)
        elif c == '>':
            if move_right(factory_map, robot_position):
                robot_position = (robot_position[0], robot_position[1] + 1)
        elif c == '^':
            if part2:
                if move_up(factory_map, robot_position, True):
                    move_up(factory_map, robot_position, False)
                    robot_position = (robot_position[0] - 1, robot_position[1])
            else:
                if move_up(factory_map, robot_position):
                    robot_position = (robot_position[0] - 1, robot_position[1])
        elif c == 'v':
            if part2:
                if move_down(factory_map, robot_position, True):
                    move_down(factory_map, robot_position, False)
                    robot_position = (robot_position[0] + 1, robot_position[1])
            else:
                if move_down(factory_map, robot_position):
                    robot_position = (robot_position[0] + 1, robot_position[1])

    return 

def calc_box_scores(factory_map):
    score = 0
    for row, line in enumerate(factory_map):
        for col, char in enumerate(line):
            if char in ['O', '[']:
                score += row * 100 + col
    return score

with open('input.txt', 'r') as f:
    content = f.readlines()

    factory_map = []
    double_factory_map = []

    readMap = True
    commands = ""
    robot_position = ()
    robot_position_2 = ()

    for row, line in enumerate(content):
        if line == "\n":
            readMap = False
            continue
        if readMap:
            factory_map.append([c for c in line.strip()])
            dbl = []
            for col, c in enumerate(line.strip()):
                if c == '@':
                    dbl.append('@')
                    dbl.append('.')
                    robot_position_2 = (row, col * 2)
                elif c == 'O':
                    dbl.append('[')
                    dbl.append(']')
                else:
                    dbl.append(c)
                    dbl.append(c)
            double_factory_map.append(dbl)
            if '@' in line:
                robot_position = (row, line.find("@"))
        else:
            commands += line
    
    run_commands(factory_map, robot_position, commands, False)
    run_commands(double_factory_map, robot_position_2, commands, True)
    answer = calc_box_scores(factory_map)
    answer2 = calc_box_scores(double_factory_map)
    print(f"Part 1 Answer: {answer}")
    print(f"Part 2 Answer: {answer2}")
