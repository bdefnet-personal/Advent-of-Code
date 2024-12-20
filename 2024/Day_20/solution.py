def traverse_maze(maze, start, end):
    MAZE_ROWS = len(maze)
    MAZE_COLS = len(maze[0])

    path = []
    pos = start
    path.append(pos)

    while pos != end:
        #up
        if pos[0] > 0 and maze[pos[0] - 1][pos[1]] != "#":
            new_pos = (pos[0] - 1, pos[1])
            if new_pos not in path:
                path.append(new_pos)
                pos = new_pos
                continue
        #down
        if pos[0] < MAZE_ROWS - 1 and maze[pos[0] + 1][pos[1]] != "#":
            new_pos = (pos[0] + 1, pos[1])
            if new_pos not in path:
                path.append(new_pos)
                pos = new_pos
                continue
        #left
        if pos[1] > 0 and maze[pos[0]][pos[1] - 1] != "#":
            new_pos = (pos[0], pos[1] - 1)
            if new_pos not in path:
                path.append(new_pos)
                pos = new_pos
                continue
        #right
        if pos[1] < MAZE_COLS - 1 and maze[pos[0]][pos[1] + 1] != "#":
            new_pos = (pos[0], pos[1] + 1)
            if new_pos not in path:
                path.append(new_pos)
                pos = new_pos
                continue

    return path

#instead of trying to traverse paths through walls, just calculate the distance between pos and 
# end_pos in a straight line (diffX + diffY)
def find_num_cheats_over_threshold(path, max_cheat_duration, threshold):
    count = 0
    for i in range(len(path)):
        pos = path[i]
        for j in range(i + threshold + 2, len(path)):
            end_pos = path[j]
            cheat_len = abs(end_pos[0] - pos[0]) + abs(end_pos[1] - pos[1])
            if cheat_len > max_cheat_duration:
                continue
            if cheat_len > 0:
                idx_diff = j - i
                savings = idx_diff - cheat_len
                if savings >= threshold:
                    count += 1

    return count


with open('input.txt', 'r') as f:
    content = f.read()

    maze = []

    start_position = ()
    end_position = ()

    for row, line in enumerate(content.strip().split("\n")):
        maze.append([c for c in line])
        if 'S' in line:
            start_position = (row, line.find("S"))
        if 'E' in line:
            end_position = (row, line.find("E"))

    #traverse the maze keeping track of the coords of each step on the path
    path = traverse_maze(maze, start_position, end_position)

    print(f"Part 1: Num cheats that save at least 100 steps: {find_num_cheats_over_threshold(path, max_cheat_duration=2, threshold=100)}")

    print(f"Part 2: Num cheats that save at least 100 steps: {find_num_cheats_over_threshold(path, max_cheat_duration=20, threshold=100)}")
