
    
    
def fence_plot(garden, visited, row, col):
    num_rows = len(garden)
    num_cols = len(garden[0])

    target_letter = garden[row][col]
    visited[row][col] = True

    area = 0
    perimeter = 0
    bulk_perimeter = 0
    num_diff_neighbors = 0
    num_diff_neighbors_bulk = 0

    if col > 0 and garden[row][col-1] == target_letter:
        if not visited[row][col-1]:
            a,p,bp = fence_plot(garden, visited, row, col-1)
            area += a
            perimeter += p
            bulk_perimeter += bp
    else:
        num_diff_neighbors += 1
        num_diff_neighbors_bulk += 1
        if (row < num_rows - 1 and garden[row+1][col] == target_letter) and (col == 0 or garden[row+1][col-1] != target_letter):
            num_diff_neighbors_bulk -= 1

    if col < num_cols - 1 and garden[row][col+1] == target_letter:
        if not visited[row][col+1]:
            a,p,bp = fence_plot(garden, visited, row, col+1)
            area += a
            perimeter += p
            bulk_perimeter += bp
    else:
        num_diff_neighbors += 1
        num_diff_neighbors_bulk += 1
        if (row < num_rows - 1 and garden[row+1][col] == target_letter) and (col == num_cols - 1 or garden[row+1][col+1] != target_letter):
            num_diff_neighbors_bulk -= 1

    if row > 0 and garden[row-1][col] == target_letter:
        if not visited[row-1][col]:
            a,p,bp = fence_plot(garden, visited, row-1, col)
            area += a
            perimeter += p
            bulk_perimeter += bp
    else:
        num_diff_neighbors += 1
        num_diff_neighbors_bulk += 1
        if (col < num_cols - 1 and garden[row][col+1] == target_letter) and (row == 0 or garden[row-1][col+1] != target_letter):
            num_diff_neighbors_bulk -= 1

    if row < num_rows - 1 and garden[row+1][col] == target_letter:
        if not visited[row+1][col]:
            a,p,bp = fence_plot(garden, visited, row+1, col)
            area += a
            perimeter += p
            bulk_perimeter += bp
    else:
        num_diff_neighbors += 1
        num_diff_neighbors_bulk += 1
        if (col < num_cols - 1 and garden[row][col+1] == target_letter) and (row == num_rows - 1 or garden[row+1][col+1] != target_letter):
            num_diff_neighbors_bulk -= 1

    area += 1
    perimeter += num_diff_neighbors
    bulk_perimeter += num_diff_neighbors_bulk
    
    return area, perimeter, bulk_perimeter

def calc_price_for_plot(garden, visited, r, c):
    a,p,bp = fence_plot(garden, visited, r, c)
    return a * p, a * bp

with open('input.txt', 'r') as f:
    content = f.read()
    
    garden = [[c for c in line] for line in content.split("\n")]
    num_rows = len(garden)
    num_cols = len(garden[0])


    visited = [[False for i in range(len(garden[0]))] for j in range(len(garden))]

    fence_price = 0
    bulk_fence_price = 0

    for r in range(num_rows):
        for c in range(num_cols):
            if not visited[r][c]:
                fp, bp = calc_price_for_plot(garden, visited, r, c)
                fence_price += fp
                bulk_fence_price += bp
    print(f"Part 1: Cost of Fencing = {fence_price}")
    print(f"Part 2: Cost of Fencing = {bulk_fence_price}")
