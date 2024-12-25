
def check_keys(locks, keys, total_height):
    count = 0

    for k in keys:
        for l in locks:
            match = True
            for col in range(len(k)):
                if k[col] + l[col] > total_height:
                    match = False
                    break
            if match:
                count += 1
    return count

locks = []
keys = []
total_height = 0

with open('input.txt', 'r') as f:
    bDoneReading = False
    while True:
        grid = []
        for i in range(7):
            line = f.readline().strip()
            if i == 0 and not line:
                bDoneReading = True
                break            
            grid.append(line)
        if bDoneReading:
            break
        f.readline()

        hash_count_list = []
        for col in range(len(grid[0])):
            num_hashes = -1
            for row in range(len(grid)):
                if grid[row][col] == '#':
                    num_hashes += 1 
            hash_count_list.append(num_hashes)

        if "#" in grid[0]:
            locks.append(hash_count_list)
        else:
            keys.append(hash_count_list)
        total_height = len(grid) - 2

    print(f"Part 1: {check_keys(locks, keys, total_height)}")

