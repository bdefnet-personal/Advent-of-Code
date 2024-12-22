'''
In particular, each buyer's secret number evolves into the next secret number in the sequence via the following process:

Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, 
prune the secret number.
Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix 
this result into the secret number. Finally, prune the secret number.
Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, 
prune the secret number.
Each step of the above process involves mixing and pruning:

To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. 
Then, the secret number becomes the result of that operation. (If the secret number is 42 and you were to mix 15
 into the secret number, the secret number would become 37.)

To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number 
becomes the result of that operation. (If the secret number is 100000000 and you were to prune the secret number, 
the secret number would become 16113920.)'''

def generate_new_secrets(secret, num_iterations):
    new_secrets = [secret]

    for _ in range(num_iterations):
        secret = (secret * 64) ^ secret
        secret = secret % 16777216
        secret = (secret // 32) ^ secret
        secret = secret % 16777216
        secret = (secret * 2048) ^ secret
        secret = secret % 16777216
        new_secrets.append(secret)
        
    return new_secrets


with open('input.txt', 'r') as f:
    initial_secret_numbers = [int(x) for x in f.read().split("\n")]

    answer = 0

    profits = {}
    for secret in initial_secret_numbers:
        secrets = generate_new_secrets(secret, 2000)
        answer += secrets[-1]
        secrets = [x%10 for x in secrets]
        keys_for_this_monkey = set()
        for i in range(4, 2000):
            key = ""
            for j in range(4):
                key = str(secrets[i-j] - secrets[i-j-1]) + key
            if key not in keys_for_this_monkey:
                keys_for_this_monkey.add(key)
                if key not in profits:
                    profits[key] = secrets[i]
                else:
                    profits[key] += secrets[i]

    print(f"Part 1: = {answer}")
    best_key = max(profits, key=profits.get)
    print(f"Part 2: = {best_key} yields {profits[best_key]} bananas")
