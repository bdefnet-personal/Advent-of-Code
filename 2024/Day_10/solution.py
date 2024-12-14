
def get_num_at_offset(pos, offset, trail_map):
    max_row = len(trail_map)
    max_col = len(trail_map[0])

    newR = pos[0] + offset[0]
    newC = pos[1] + offset[1]
    if newR < 0 or newR >= max_row or newC < 0 or newC >= max_col:
        return -1
    return trail_map[newR][newC]

def hike(pos, idx, trail_map, unique_peaks):
    if idx == 9:
        unique_peaks.add(pos)
        return 1
    
    rating = 0

    if get_num_at_offset(pos, (1, 0), trail_map) == idx+1:
        rating += hike((pos[0] + 1, pos[1] + 0), idx+1, trail_map, unique_peaks)
    if get_num_at_offset(pos, (-1, 0), trail_map) == idx+1:
        rating += hike((pos[0] - 1, pos[1] + 0), idx+1, trail_map, unique_peaks)
    if get_num_at_offset(pos, (0, 1), trail_map) == idx+1:
        rating += hike((pos[0] + 0, pos[1] + 1), idx+1, trail_map, unique_peaks)
    if get_num_at_offset(pos, (0, -1), trail_map) == idx+1:
        rating += hike((pos[0] + 0, pos[1] - 1), idx+1, trail_map, unique_peaks)
    
    return rating

with open('input.txt', 'r') as f:
    content = f.read()
    trail_map = [[int(c) for c in line] for line in content.split("\n")]

    max_row = len(trail_map)
    max_col = len(trail_map[0])

    trail_heads = []
    for row in range(max_row):
        for col in range(max_col):
            if trail_map[row][col] == 0:
                trail_heads.append((row,col))

    score = 0
    rating = 0
    for th in trail_heads:
        unique_peaks = set()
        rating += hike(th, 0, trail_map, unique_peaks)
        score += len(unique_peaks)

    print(f"Part 1: Score is {score}")
    print(f"Part 2: Rating is {rating}")
