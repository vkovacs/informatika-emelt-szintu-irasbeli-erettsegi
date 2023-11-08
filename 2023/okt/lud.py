# 1. feladat
throws_input_file = open("dobasok.txt")
paths_input_file = open("osvenyek.txt")


throws = []
for element in throws_input_file.readlines()[0].strip().split(" "):
    throws.append(int(element))

paths = []
for lines in paths_input_file:
    line = lines.strip().split("\t")[0]
    paths.append(line)


print(throws)
print(paths)

# 2. feladat

print(f"A dobások száma: {len(throws)}")
print(f"Az ösvények száma: {len(paths)}")

# 3. feladat

min_path_index = 0

for path_index in range(1, len(paths)):
    if len(paths[path_index]) > len(paths[min_path_index]):
        min_path_index = path_index

print(f"Az egyik leghosszabb a(z) {min_path_index + 1} ösvény, hossza: {len(paths[min_path_index])}")