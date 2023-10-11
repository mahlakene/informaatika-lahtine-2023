import sys
import time

# lines = sys.stdin.readlines()

start = time.time()
with open("test2", "r") as f:
    lines = f.readlines()
total_players = int(lines[0].split()[0])  # N
total_plans = int(lines[0][:-1].split()[1])  # Q
ages = list(map(lambda x: int(x) - 16, lines[1][:-1].split()))
copy = ages.copy()
some_dict = [[0, 0] for i in range(total_players)]


def counting_sort(array, k):
    output = [0] * total_players
    count = [0] * k
    for i in range(total_players):
        count[array[i]] += 1

    for i in range(k):
        count[i] += count[i - 1]

    i = total_players - 1
    while i >= 0:  # elements_to_sort > 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, total_players):
        c = output[i]
        some_dict[i] = [c, None]
        array[i] = c
    return array


ages = counting_sort(ages, 42)
for i, j in enumerate(ages):
    if j != -1:
        b = copy.index(j)
        some_dict[i] = [j, b]
        copy[b] = -1

for i in range(2, total_plans + 2):
    smallest_nr = int(lines[i].split()[0])
    biggest_nr = int(lines[i][:-1].split()[1])
    count = 0
    for j in some_dict:
        if smallest_nr <= j[1] <= biggest_nr:
            count += 1
            if count == 11:
                print(j[0] + 16)
                break
finish = time.time()
print(f"TOTAL TIME: {finish - start}")
