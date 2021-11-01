print("1. feladat")

# input_file_name = input("Adja meg a bemeneti file nevét: ")
input_file_name = "konnyu.txt"

input_file_path = "../resources/Forrasok/4_Sudoku/" + input_file_name

input_file = open(input_file_path)

sudo_matrix_max_row_size = 9
sudo_matrix_max_col_size = 9

sudoku_matrix = [[0] * sudo_matrix_max_col_size] * sudo_matrix_max_row_size # https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/

line_counter = 0
for line in input_file.readlines():
    split_line = list(map(int, line.split())) # we want a matrix which contains ints not strings: https://stackoverflow.com/a/6429930

    if len(split_line) == 9:
        sudoku_matrix[line_counter] = split_line
        line_counter = line_counter + 1
    else:
        break

selected_row_num = int(input("Adja meg egy sor számát: "))
selected_col_num = int(input("Adja meg egy oszlop számát: "))
selected_row_index = selected_row_num - 1
selected_col_index = selected_col_num - 1

print("2. feladat")
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


print("A hely a(z) " + str(determine_sub_matrix_number(selected_row_index, selected_col_index)) + ". résztáblázathoz tartozik.")

print("Feladat 4.")

zero_count = 0
for i in range(sudo_matrix_max_col_size):
    for j in range(sudo_matrix_max_row_size):
        if sudoku_matrix[i][j] == 0:
            zero_count = zero_count + 1

print("Az üres helyek aránya: " + str(round((zero_count / 81) * 100, 1)))
