
def recurse(answer, nums, subtotal, part_2):
    if len(nums) == 0:
        if subtotal == answer:
            return True
        else:
            return False
    if subtotal > answer:
        return False
    
    if recurse(answer, nums[1:], subtotal + nums[0], part_2):
        return True
    elif recurse(answer, nums[1:], subtotal * nums[0], part_2):
        return True
    elif part_2:
        if recurse(answer, nums[1:], int(str(subtotal) + str(nums[0])), part_2):
            return True
        
    return False
  
with open('input.txt', 'r') as f:
    content = f.read()
    answers = []
    numbers = []
    for line in content.strip().split('\n'):
        line = line.split(':')
        answers.append(int(line[0]))
        numbers.append([int(num) for num in line[1][1:].split(' ')])

    calibration_1 = 0
    calibration_2 = 0
    for i, a in enumerate(answers):
        if recurse(a, numbers[i], 0, False):
            #print(f"Part 1: Answer found for {i}: {a}")
            calibration_1 += a
            calibration_2 += a
        elif recurse(a, numbers[i], 0, True):
            #print(f"Part 2: Answer found for {i}: {a}")
            calibration_2 += a
    print(f"Part 1: {calibration_1}")
    print(f"Part 2: {calibration_2}")
