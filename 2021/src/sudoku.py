print("1. feladat")
input_file_name = input("Adja meg a bemeneti file nevét: ")

input_file_path = "../resources/Forrasok/4_Sudoku/" + input_file_name

input_file = open(input_file_path)

for line in input_file.readlines():
    line.sp

selected_row_num = input("Adja meg egy sor számát: ")
selected_col_num = input("Adja meg egy oszlop számát: ")
