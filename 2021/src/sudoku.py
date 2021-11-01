print("1. feladat")

# input_file_name = input("Adja meg a bemeneti file nevét: ")
input_file_name = "konnyu.txt"

input_file_path = "../resources/Forrasok/4_Sudoku/" + input_file_name

input_file = open(input_file_path)

sudo_matrix_row_size = 9
sudo_matrix_col_size = 9

sudoku_matrix = [[0] * sudo_matrix_col_size] * sudo_matrix_row_size # https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/


line_counter = 0
for line in input_file.readlines():
    split_line = line.split()

    if len(split_line) == 9:
        sudoku_matrix[line_counter] = split_line
        line_counter = line_counter + 1
    else:
        break

selected_row_num = input("Adja meg egy sor számát: ")
selected_col_num = input("Adja meg egy oszlop számát: ")
