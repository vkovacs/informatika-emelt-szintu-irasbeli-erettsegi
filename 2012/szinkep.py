input_file = open("kep.txt")

pixels = []

for line in input_file.readlines():
    split_line = line.strip().split(" ")
    pixels.append(tuple(split_line))

pixels_multi_dimensional_list = []

for i in range(0, 2500, 49):
    pixels_multi_dimensional_list.append(pixels[i:i + 50])

print(pixels_multi_dimensional_list)
