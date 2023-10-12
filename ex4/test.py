import random

with open("test2", "w") as f:
    """f.write(f"{2 * (10 ** 5)} {3 * (10 ** 5)}\n")
    second_line = ""
    for i in range(2 * (10 ** 5)):
        second_line += " " + str(random.randint(16, 56))
    second_line = second_line[1:] + "\n"
    f.write(second_line)
    for i in range(3 * (10 ** 5)):
        a = random.randint(0, 2 * (10 ** 5) - 15)
        b = random.randint(a + 11, 2 * (10 ** 5))
        f.write(f"{a} {b}\n")"""


with open("test3", "w") as f:
    f.write("1000 1000\n")
    second_line = ""
    for i in range(100000):
        second_line += " " + str(random.randint(16, 56))
    second_line = second_line[1:] + "\n"
    f.write(second_line)
    for i in range(10000):
        a = random.randint(0, 100000 - 15)
        b = random.randint(a + 11, 100000)
        f.write(f"{a} {b}\n")

