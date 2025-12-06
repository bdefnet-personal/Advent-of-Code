with open('input.txt', 'r') as f:
    content = f.read()

    invalid_sum = 0

    for id_range in content.strip().split(','):
        start, end = id_range.split('-')
        #print(start, end)

        len_start = len(start)
        len_first_half = len_start // 2
        
        if len_start % 2 == 1:
            first_half = str(10 ** (len_first_half))
        else:
            first_half = start[:len_first_half]

        test_number = int(first_half + first_half)
        while test_number <= int(end):
            if test_number <= int(end):
                if test_number >= int(start):
                    #print(f"Invalid: {test_number}")
                    invalid_sum += test_number
            else:
                break
            first_half = str(int(first_half) + 1)
            test_number = int(first_half + first_half)

    print(f"Part 1 - Invalid sum: {invalid_sum}")

    invalid_sum = 0

    for id_range in content.strip().split(','):
        start, end = id_range.split('-')
        #print(start, end)

        invalid_set = set()
        number = 1
        end_test = int(end[:(len(end)+1)//2])
        while number <= end_test:
            test_str = str(number)
            while int(test_str) <= int(end):
                test_str += str(number)
                test_number = int(test_str)
                if test_number <= int(end):
                    if test_number >= int(start):
                        invalid_set.add(test_number)
                else:
                    break
            number += 1

        for invalid in invalid_set:
            invalid_sum += invalid

    print(f"Part 2 - Invalid sum: {invalid_sum}")
