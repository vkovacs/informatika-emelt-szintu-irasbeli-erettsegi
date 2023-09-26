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
