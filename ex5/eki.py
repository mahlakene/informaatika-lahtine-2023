import sys

total_tests = sys.stdin.readlines()[1:][:-1]
lines = sys.stdin.readlines()[1:]


def do_something(i, M, N):
    countries = {}
    country = 1
    for j in lines[i + 1: i + N + 1]:
        countries[country] = int(j[:-1].split()[2])
        country += 1
    for j in lines[i + N + 1: i + M + 1 + N]:
        a = int(j[:-1].split()[0])
        b = int(j[:-1].split()[1])
        if countries[a] > countries[b]:
            continue
        else:
            return "EI"
    return "JAH"

next_start = 1

for i, line in enumerate(lines):
    if i != next_start:
        continue
    N = int(line[:-1].split()[0])
    M = int(line[:-1].split()[1])
    print(do_something(i, M, N))
    next_start = i + N + M + 1
