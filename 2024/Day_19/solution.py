def test_pattern(towels, pattern, pattern_cache):
    if not pattern:
        return 1
    
    if pattern in pattern_cache:
        return pattern_cache[pattern]
    
    num_good_combos = 0
    for t in towels:
        if pattern.startswith(t):
            num_good_combos += test_pattern(towels, pattern[len(t):], pattern_cache)

    pattern_cache[pattern] = num_good_combos
    
    return num_good_combos


with open('input.txt', 'r') as f:
    towels = [t for t in f.readline().strip().split(", ")]
    f.readline()
    patterns = []
    while line := f.readline():
        patterns.append(line.strip())

    valid_patterns = 0
    total_num_combos = 0
    idx = 0

    pattern_cache = {}
    for p in patterns:
        num_combos = test_pattern(towels, p, pattern_cache)
        if num_combos > 0:
            valid_patterns += 1
            total_num_combos += num_combos
            print(f"Pattern {idx} is valid.  Num Combos = {num_combos}")
        else:
            print(f"Pattern {idx} is invalid")
        idx += 1

    print(f"Part 1: Num Valid Patterns = {valid_patterns}")
    print(f"Part 2: Total Num Combos = {total_num_combos}")