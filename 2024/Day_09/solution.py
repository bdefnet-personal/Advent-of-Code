
def solve_part_1(content_as_ints):

    my_content_as_ints = content_as_ints.copy()

    checksum = 0
    left_idx = 0
    right_idx = len(my_content_as_ints) - 1
    write_idx = 0
    left_id = 0
    right_id = len(my_content_as_ints) // 2

    while left_idx < right_idx:
        while my_content_as_ints[left_idx] > 0:
            checksum += write_idx * left_id
            write_idx += 1
            my_content_as_ints[left_idx] -= 1
            
        left_id += 1
        left_idx += 1

        while my_content_as_ints[left_idx] > 0:
            checksum += write_idx * right_id
            write_idx += 1
            my_content_as_ints[right_idx] -= 1
            my_content_as_ints[left_idx] -= 1
            if my_content_as_ints[right_idx] == 0:
                my_content_as_ints[right_idx - 1] = 0
                right_idx -= 2
                right_id -= 1
                if right_idx < left_idx:
                    break

        left_idx += 1

    while right_id >= left_id and my_content_as_ints[right_idx] > 0:
        checksum += write_idx * right_id
        write_idx += 1
        my_content_as_ints[right_idx] -= 1

    return checksum

def solve_part_2(content_as_ints):

    my_content_as_ints = content_as_ints.copy()

    checksum = 0
    left_idx = 0
    right_idx = len(my_content_as_ints) - 1
    write_idx = 0
    left_id = 0

    while left_idx <= right_idx:
        #if negative, that means we already moved this file to the left
        if my_content_as_ints[left_idx] < 0:
            write_idx += my_content_as_ints[left_idx]*-1
            #for i in range(my_content_as_ints[left_idx]*-1):
                #print(".")
        else:
            #write the left most unprocessed file
            while my_content_as_ints[left_idx] > 0:
                #print(left_id)
                checksum += write_idx * left_id
                write_idx += 1
                my_content_as_ints[left_idx] -= 1
            
        #now look to fill the next space
        left_id += 1
        left_idx += 1

        if left_idx > right_idx:
            break

        temp_right_idx = right_idx
        while True:
            #find the right most file that can be moved, in entirety, into this left-most space
            right_id = -1
            while temp_right_idx > left_idx:
                if my_content_as_ints[temp_right_idx] > 0 and my_content_as_ints[temp_right_idx] <= my_content_as_ints[left_idx]:
                    #found it
                    right_id = temp_right_idx // 2
                    break
                else:
                    temp_right_idx -= 2
                    
            if right_id != -1:
                #found one, write it
                while my_content_as_ints[temp_right_idx] > 0:
                    #print(right_id)
                    checksum += write_idx * right_id
                    write_idx += 1
                    my_content_as_ints[temp_right_idx] -= 1
                    my_content_as_ints[left_idx] -= 1
                #change this size of this file to negative, so we know it's been moved
                my_content_as_ints[temp_right_idx] = content_as_ints[temp_right_idx] * -1
                #now try the parent "while True" loop again in case there are more files that can fit into the remaining space
            else:
                #didn't find one, so we'll just leave these as spaces
                #for i in range(my_content_as_ints[left_idx]):
                    #print(".")
                break;


        write_idx += my_content_as_ints[left_idx]
        left_idx += 1

    return checksum



with open('input.txt', 'r') as f:
    content = f.read()
    content_as_ints = [int(c) for c in content]

print(f"Part 1: {solve_part_1(content_as_ints)}")
print(f"Part 2: {solve_part_2(content_as_ints)}")
