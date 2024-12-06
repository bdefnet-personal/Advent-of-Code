
def repaired_update(u, order_map):
    i = 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(u)):
            if u[i] not in order_map[u[i-1]]:
                u[i], u[i-1] = u[i-1], u[i]
                swapped = True
    return u

with open('input.txt', 'r') as f:
    content = f.read()
    lines = content.strip().split('\n')

    order_map = {}
    updates = []
    phase_1 = True
    for line in lines:
        if line == "":
            phase_1 = False
        elif phase_1:
            key, value = map(int, line.split('|'))
            if key not in order_map:
                order_map[key] = []
            order_map[key].append(value)
        else:
            updates.append(list(map(int, line.split(','))))

    first_pass_total = 0
    repaired_total = 0
    for u in updates:
        prev_page = u[0]
        bad = False
        for i in range(1, len(u)):
            if u[i] not in order_map[u[i-1]]:
                bad = True
                break;
        if not bad:
            first_pass_total += u[len(u) // 2]
        else:
            repaired_total += repaired_update(u, order_map)[len(u) // 2]

print(f"First Pass Total: {first_pass_total}, Repaired Total: {repaired_total}")
