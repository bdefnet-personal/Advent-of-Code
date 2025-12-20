fill_counts = [7, 7, 6, 7, 5, 7]

with open('input.txt', 'r') as f:
    content = f.read()
    lines = content.strip().split('\n')

    pass_count = 0
    for line in lines:
        if "x" in line:
            dimensions, raw_counts =line.split(":")
            x, y = map(int, dimensions.split("x"))

            trimmed_x = x - (x % 3)
            trimmed_y = y - (y % 3)

            counts = list(map(int, raw_counts.split()))

            min_needed = 0
            max_needed = 0
            for i in range(len(counts)):
                min_needed += counts[i] * fill_counts[i]
                max_needed += counts[i] * 9
            if max_needed <= (trimmed_x * trimmed_y):
                pass_count += 1
    
    print(f"Pass count: {pass_count}")