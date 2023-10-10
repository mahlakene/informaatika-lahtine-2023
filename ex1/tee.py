import sys
line = sys.stdin.readlines()[0][:-1].split()
energy_to_heat = float(line[0])  # how much energy it takes to heat 1 degree
time_to_heat = float(line[1])  # how many seconds it takes to heat 1 degree
energy_to_keep_warm = float(line[2])  # how much energy it takes to keep water warm for 1 minute
cooling_degrees = float(line[3])  # how many degrees it cools down in one minute

print(round(energy_to_keep_warm * 60, 3))

max_time_to_heat = (time_to_heat * 78) / 60   # minutes
time_when_fully_cooled = 78 / cooling_degrees   # minutes

if time_when_fully_cooled < 60 - max_time_to_heat:
    print(78 * energy_to_heat)
else:
    a = max_time_to_heat / (time_when_fully_cooled + max_time_to_heat)
    minutes = 60 - max_time_to_heat + a * (time_when_fully_cooled - (60 - max_time_to_heat))
    print(round((60 - minutes) / (time_to_heat / 60) * energy_to_heat, 3))
