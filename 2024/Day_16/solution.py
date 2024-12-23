'''
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
'''
import heapq

def traverse_maze(maze, goal, visited, candidates):
    best_score = -1
    all_paths = set()

    max_row = len(maze)
    max_col = len(maze[0])

    while candidates:
        candidate = heapq.heappop(candidates)

        pos = candidate[1][0]
        facing = candidate[1][1]
        path = candidate[1][2]
        path.add(pos)
        score = candidate[0]

        if pos == goal:
            if best_score == -1:
                all_paths = set(path)
                best_score = score
            elif best_score > score:
                all_paths = set(path)
                best_score = score
            elif best_score == score:
                all_paths = all_paths.union(path)

        if (pos, facing) in visited:
            if visited[(pos, facing)] < score:
                continue
    
        visited[(pos, facing)] = score

        #move forward
        if facing == "NORTH":
            if pos[0] > 0 and maze[pos[0] - 1][pos[1]] != "#":
                heapq.heappush(candidates, (score + 1, ((pos[0] - 1, pos[1]), facing, set(path))))
        elif facing == "SOUTH":
            if pos[0] < max_row - 1 and maze[pos[0] + 1][pos[1]] != "#":
                heapq.heappush(candidates, (score + 1, ((pos[0] + 1, pos[1]), facing, set(path))))
        elif facing == "WEST":
            if pos[1] > 0 and maze[pos[0]][pos[1] - 1] != "#":
                heapq.heappush(candidates, (score + 1, ((pos[0], pos[1] - 1), facing, set(path))))
        elif facing == "EAST":
            if pos[1] < max_col - 1 and maze[pos[0]][pos[1] + 1] != "#":
                heapq.heappush(candidates, (score + 1, ((pos[0], pos[1] + 1), facing, set(path))))

        #rotate
        if facing in ["NORTH", "SOUTH"]:
            heapq.heappush(candidates, (score + 1000, (pos, "EAST", set(path))))
            heapq.heappush(candidates, (score + 1000, (pos, "WEST", set(path))))
        if facing in ["EAST", "WEST"]:
            heapq.heappush(candidates, (score + 1000, (pos, "NORTH", set(path))))
            heapq.heappush(candidates, (score + 1000, (pos, "SOUTH", set(path))))

    return best_score, all_paths

with open('input.txt', 'r') as f:
    content = f.read()

    maze = []

    reindeer_position = ()
    reindeer_orientation = "EAST"
    end_position = ()

    for row, line in enumerate(content.strip().split("\n")):
        maze.append([c for c in line])
        if 'S' in line:
            reindeer_position = (row, line.find("S"))
        if 'E' in line:
            end_position = (row, line.find("E"))

    visited = {}
    candidates = []
    heapq.heappush(candidates, (0, (reindeer_position, reindeer_orientation, set())))
    best_score, all_paths = traverse_maze(maze, end_position, visited, candidates)

    print(f"Part 1 Answer: {best_score}")
    print(f"Part 2 Answer: {len(all_paths)}")
