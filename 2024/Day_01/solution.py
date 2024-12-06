from collections import Counter

with open('input.txt', 'r') as f:
    content = f.read()

    list1 = []
    list2 = []
    
    for line in content.strip().split('\n'):
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

    list1.sort()
    list2.sort()
    counter = Counter(list2)

    distance = 0
    similarity = 0
    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i])
        similarity += list1[i] * counter[list1[i]]

    print(f"Distance: {distance}, Similarity: {similarity}")

