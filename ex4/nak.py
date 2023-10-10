"""import sys
lines = sys.stdin.readlines()
total_players = int(lines[0].split()[0])  # N
total_plans = int(lines[0][:-1].split()[1])  # Q
ages = list(map(int, lines[1][:-1].split()))"""

def counting_sort(array, k, elements_to_sort):
    size = len(array)
    elements_to_sort = min(size, elements_to_sort)
    output = [0] * size  # elements_to_sort
    count = [0] * k
    for i in range(0, size):
        count[array[i]] += 1

    for i in range(1, k):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:  # and elements_to_sort > 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
        elements_to_sort -= 1

    for i in range(0, size):
        array[i] = output[i]
    return array
print(counting_sort([1, 56, 2, 56,2,5,344,1,2,54,52], 345, 5))

for i in range(2, total_plans + 2):
    left_index = int(lines[i].split()[0])
    right_index = int(lines[i][:-1].split()[1]) + 1
    print(counting_sort(ages[left_index:right_index], 57, 11)[10])
