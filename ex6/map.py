from PIL import Image, ImageDraw

file = "testid.windows/input_009.txt"
map = []
with open(file, "r") as f:
    for i in f.readlines()[1:]:
        map.append([char for char in i[:-1]])


rows = 57
columns = 361
height = 570
width = 3610
image = Image.new(mode='RGB', size=(width, height), color=255)

# Draw some lines
draw = ImageDraw.Draw(image)
y_start = 0
y_end = image.height
step_size_horizontal = int(image.width / columns)
step_size_vertical = int(image.height / rows)

yellow = "#FFFF00"
blue = "#0000FF"
red = "#ff0000"
gray = "#808080"
white = "#FFFFFF"

for i, y in enumerate(map):
    for j, x in enumerate(y):
        x1 = j * step_size_horizontal
        x2 = x1 + step_size_horizontal
        y1 = i * step_size_vertical
        y2 = y1 + step_size_vertical
        if x == "o":
            draw.rectangle([x1, y1, x2, y2], fill=blue)
        elif x == "x":
            draw.rectangle([x1, y1, x2, y2], fill=red)
        elif x == "#":
            draw.rectangle([x1, y1, x2, y2], fill=gray)
        elif x == "S":
            draw.rectangle([x1, y1, x2, y2], fill=yellow)
        else:
            draw.rectangle([x1, y1, x2, y2], fill=white)

for x in range(0, image.width, step_size_horizontal):
    line = ((x, y_start), (x, y_end))
    draw.line(line, fill=128)

x_start = 0
x_end = image.width

for y in range(0, image.height, step_size_vertical):
    line = ((x_start, y), (x_end, y))
    draw.line(line, fill=128)

result_string = ""
"""sonic_location = [9, 8]
finish = [76, 56]
result_string = ""
while sonic_location != finish:
    print(sonic_location)
    last = sonic_location
    x = sonic_location[0]
    y = sonic_location[1]
    if len(map[y]) > x + 1 and map[y][x + 1] == "o":
        sonic_location = [x + 1, y]
        result_string += "R"
    elif x - 1 >= 0 and map[y][x - 1] == "o":
        sonic_location = [x - 1, y]
        result_string += "L"
    elif y - 1 >= 0 and map[y - 1][x] == "o":
        sonic_location = [x, y - 1]
        result_string += "U"
    else:
        sonic_location = [x, y + 1]
        result_string += "D"
    map[last[1]][last[0]] = "x" """

#with open("output/output_003.txt", "w") as f:
#    f.write(result_string)

file = "output/output_007.txt"
with open(file, "r") as f:
    moves = f.readlines()[0]
location = [1, 0]

for move in moves:
    if move == " ":
        break
    if move == "L":
        location[0] -= 1
    elif move == "R":
        location[0] += 1
    elif move == "U":
        location[1] -= 1
    else:
        location[1] += 1
    x1 = location[0] * step_size_horizontal
    x2 = x1 + step_size_horizontal
    y1 = location[1] * step_size_vertical
    y2 = y1 + step_size_vertical
    #draw.rectangle([x1, y1, x2, y2], fill="#008000")


#image.paste(green_image, (0, 0))
del draw

image.show()
