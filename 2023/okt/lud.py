# 1. feladat
throws_input_file = open("dobasok.txt")
paths_input_file = open("osvenyek.txt")


def read_file(file, delimiter):
    elements = []

    for line in file.readlines():
        split_line = line.strip().split(delimiter)  # strip: used to remove line end character "\n" which would just cause trouble later
        elements.append(split_line)

    return elements


throws = read_file(throws_input_file, " ")[0]
paths = read_file(paths_input_file, "\t")

print(throws)
print(paths)

# 2. feladat

print(f"A dobások száma: {len(throws)}")
print(f"Az ösvények száma: {len(paths)}")