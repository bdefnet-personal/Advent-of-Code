INCLUDE_DO_DONT = True

with open('input.txt', 'r') as f:
    content = f.read()

    import re
    pattern = r'mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)'

    enabled = True
    total = 0

    for m in re.finditer(pattern, content):
        if m[0].startswith('mul'):
            if enabled:
                total += int(m[1]) * int(m[2])
        elif INCLUDE_DO_DONT:
            if m[0].startswith("don't"):
                enabled = False
            else:
                enabled = True    

    print(f"Total: {total}")

