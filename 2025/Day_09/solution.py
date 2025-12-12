from functools import cache

locations = []
vertical_line_segments = []
horizontal_line_segments = []

with open('input.txt', 'r') as f:
    content = f.read()
    lines = content.strip().split('\n')

for location in lines:
    x, y = map(int, location.split(','))
    locations.append((x, y))

area = 0
for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        area = max(area, (abs(locations[i][0] - locations[j][0]) + 1) * (abs(locations[i][1] - locations[j][1]) + 1))

print(f"Part 1: {area}")

@cache
def is_inside(x, y):
    for line_segment in horizontal_line_segments:
        if y == line_segment[0][1]:
            if x <= line_segment[0][0] and x >= line_segment[1][0]:
                return True
            elif x >= line_segment[0][0] and x <= line_segment[1][0]:
                return True

    num_lines_crossed = 0
    for line_segment in vertical_line_segments:
        if x == line_segment[0][0]:
            if y <= line_segment[0][1] and y >= line_segment[1][1]:
                return True
            elif y >= line_segment[0][1] and y <= line_segment[1][1]:
                return True
        elif x < line_segment[0][0]:
            if y == line_segment[0][1]:
                if line_segment[1][1] < line_segment[0][1]:
                    num_lines_crossed += 1
            elif y == line_segment[1][1]:
                if line_segment[0][1] < line_segment[1][1]:
                    num_lines_crossed += 1
            elif y >= line_segment[0][1] and y <= line_segment[1][1]:
                num_lines_crossed += 1
            elif y <= line_segment[0][1] and y >= line_segment[1][1]:
                num_lines_crossed += 1
    return num_lines_crossed % 2 == 1

def test_rectangle(corner1, corner2):
    #print(f"Testing rectangle from {corner1} to {corner2}")
    min_x = min(corner1[0], corner2[0])
    max_x = max(corner1[0], corner2[0])
    min_y = min(corner1[1], corner2[1])
    max_y = max(corner1[1], corner2[1])
    for x in range(min_x, max_x + 1):
        if not is_inside(x, min_y):
            #print(f"Point {x}, {min_y} is not inside")
            return False
        if not is_inside(x, max_y):
            #print(f"Point {x}, {max_y} is not inside")
            return False
    for y in range(min_y, max_y + 1):
        if not is_inside(min_x, y):
            #print(f"Point {min_x}, {y} is not inside")
            return False
        if not is_inside(max_x, y):
            #print(f"Point {max_x}, {y} is not inside")
            return False
    return True

locations.append(locations[0])
for i in range(1, len(locations)):
# for each adjacent pair, create a list of line segments if they are vertical
    if locations[i][0] == locations[i-1][0]:
        vertical_line_segments.append(((locations[i][0], locations[i][1]), (locations[i-1][0], locations[i-1][1])))
    elif locations[i][1] == locations[i-1][1]:
        horizontal_line_segments.append(((locations[i][0], locations[i][1]), (locations[i-1][0], locations[i-1][1])))
locations.pop()

#print(vertical_line_segments)
#print(horizontal_line_segments)

area = 0
for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        if test_rectangle(locations[i], locations[j]):    
            new_area = (abs(locations[i][0] - locations[j][0]) + 1) * (abs(locations[i][1] - locations[j][1]) + 1)  
            area = max(area, new_area)

print(f"Part 2: {area}")
