print("1. feladat")

input_file_name = input("Adja meg a bemeneti file nevét: ")

input_file_path = "../resources/Forrasok/4_Sudoku/" + input_file_name

input_file = open(input_file_path)

sudoku_matrix_max_row_size = 9
sudoku_matrix_max_col_size = 9

sudoku_matrix = [[
                     0] * sudoku_matrix_max_col_size] * sudoku_matrix_max_row_size  # https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/

move_list = []

line_counter = 0
for line in input_file.readlines():
    split_line = list(
        map(int, line.split()))  # we want a matrix which contains ints not strings: https://stackoverflow.com/a/6429930

    if len(split_line) == 9:
        sudoku_matrix[line_counter] = split_line
        line_counter = line_counter + 1
    else:
        move_list.append(split_line)

selected_row_num = int(input("Adja meg egy sor számát: "))
selected_col_num = int(input("Adja meg egy oszlop számát: "))
selected_row_index = selected_row_num - 1
selected_col_index = selected_col_num - 1

print("3. feladat")
print("Az adott helyen szereplő szám: ")
value_in_selected_position = sudoku_matrix[selected_row_index][selected_col_index]

if value_in_selected_position > 0:
    print(value_in_selected_position)
else:
    print("Az adott helyet még nem töltötték ki.")


def determine_sub_matrix_number(row_index, col_index):
    sub_matrix_number = (col_index // 3) + 1  # div https://www.geeksforgeeks.org/division-operator-in-python/
    sub_matrix_number = sub_matrix_number + (row_index // 3) * 3
    return sub_matrix_number


print("A hely a(z) " + str(
    determine_sub_matrix_number(selected_row_index, selected_col_index)) + ". résztáblázathoz tartozik.")

print("4. Feladat")

zero_count = 0
for i in range(sudoku_matrix_max_col_size):
    for j in range(sudoku_matrix_max_row_size):
        if sudoku_matrix[i][j] == 0:
            zero_count = zero_count + 1

print("Az üres helyek aránya: " + str(round((zero_count / 81) * 100, 1)))

print("5. Feladat")


def positions_in_selected_row(row_index):
    positions = []
    for i in range(9):
        positions.append((row_index, i))

    return positions


def positions_in_selected_col(col_index):
    positions = []
    for i in range(9):
        positions.append((i, col_index))

    return positions


def positions_in_selected_sub_matrix(sub_matrix):  # not effective solution
    positions = []
    for i in range(sudoku_matrix_max_row_size):
        for j in range(sudoku_matrix_max_col_size):
            if determine_sub_matrix_number(i, j) == sub_matrix:
                positions.append((i, j))

    return positions


def validate_positions(positions):
    for position in positions:
        if sudoku_matrix[position[0]][position[1]] == move_value:
            return False

    return True


for move in move_list:
    move_value = move[0]
    move_row_index = move[1] - 1  # -1 is there since this is going to be an index of the sudoku_matrix which is indexed from 0 not 1
    move_col_index = move[2] - 1

    print(f"A kiválasztott sor {move[1]}: oszlop {move[2]}, a megadott szám: {move_value}")
    if sudoku_matrix[move_row_index][move_col_index] != 0:
        print("A helyet már kitöltötték")
        continue

    if not validate_positions(positions_in_selected_row(move_row_index)):
        print("Az adott sorban már szerepel a szám!")
        continue

    if not validate_positions(positions_in_selected_col(move_col_index)):
        print("Az adott oszlopban már szerepel a szám!")
        continue

    if not validate_positions(positions_in_selected_sub_matrix(determine_sub_matrix_number(move_row_index, move_col_index))):
        print("Az adott résztáblázatban már szerepel a szám!")
        continue

    print("A lépés megtehető!")