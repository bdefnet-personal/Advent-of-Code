
'''
If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
'''
NUM_BLINKS_1 = 25
NUM_BLINKS_2 = 75

with open('input.txt', 'r') as f:
    content = f.read()
    input_list = [int(c) for c in content.split(" ")]
    old_stones = {}
    for i, num in enumerate(input_list):
        if num not in old_stones:
            old_stones[num] = 0
        old_stones[num] += 1

    part_1_stones = 0
    part_2_stones = 0

    for i in range(NUM_BLINKS_2):
        new_stones = {}
        for num in old_stones:
            if num == 0:
                if 1 not in new_stones:
                    new_stones[1] = 0
                new_stones[1] += old_stones[num]
            elif len(str(num)) % 2 == 0:
                left_num = int(str(num)[:len(str(num))//2])
                right_num = int(str(num)[len(str(num))//2:])
                if left_num not in new_stones:
                    new_stones[left_num] = 0
                if right_num not in new_stones:
                    new_stones[right_num] = 0
                new_stones[left_num] += old_stones[num]
                new_stones[right_num] += old_stones[num]
            else:
                if num * 2024 not in new_stones:
                    new_stones[num * 2024] = 0
                new_stones[num * 2024] += old_stones[num]
        old_stones = new_stones
        if i == NUM_BLINKS_1-1:
            part_1_stones = sum(old_stones.values())
        if i == NUM_BLINKS_2-1:
            part_2_stones = sum(old_stones.values())
    
    print(f"Part 1:Num Stones: {part_1_stones}")
    print(f"Part 2:Num Stones: {part_2_stones}")
