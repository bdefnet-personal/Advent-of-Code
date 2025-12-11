import heapq

locations = []
distances = []

with open('input.txt', 'r') as f:
    content = f.read()
    lines = content.strip().split('\n')

for location in lines:
    x, y, z = map(int, location.split(','))
    locations.append((x, y, z))

for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        distance = abs((locations[i][0] - locations[j][0])**2) + abs((locations[i][1] - locations[j][1])**2) + abs((locations[i][2] - locations[j][2])**2)
        heapq.heappush(distances, (distance, i, j))

locations_remaining = len(locations)
circuits = []

def find_circuit(circuits, location):
    for i in range(len(circuits)):
        if location in circuits[i]:
            return i
    return None

#PART 1
for i in range(1000):
    connection = heapq.heappop(distances)
    #print(connection[0], locations[connection[1]], locations[connection[2]])
    circuit_idx_1 = find_circuit(circuits, connection[1])
    circuit_idx_2 = find_circuit(circuits, connection[2])
    if circuit_idx_1 is None and circuit_idx_2 is None:
        locations_remaining -= 2
        circuits.append([connection[1], connection[2]])
    elif circuit_idx_1 is None:
        locations_remaining -= 1
        circuits[circuit_idx_2].append(connection[1])
    elif circuit_idx_2 is None:
        locations_remaining -= 1
        circuits[circuit_idx_1].append(connection[2])
    else:
        if circuit_idx_1 != circuit_idx_2:
            circuits[circuit_idx_1].extend(circuits[circuit_idx_2])
            circuits.pop(circuit_idx_2)
        
circuits.sort(key=lambda x: len(x), reverse=True)
#print(locations_remaining)
#print(circuits)

answer = 1
for i in range(3):
    answer *= len(circuits[i])
print(f"Part 1: {answer}")

#PART 2
while locations_remaining > 0:
    connection = heapq.heappop(distances)
    #print(connection[0], locations[connection[1]], locations[connection[2]])
    circuit_idx_1 = find_circuit(circuits, connection[1])
    circuit_idx_2 = find_circuit(circuits, connection[2])
    if circuit_idx_1 is None and circuit_idx_2 is None:
        locations_remaining -= 2
        circuits.append([connection[1], connection[2]])
    elif circuit_idx_1 is None:
        locations_remaining -= 1
        circuits[circuit_idx_2].append(connection[1])
    elif circuit_idx_2 is None:
        locations_remaining -= 1
        circuits[circuit_idx_1].append(connection[2])
    else:
        if circuit_idx_1 != circuit_idx_2:
            circuits[circuit_idx_1].extend(circuits[circuit_idx_2])
            circuits.pop(circuit_idx_2)
    if locations_remaining == 0:
        #print("HERE", locations[connection[1]], locations[connection[2]])
        print(f"Part 2: {locations[connection[1]][0] * locations[connection[2]][0]})")
        break
