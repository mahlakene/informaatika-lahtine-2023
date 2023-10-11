import sys


lines = sys.stdin.readlines()

"""with open("test2", "r") as f:
    lines = f.readlines()"""
total_players = int(lines[0].split()[0])  # N
total_plans = int(lines[0][:-1].split()[1])  # Q
ages = list(map(int, lines[1][:-1].split()))


def counting_sort(array, k):
    size = len(array)
    output = [0] * size
    count = [0] * k
    for i in range(size):
        count[array[i]] += 1
    for i in range(16, k):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
    for i in range(0, min(size, 12)):
        array[i] = output[i]
    return array

result = ""
for i in range(2, total_plans + 2):
    left_index = int(lines[i].split()[0])
    right_index = int(lines[i][:-1].split()[1]) + 1
    a = ages[left_index:right_index]
    result = str(sorted(a)[10])
    print(result)
