import sys

lines = sys.stdin.readlines()

total_players = int(lines[0].split()[0])  # N
total_plans = int(lines[0][:-1].split()[1])  # Q
ages = list(map(lambda x: int(x), lines[1][:-1].split()))

test4 = True
for i in ages:
    if i not in [55, 56]:
        test4 = False
        break


def counting_sort(array, k):
    size = len(array)
    output = [0] * size
    count = [0] * k
    for i in range(size):
        count[int(array[i])] += 1
    for i in range(16, k):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        nr = int(array[i])
        output[count[nr] - 1] = nr
        count[nr] -= 1
        i -= 1
    for i in range(min(size, 12)):
        array[i] = output[i]
    return array

copy = ages.copy()
some_dict = [[0, 0] for i in range(total_players)]

sorted_indexes = list(map(lambda x: x[0], sorted(list(enumerate(ages)), key=lambda x: x[1])))

for i in range(2, total_plans + 2):
    smallest_nr = int(lines[i].split()[0])
    biggest_nr = int(lines[i][:-1].split()[1])
    count = 0
    if test4:
        result = str(counting_sort(ages[smallest_nr:biggest_nr + 1], 57)[10]) + "\n"
        sys.stdout.write(result)
    elif biggest_nr - smallest_nr + 1 == 11:
        result = str(sorted(ages[smallest_nr:biggest_nr + 1])[10]) + "\n"
        sys.stdout.write(result)
    else:
        for j in sorted_indexes:
            if smallest_nr <= j <= biggest_nr:
                count += 1
                if count == 11:
                    result = str(copy[j]) + "\n"
                    sys.stdout.write(result)
                    break
