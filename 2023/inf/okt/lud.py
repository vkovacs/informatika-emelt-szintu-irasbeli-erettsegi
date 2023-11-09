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
position = 0  # I guess they want to have the positions indexed from 1 not form 0, so I'm using value 0 here and immediately increase it by 1 in the loop
special_character_lines = []
for field in paths[chosen_path_index]:
    position += 1
    if field in ["E", "V"]:
        special_character_lines.append(f"{position} \t {field}")

print(special_character_lines)  # FIXME: write result to file

# 7. feladat


is_game_finished = False
# player positions show the players position on the board, which board is indexed from 1
player_positions = [0 for _ in range(player_count)]  # https://www.w3schools.com/python/python_lists_comprehension.asp
actual_throw_index = -1
turn_count = -1
actual_player_index = 0

while not is_game_finished:
    actual_player_index = actual_player_index % player_count
    if actual_player_index == 0:
        turn_count += 1

    actual_throw_index += 1
    actual_throw = throws[actual_throw_index]

    player_positions[actual_player_index] += actual_throw

    if player_positions[actual_player_index] >= len(paths[chosen_path_index]):
        is_game_finished = True
    else:
        actual_player_index += 1

print(f"A játék a {turn_count + 1}. körben fejeződött be a játékot a {actual_player_index + 1}. játékos nyerte")

# 8. feladat
is_game_finished = False
# player positions show the players position on the board, which board is indexed from 1
player_positions = [0 for _ in range(player_count)]  # https://www.w3schools.com/python/python_lists_comprehension.asp
actual_throw_index = -1
turn_count = -1
actual_player_index = 0
chosen_path = paths[chosen_path_index]


def is_player_finished(player_position, path):
    return player_position >= len(path)


def is_any_player_finished(player_positions, path):
    for i in range(0, len(player_positions)):
        if is_player_finished(player_positions[i], path):
            return True

    return False


while not is_any_player_finished(player_positions, chosen_path) or not actual_player_index == player_count:
    actual_player_index = actual_player_index % player_count

    if actual_player_index == 0:
        turn_count += 1

    actual_throw_index += 1
    actual_throw = throws[actual_throw_index]

    thrown_new_player_position = player_positions[actual_player_index] + actual_throw
    # thrown_new_player_position is an index on the board (1 based indexed), but our board is represented in a list which is 0 based indexed!!
    thrown_new_player_position_index = thrown_new_player_position - 1

    if not is_player_finished(thrown_new_player_position, chosen_path):
        if chosen_path[thrown_new_player_position_index] == "E":
            player_positions[actual_player_index] += actual_throw * 2
        elif chosen_path[thrown_new_player_position_index] == "M":
            player_positions[actual_player_index] += actual_throw
    else:
        player_positions[actual_player_index] = thrown_new_player_position  # position NEEDS to be updated even there is no such position on board!!

    # print(f"{turn_count} {player_positions}")

    actual_player_index += 1

print(player_positions)

max_value_indices = [i for i, num in enumerate(player_positions) if num == max(player_positions)]

print(f"Győztesek: {[i + 1 for i in max_value_indices]}")

for i in range(0, player_count):
    if i not in max_value_indices:
        print(f"Játékos: {i + 1}, {player_positions[i]} mező.")
