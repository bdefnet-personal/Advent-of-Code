diagram = []

with open('input.txt', 'r') as f:
    content = f.read()
    diagram = content.strip().split('\n')

#find the start index
start_idx = diagram[0].find("S")

beams = [start_idx]

num_splits = 0
for row_idx in range(1,len(diagram)):
    new_beams = set()
    for beam in beams:
        if diagram[row_idx][beam] == "^":
            num_splits += 1
            if beam - 1 >= 0:
                new_beams.add(beam - 1)
            if beam + 1 < len(diagram[row_idx]):
                new_beams.add(beam + 1)
        else:
            new_beams.add(beam)
    beams = new_beams
    
print(f"Part 1: {num_splits}")

#For Part 2, start at the bottom of the diagram.  
#memoize the number of paths to the end from each splitter.
memo = [1 for _ in range(len(diagram[0]))]
for row_idx in range(len(diagram) - 2, -1, -1):
    for col_idx in range(len(diagram[row_idx])):
        if diagram[row_idx][col_idx] == "^":
            left = 0
            right = 0

            if col_idx + 1 < len(diagram[row_idx]):
                right = memo[col_idx + 1]
            if col_idx - 1 >= 0:
                left = memo[col_idx - 1]
            memo[col_idx] = left + right

#print(memo)
print(f"Part 2: {memo[start_idx]}")