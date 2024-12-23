

def trace_path(connections, target, current, depth, path, all_sets):
    path = path + current

    if depth == 0:
        if target in connections[current]:
            new_set = frozenset(path.split(","))
            all_sets.add(new_set)
        return
        
    for connection in connections[current]:
        if connection in path:
            continue
        trace_path(connections, target, connection, depth-1, path + ",", all_sets)

'''
algorithm BronKerbosch1(R, P, X) is
    if P and X are both empty then
        report R as a maximal clique
    for each vertex v in P do
        BronKerbosch1(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
        P := P - {v}
        X := X ⋃ {v}
'''
def BronKerbosch(R, P, X, best_set):
    if not P and not X:
        if len(R) > len(best_set):
            best_set.clear()
            best_set.update(R)
            #print(f"New maximal clique: {R}")
        return
    P_copy = P.copy()
    X_copy = X.copy()
    for v in P_copy.copy():
        P_copy.remove(v)
        BronKerbosch(R.union({v}), P_copy.intersection(connections_per_user[v]), X.intersection(connections_per_user[v]), best_set)
        X_copy.add(v)

with open('input.txt', 'r') as f:
    connections = []
    for line in f.readlines():
        line = line.strip()
        connections.append((line[:2], line[3:5]))

    connections_per_user = {}
    for a, b in connections:
        if a in connections_per_user:
            connections_per_user[a].append(b)
        else:
            connections_per_user[a] = [b]
        if b in connections_per_user:
            connections_per_user[b].append(a)
        else:
            connections_per_user[b] = [a]

    all_sets = set()
    for user in connections_per_user:
        if user.startswith('t'):
            trace_path(connections_per_user, user, user, 2, "", all_sets)

    print(f"Part 1: {len(all_sets)}")

    best_set = set()
    R = set()
    P = set(connections_per_user.keys())
    X = set()
    BronKerbosch(R, P, X, best_set)
    password = ",".join(sorted(best_set))

    print(f"Part 2: {password}")


