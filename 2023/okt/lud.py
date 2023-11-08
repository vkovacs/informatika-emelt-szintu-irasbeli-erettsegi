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

# 4. feladat

chosen_path_index = 8  # FIXME: read from user input
player_count = 5  # FIXME: read from user input

# 5. feladat

field_dict = {"M": 0, "E": 0, "V": 0}

for field in paths[chosen_path_index]:
    field_dict[field] += 1

print(field_dict)

# 6. feladat
position = 0    # I guess they want to have the positions indexed from 1 not form 0, so I'm using value 0 here and immediately increase it by 1 in the loop
special_character_lines = []
for field in paths[chosen_path_index]:
    position += 1
    if field in ["E", "V"]:
        special_character_lines.append(f"{position} \t {field}")

print(special_character_lines)  # FIXME: write result to file
