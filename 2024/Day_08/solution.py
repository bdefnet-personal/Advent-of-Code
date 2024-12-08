
def locate_antinodes(antennas, antinodes, part2):
    for antenna_type in antennas:
        for i in range(len(antennas[antenna_type])):
            for j in range(i + 1, len(antennas[antenna_type])):
                a1 = antennas[antenna_type][i]
                a2 = antennas[antenna_type][j]
                if part2:
                    antinodes.add(a1)
                    antinodes.add(a2)

                diff1 = (a2[0] - a1[0], a2[1] - a1[1])
                diff2 = (a1[0] - a2[0], a1[1] - a2[1])

                count = 0
                while True:
                    count += 1
                    n1 = (a2[0] + diff1[0] * count, a2[1] + diff1[1] * count)

                    if n1[0] < max_row and n1[1] < max_col and n1[0] >= 0 and n1[1] >= 0:
                        antinodes.add(n1)
                    else:
                        break

                    if not part2:
                        break

                count = 0
                while True:
                    count += 1
                    n2 = (a1[0] + diff2[0] * count, a1[1] + diff2[1] * count)
                    if n2[0] < max_row and n2[1] < max_col and n2[0] >= 0 and n2[1] >= 0:
                        antinodes.add(n2)
                    else:
                        break

                    if not part2:
                        break

with open('input.txt', 'r') as f:
    content = f.read()
    lines = content.strip().split('\n')

    antennas = {}

    max_row = len(lines)
    max_col = len(lines[0])

    for row in range(max_row):
        for col in range(max_col):
            if lines[row][col] != '.':
                if lines[row][col] not in antennas:
                    antennas[lines[row][col]] = []
                antennas[lines[row][col]].append((row, col))

    antinodes = set()
    locate_antinodes(antennas, antinodes, False)
    print(f"Part1: {len(antinodes)} uniqueantinodes")

    antinodes = set()
    locate_antinodes(antennas, antinodes, True)
    print(f"Part2: {len(antinodes)} uniqueantinodes")
