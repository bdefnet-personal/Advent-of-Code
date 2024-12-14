'''
Floor is 101 tiles wide, and 103 tiles tall
Positive x is to the right
Positive y is down

input: p=69,11 v=-25,6
'''

ITERATIONS = 100
FLOOR_WIDTH = 101
FLOOR_HEIGHT = 103

def part1(positions, velocities):
    quadrants = [0] * 4

    for i in range(len(positions)):
        positions[i][0] = (positions[i][0] + ITERATIONS * velocities[i][0]) % FLOOR_WIDTH
        positions[i][1] = (positions[i][1] + ITERATIONS * velocities[i][1]) % FLOOR_HEIGHT
        if positions[i][0] < FLOOR_WIDTH // 2 and positions[i][1] < FLOOR_HEIGHT // 2:
            quadrants[0] += 1
        elif positions[i][0] > FLOOR_WIDTH // 2 and positions[i][1] < FLOOR_HEIGHT // 2:
            quadrants[1] += 1
        elif positions[i][0] < FLOOR_WIDTH // 2 and positions[i][1] > FLOOR_HEIGHT // 2:
            quadrants[2] += 1
        elif positions[i][0] > FLOOR_WIDTH // 2 and positions[i][1] > FLOOR_HEIGHT // 2:
            quadrants[3] += 1
    score = 1
    for s in quadrants:
        score *= s
    print(f"Part 1 Safety Score: {score}")

def part2(positions, velocities):
    for j in range(ITERATIONS, 100000000):
        overlap_set = set()
        overlaps = False
        for i in range(len(positions)):
            positions[i][0] = (positions[i][0] + velocities[i][0]) % FLOOR_WIDTH
            positions[i][1] = (positions[i][1] + velocities[i][1]) % FLOOR_HEIGHT
            pos = (positions[i][0], positions[i][1])
            if pos in overlap_set:
                overlaps = True
            else:
                overlap_set.add(pos)

        #I'm going to assume that the way this image was generated was by starting with the image
        #and then running the velocities backwards for some number of iterations.  I'm assuming
        #this means that that frame with the image didn't have any robots overlapping.  Maybe
        #every other frame does???
        if not overlaps:
            canvas = []
            for row in range(FLOOR_HEIGHT):
                line = []
                for col in range(FLOOR_WIDTH):
                    line.append(".")
                canvas.append(line)

            for i in range(len(positions)):
                canvas[positions[i][1]][positions[i][0]] = "X"
            for row in range(FLOOR_HEIGHT):
                line = "".join(canvas[row])
                print(line)
            print(f"Part 2: Iteration {j+1}\n")
            break

    
with open('input.txt', 'r') as f:
    content = f.read()
    
    positions = []
    velocities = []

    import re
    pattern = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
    for m in re.finditer(pattern, content):
        positions.append([int(m[1]), int(m[2])])
        velocities.append([int(m[3]), int(m[4])])
        
    part1(positions, velocities)
    part2(positions, velocities)