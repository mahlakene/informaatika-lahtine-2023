import math
import sys

"""lines = sys.stdin.readlines()
cuboid = list(map(int, lines[0][:-1].split()))
ant = list(map(int, lines[1][:-1].split()))
honey = list(map(int, lines[2][:-1].split()))
x1 = ant[0]
x2 = honey[0]
y1 = ant[1]
y2 = honey[1]
z1 = ant[2]
z2 = honey[2]
"""
x1 = 3
x2 = 4
y1 = 0
y2 = 3
z1 = 5
z2 = 2
cuboid = [4, 6, 8]

dx = abs(x1 - x2)
dy = abs(y1 - y2)
dz = abs(z1 - z2)



if x1 == x2 == 0 or x1 == x2 == cuboid[0]:
    print(math.sqrt((y2 - y1) ** 2 + (z2 - z1) ** 2))
    exit()
elif y1 == y2 == 0 or y1 == y2 == cuboid[1]:
    print(math.sqrt((x2 - x1) ** 2 + (z2 - z1) ** 2))
    exit()
elif z1 == z2 == 0 or z1 == z2 == cuboid[2]:
    print(math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))
    exit()

"""delta_x = abs(x1 - x2)
delta_y = abs(y1 - y2)
delta_z = abs(z1 - z2)
print(delta_x + delta_y + delta_z)"""

mid = None
distance1 = None
distance2 = None

if y1 == 0 and x2 == 0:
    mid = (0, (y2 + y1) / 2, (z1 + z2) / 2)

elif y1 == 0 and x2 == cuboid[0]:
    mid = (cuboid[0], (y2 + y1) / 2, (z1 + z2) / 2)

elif y1 == 0 and z2 == 0:
    mid = ((x1 + x2) / 2, (y2 + y1) / 2, 0)

elif y1 == 0 and z2 == cuboid[2]:
    mid = ((x1 + x2) / 2, (y2 + y1) / 2, cuboid[2])



elif x1 == 0 and x2 == 0:
    mid = (x1, (y1 + y2) / 2, (z1 + z2) / 2)


elif x1 == 0 and y2 == 0:
    mid = ((x1 + x2) / 2, (y1 + y2) / 2, z1)

elif x1 == 0 and z2 == 0:
    mid = ((x1 + x2) / 2, y1, (z1 + z2) / 2)

elif x1 == 0 and z1 == 0:
    mid = ((x1 + x2) / 2, (y1 + y2) / 2, z1)

elif z1 == 0 and x2 == 0:
    mid = (x1, (y1 + y2) / 2, (z1 + z2) / 2)

elif z1 == 0 and y2 == 0:
    mid = (x1, (y1 + y2) / 2, z1)

elif z1 == 0 and z2 == 0:
    mid = (x1, (y1 + y2) / 2, (z1 + z2) / 2)

elif z1 == 0 and x1 == 0:
    mid = (x1, (y1 + y2) / 2, z1)

print(distance1 + distance2)
