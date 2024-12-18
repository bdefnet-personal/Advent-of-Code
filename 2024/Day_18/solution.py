import heapq

MAZE_ROWS = 71
MAZE_COLUMNS = 71
NUM_BYTES = 1024

def traverse_maze(maze, goal, visited, candidates):
    best_score = -1

    while candidates:
        candidate = heapq.heappop(candidates)

        score = candidate[0]
        pos = candidate[1]

        if pos == goal:
            if best_score == -1:
                best_score = score
            elif best_score > score:
                best_score = score

        if pos in visited:
            if visited[pos] <= score:
                continue
    
        visited[pos] = score

        #Try to move up
        if pos[0] > 0 and maze[pos[0] - 1][pos[1]] != "#":
            new_pos = (pos[0] - 1, pos[1])
            heapq.heappush(candidates, (score + 1, new_pos))
        #Try to move down
        if pos[0] < MAZE_ROWS - 1 and maze[pos[0] + 1][pos[1]] != "#":
            new_pos = (pos[0] + 1, pos[1])
            heapq.heappush(candidates, (score + 1, new_pos))
        #Try to move left
        if pos[1] > 0 and maze[pos[0]][pos[1] - 1] != "#":
            new_pos = (pos[0], pos[1] - 1)
            heapq.heappush(candidates, (score + 1, new_pos))
        #Try to move right
        if pos[1] < MAZE_COLUMNS - 1 and maze[pos[0]][pos[1] + 1] != "#":
            new_pos = (pos[0], pos[1] + 1)
            heapq.heappush(candidates, (score + 1, new_pos))

    return best_score

with open('input.txt', 'r') as f:
    content = f.read()

    maze = []

    corrupted_bytes = []
    import re
    pattern = r'(\d+),(\d+)'
    for m in re.finditer(pattern, content):
        corrupted_bytes.append((int(m[2]), int(m[1])))

    for row in range(MAZE_ROWS):
        maze.append(["."]*MAZE_COLUMNS)
    for i in range(NUM_BYTES):
        b = corrupted_bytes[i]
        maze[b[0]][b[1]] = '#'

    start_pos = (0,0)
    end_position = (MAZE_ROWS-1,MAZE_ROWS-1)

    visited = {}
    candidates = []
    heapq.heappush(candidates, (0, start_pos))
    min_steps = traverse_maze(maze, end_position, visited, candidates)
    print(f"Part 1 Answer: {min_steps}")

    max_corrupted = len(corrupted_bytes)
    start = NUM_BYTES
    stop = start + ((max_corrupted - NUM_BYTES) // 2)
    prev_stop = max_corrupted

    while start != stop:
        maze = []
        for row in range(MAZE_ROWS):
            maze.append(["."]*MAZE_COLUMNS)
        for i in range(stop):
            b = corrupted_bytes[i]
            maze[b[0]][b[1]] = '#'

        visited = {}
        candidates = []
        heapq.heappush(candidates, (0, start_pos))
        min_steps = traverse_maze(maze, end_position, visited, candidates)
            
        if min_steps == -1:
            prev_stop = stop
            stop = start + (stop - start)// 2
        else:
            start = stop
            stop = start + (prev_stop - start) // 2

    #Flip the bytes since the question uses (x,y) and I'm using (row,col)
    flipped_byte = (corrupted_bytes[start][1], corrupted_bytes[start][0])
    print(f"Part 2 Answer: ByteIdx: {start}, Coord: {flipped_byte}")
