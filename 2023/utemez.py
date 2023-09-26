from datetime import date

input_file = open("taborok.txt")

# 1. feladat
camps = []

for line in input_file.readlines():
    split_line = line.strip().split(
        "\t")  # strip: used to remove line end character "\n" which would just cause trouble later
    camps.append(split_line)

# 2. feladat
print("2. feladat")
print("Az adatsorok szama: {0}".format(len(camps)))
print("Az eloszor rogzitett tabor temaja: {}".format(camps[0][5]))
print("Az utoljara rogzitett tabor temaja: {}".format(camps[len(camps) - 1][5]))  # shorter version: camps[-1][5])     https://stackoverflow.com/a/930398

# 3. feladat
print("3. feladat")
music_camp_count = 0
for camp in camps:
    if camp[5] == "zenei":
        music_camp_count = music_camp_count + 1
        print("Zenei tabor kezdodik {0}. ho {1}. napjan".format(camp[0], camp[1]))

if music_camp_count == 0:
    print("Nem volt zenei tabor!")

# 4. feladat
print("4. feladat")
max_attendant_size = len(camps[0][4])
camp_index_with_max_attendant = [0]

for i in range(1, len(camps)):  # end parameter of range is exclusive     #https://docs.python.org/2/library/functions.html#range
    if len(camps[i][4]) > max_attendant_size:
        max_attendant_size = len(camps[i][4])
        camp_index_with_max_attendant = [i]
    elif len(camps[i][4]) == max_attendant_size:
        camp_index_with_max_attendant.append(i)

print("Legnepszerubbek: ")
for i in camp_index_with_max_attendant:
    print("{0} {1} {2}".format(camps[i][0], camps[i][1], camps[i][5]))

# 5. feladat
print("5. feladat")

def sorszam(month, day): # https://tecadmin.net/calculate-days-between-two-dates-in-python/
    dayStart = date(2023, 6, 16)
    actualDay = date(2023, month, day)

    return (actualDay - dayStart).days + 1 # add plus one because it calculates 2023.6.16 as the 0th day of holiday and we need it as the 1st day..

print("Aug 31 a nyariszunet {0}. napja".format(sorszam(8, 31)))

# 6. feladat
print("6. feladat")

user_month = 8  # should be user input, but I use predefined values for the sake of convenience
user_day = 1

camps_count_at_user_date = 0
for camp in camps:
    start = date(2023, int(camp[0]), int(camp[1]))
    end = date(2023, int(camp[2]), int(camp[3]))

    user_date = date(2023, int(user_month), int(user_day))

    if start <= user_date <= end:  # https://stackoverflow.com/a/5464467
        camps_count_at_user_date = camps_count_at_user_date + 1

print("Ekkor eppen {0} tabor tart.".format(camps_count_at_user_date))

# 7 feladat
print("7. feladat")

student_id = "L"
students_camps = []
for camp in camps:
    if student_id in camp[4]: # https://www.javatpoint.com/check-if-string-has-character-in-python
        start = date(2023, int(camp[0]), int(camp[1]))
        end = date(2023, int(camp[2]), int(camp[3]))

        students_camps.append([start, end, camp])


# https://www.w3schools.com/python/python_lambda.asp
# https://www.tutorialspoint.com/How-to-sort-a-Python-date-string-list
students_camps.sort(key = lambda camp : camp[0]) # sort by the 0.parameter of the parameter received by the lambda (which will be in date format)


# TODO: make it to write to file
for students_camp in students_camps:
    print("{}.{}-{}.{}. {}".format(students_camp[2][0], students_camp[2][1], students_camp[2][2], students_camp[2][3], students_camp[2][5]))