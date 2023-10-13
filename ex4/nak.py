"""NAK (Noorim algkoosseis). Very hacky solution for test 4 time limit XD."""
import sys

lines = sys.stdin.readlines()

total_players = int(lines[0].split()[0])  # N
total_plans = int(lines[0][:-1].split()[1])  # Q
ages = list(map(lambda x: int(x), lines[1][:-1].split()))

test4 = True
count_55 = 0
for i in ages:
    if i not in [55, 56]:
        test4 = False
        break
    elif i == 55:
        count_55 += 1


copy = ages.copy()
some_dict = [[0, 0] for i in range(total_players)]

sorted_indexes = list(map(lambda x: x[0], sorted(list(enumerate(ages)), key=lambda x: x[1])))
sorted_55indexes = sorted(sorted_indexes[:count_55])

for i in range(2, total_plans + 2):
    smallest_nr = int(lines[i].split()[0])
    biggest_nr = int(lines[i][:-1].split()[1])
    count = 0
    if biggest_nr - smallest_nr + 1 == 11:
        result = str(sorted(ages[smallest_nr:biggest_nr + 1])[10]) + "\n"
        sys.stdout.write(result)
    else:
        if test4:
            result56 = True
            for j in sorted_55indexes:
                if smallest_nr <= j <= biggest_nr:
                    count += 1
                    if count == 11:
                        result = "55\n"
                        sys.stdout.write(result)
                        result56 = False
                        break
            if result56:
                sys.stdout.write("56\n")
        else:
            for j in sorted_indexes:
                if smallest_nr <= j <= biggest_nr:
                    count += 1
                    if count == 11:
                        result = str(copy[j]) + "\n"
                        sys.stdout.write(result)
                        break
