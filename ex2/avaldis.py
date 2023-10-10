import sys
line = sys.stdin.readlines()[0][:-1].split()

a = int(line[0])
b = int(line[1])

if a == 0 and b == 0:
    print(0)
    exit()
result = ""
if not -1 <= a <= 1:
    result += str(a) + "x"
elif a == -1:
    result += "-x"
elif a == 1:
    result += "x"
if b == 0:
    print(result)
else:
    if b > 0 and result:
        result += "+" + str(b)
    else:
        result += str(b)
    print(result)
