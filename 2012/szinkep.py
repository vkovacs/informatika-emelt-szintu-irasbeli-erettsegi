# 1
input_file = open("kep.txt")

colors = []

for line in input_file.readlines():
    split_line = line.strip().split(" ")
    integer_list = [int(s) for s in split_line]  # the tuples should contain ints not strings
    colors.append(tuple(integer_list))

colors_multi_dimensional_list = []

for i in range(0, 2500, 49):
    colors_multi_dimensional_list.append(colors[i:i + 50])


# 2
def isColorPresent(color):
    for row in colors_multi_dimensional_list:
        if color in row:
            return True
    return False


user_pixel_present = (200, 96, 64)
assert isColorPresent(user_pixel_present)
user_pixel_not_present = (123, 123, 123)
assert not isColorPresent(user_pixel_not_present)


# 3
def countColorInRow(color, rowIndex):
    return colors_multi_dimensional_list[rowIndex].count(color)


def countColorInColumn(color, colIndex):
    colorCounter = 0
    for i in range(0, 50):
        if (colors_multi_dimensional_list[i][7] == color):
            colorCounter = colorCounter + 1

    return colorCounter


colorToCount = colors_multi_dimensional_list[34][7]
print(f"Sorban: {countColorInRow(colorToCount, 34)} Oszlopban: {countColorInColumn(colorToCount, 7)}")

# 4
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

redCount = 0
for i in range(0, 50):
   redCount = redCount + countColorInRow(red, i)

greenCount = 0
for i in range(0, 50):
   greenCount = greenCount + countColorInRow(green, i)

blueCount = 0
for i in range(0, 50):
   blueCount = blueCount + countColorInRow(blue, i)

maxColor = "Piros"
if greenCount > redCount:
    maxColor = "Zöld"
if (blueCount > greenCount):
    maxColor = "Kék"

print(f"A piros színből {redCount} a zöld színből {greenCount} a kék színből {blueCount} darab van a képen. Tehát a legtöbb szín {maxColor}-ból van.")