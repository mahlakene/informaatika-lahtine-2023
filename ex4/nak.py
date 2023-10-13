import sys

# lines = sys.stdin.readlines()

with open("test3", "r") as f:
    lines = f.readlines()
total_players = int(lines[0].split()[0])  # N
total_plans = int(lines[0][:-1].split()[1])  # Q
ages = list(map(lambda x: int(x), lines[1][:-1].split()))
copy = ages.copy()
some_dict = [[0, 0] for i in range(total_players)]


sorted_indexes = list(map(lambda x: x[0], sorted(list(enumerate(ages)), key=lambda x: x[1])))

for i in range(2, total_plans + 2):
    smallest_nr = int(lines[i].split()[0])
    biggest_nr = int(lines[i][:-1].split()[1])
    count = 0
    for j in sorted_indexes:
        if smallest_nr <= j <= biggest_nr:
            count += 1
            if count == 11:
                result = str(copy[j]) + "\n"
                sys.stdout.write(result)
                break
