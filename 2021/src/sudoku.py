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