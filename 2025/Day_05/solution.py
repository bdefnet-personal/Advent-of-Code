'''
3-5
10-14
16-20
12-18

1
5
8
11
17
32
'''

def aggregate_ranges(ranges):
    aggregated_ranges = []
    for range in ranges:
        if aggregated_ranges == []:
            aggregated_ranges.append(range)
        else:
            if range[0] <= aggregated_ranges[-1][1] and range[1] >= aggregated_ranges[-1][0]:
                #merge them
                aggregated_ranges[-1] = (aggregated_ranges[-1][0], max(aggregated_ranges[-1][1], range[1]))
            else:
                aggregated_ranges.append(range)

    #print(f"aggregated ranges: {aggregated_ranges}")
    return aggregated_ranges

fresh_ranges = []
ingredients = []

with open('input.txt', 'r') as f:
    content = f.read()
    gathering_ranges = True
    for line in content.strip().split('\n'):
        if gathering_ranges and line == "":
            gathering_ranges = False
            continue

        if gathering_ranges:
            line = line.split('-')
            fresh_ranges.append((int(line[0]), int(line[1])))
        else:
            ingredients.append(int(line))

#sort the fresh ranges
fresh_ranges.sort(key=lambda x: x[0])

#print(f"fresh ranges: {fresh_ranges}")
#print(f"ingredients: {ingredients}")

aggregated_ranges = aggregate_ranges(fresh_ranges)
#print(f"aggregated ranges: {aggregated_ranges}")

fresh_count = 0
for ingredient in ingredients:
    for range in aggregated_ranges:
        if ingredient >= range[0] and ingredient <= range[1]:
            fresh_count += 1
            break

print(f"actual fresh count: {fresh_count}")

total_fresh_count = 0
for range in aggregated_ranges:
    total_fresh_count += ((range[1] - range[0]) + 1)

print(f"total fresh count: {total_fresh_count}")
