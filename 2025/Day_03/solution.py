def calc_joltage_1(bank):
    best_left = 0
    best_right = 0

    for battery in bank[:len(bank) - 1]:
        value = int(battery)
        if value > best_left:
            best_left = value
            best_right = 0
        elif value > best_right:
            best_right = value

        if int(bank[-1])> best_right:
            best_right = int(bank[-1])

    #print(f"Best left: {best_left}, Best right: {best_right}")
    return 10 * best_left + best_right

def calc_joltage_2(bank):
    len_bank = len(bank)
    best = bank[len_bank - 12:]
    
    for battery in bank[len_bank - 13::-1]:
        if battery >= best[0]:
            smallest = 10
            smallest_index = 0
            for i in range(len(best)):
                if int(best[i]) < smallest:
                    smallest = int(best[i])
                    smallest_index = i
                elif int(best[i]) > smallest:
                    break

            best = str(battery) + best[0:smallest_index] + best[smallest_index + 1:]

    #print(f"Best: {best}")
    return int(best)

with open('input.txt', 'r') as f:
    content = f.read()

    total_joltage_1 = 0
    total_joltage_2 = 0

    for bank in content.strip().split('\n'):
        total_joltage_1 += calc_joltage_1(bank)
        total_joltage_2 += calc_joltage_2(bank)

    print(f"Total joltage 1: {total_joltage_1}")
    print(f"Total joltage 2: {total_joltage_2}")
