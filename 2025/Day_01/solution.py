with open('input.txt', 'r') as f:
    content = f.read()

    start = 50
    end_on_zero = 0
    passes_zero = 0

    for line in content.strip().split('\n'):
        direction = line[0]  # First character: 'L' or 'R'
        num = int(line[1:])  # Everything after first character as integer

        while num > 0:
            if direction == 'L':
                start -= 1
            else:
                start += 1
            num -= 1

            if start == 100:
                start = 0
            if start == -1:
                start = 99

            if start == 0:
                passes_zero += 1

        if start == 0:
            end_on_zero += 1

    print(f"End on zero: {end_on_zero}")
    print(f"Passes zero: {passes_zero}")

