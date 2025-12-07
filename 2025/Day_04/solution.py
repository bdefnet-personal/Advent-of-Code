def get_neighbors(row, col):
    neighbors = []
    # Top
    if row > 0:
        neighbors.append(diagram[row - 1][col])
    # Bottom
    if row < len(diagram) - 1:
        neighbors.append(diagram[row + 1][col])
    # Left
    if col > 0:
        neighbors.append(diagram[row][col - 1])
    # Right
    if col < len(diagram[row]) - 1:
        neighbors.append(diagram[row][col + 1])
    # Top-left
    if row > 0 and col > 0:
        neighbors.append(diagram[row - 1][col - 1])
    # Top-right
    if row > 0 and col < len(diagram[row]) - 1:
        neighbors.append(diagram[row - 1][col + 1])
    # Bottom-left
    if row < len(diagram) - 1 and col > 0:
        neighbors.append(diagram[row + 1][col - 1])
    # Bottom-right
    if row < len(diagram) - 1 and col < len(diagram[row]) - 1:
        neighbors.append(diagram[row + 1][col + 1])
    return neighbors

diagram = []

with open('input.txt', 'r') as f:
    content = f.read()
    for row in content.strip().split('\n'):
        diagram.append(row)

count = 0
for row in range(len(diagram)):
    #print(diagram[row])
    for col in range(len(diagram[row])):
        if diagram[row][col] == '@':
            neighbor_rolls = 0
            neighbors = get_neighbors(row, col)
            for neighbor in neighbors:
                if neighbor == '@':
                    neighbor_rolls += 1
            if neighbor_rolls < 4:
                #print(f"Roll at {row}, {col}")
                count += 1

print(f"Part 1:Num Rolls: {count}")

count = 0
new_count = -1

while new_count != 0:
    diagram2 = []
    new_count = 0
    for row in range(len(diagram)):
        new_row = ""
        for col in range(len(diagram[row])):
            if diagram[row][col] =='@':
                neighbor_rolls = 0
                neighbors = get_neighbors(row, col)
                for neighbor in neighbors:
                    if neighbor =='@':
                        neighbor_rolls += 1
                if neighbor_rolls < 4:
                    #print(f"Roll at {row}, {col}")
                    new_row = new_row + "."
                    new_count += 1
                else:
                    new_row = new_row + "@"
            else:
                new_row = new_row + "."
        
        diagram2.append(new_row)
        #print(new_row)
    diagram = diagram2
    #print(f"Removed {new_count} rolls")
    #print("--------------------------------")
    count += new_count

print(f"Part 2:Num Rolls: {count}")
