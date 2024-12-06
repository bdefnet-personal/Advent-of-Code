XMAS = "XMAS"

def check_for_christmas(grid, row, col):
    max_row = len(grid)
    max_col = len(grid[0])

    valid = [True]*8

    for i in range(1, 4):
        if col + i >= max_col or grid[row][col + i] != XMAS[i]:
            valid[0] = False
        if col - i < 0 or grid[row][col - i] != XMAS[i]:
            valid[1] = False
        if row + i >= max_row or grid[row + i][col] != XMAS[i]:
            valid[2] = False
        if row - i < 0 or grid[row - i][col] != XMAS[i]:
            valid[3] = False
        if row + i >= max_row or col + i >= max_col or grid[row + i][col + i] != XMAS[i]:
            valid[4] = False
        if row + i >= max_row or col - i < 0 or grid[row + i][col - i] != XMAS[i]:
            valid[5] = False
        if row - i < 0 or col + i >= max_col or grid[row - i][col + i] != XMAS[i]:
            valid[6] = False
        if row - i < 0 or col - i < 0 or grid[row - i][col - i] != XMAS[i]:
            valid[7] = False

    return valid.count(True)

def check_for_xmas(grid, row, col):
    max_row = len(grid)
    max_col = len(grid[0])

    if grid[row][col] == 'M':
        if row + 2 < max_row and col + 2 < max_col:
            if grid[row + 1][col + 1] == 'A' and grid[row + 2][col + 2] == 'S':
                if grid[row][col + 2] == 'M' and grid[row + 2][col] == 'S':
                    return 1
                elif grid[row][col + 2] == 'S' and grid[row + 2][col] == 'M':
                    return 1
    elif grid[row][col] == 'S':
        if row + 2 < max_row and col + 2 < max_col:
            if grid[row + 1][col + 1] == 'A' and grid[row + 2][col + 2] == 'M':
                if grid[row][col + 2] == 'M' and grid[row + 2][col] == 'S':
                    return 1
                elif grid[row][col + 2] == 'S' and grid[row + 2][col] == 'M':
                    return 1
    return 0

with open('input.txt', 'r') as f:
    content = f.read()

    lines = content.strip().split('\n')
    grid = [list(line) for line in lines]

    total = 0
    xmas_total = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'X':
                total += check_for_christmas(grid, row, col)
            elif grid[row][col] == 'M' or grid[row][col] == 'S':
                xmas_total += check_for_xmas(grid, row, col)

    print(f"Christmas: {total}, X-mas: {xmas_total}")

