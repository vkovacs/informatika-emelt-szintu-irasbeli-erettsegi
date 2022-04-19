# 1
base_path = "../resources/Forrasok/4_Nezoter"  # Relative paths are relative to current working directory


def read_file(path):
    result = list()
    for line in open(path).readlines():
        result.append(list(line.strip()))

    return result


reservations = read_file(base_path + "/foglaltsag.txt")
price_categories = read_file(base_path + "/kategoria.txt")

print(reservations)
print(price_categories)

# 2

# line = int(input("Sor: "))
# col = int(input("Sorszám: "))

line = 1
col = 1

seat_status = "üres" if reservations[line - 1][col - 1] == "o" else "foglalt"
print("A megadott szék " + seat_status)

# 3
sum_reserved = 0
all_seats_count = 0
for reservation_line in reservations:
    sum_reserved = sum_reserved + reservation_line.count("o")
    all_seats_count = all_seats_count + len(reservation_line)

print(f"Az előadásra eddig {sum_reserved} jegyet adtak el, ez a nézőtér {round(sum_reserved / all_seats_count * 100)} %-a.")

# 4
reserved_seat_count_by_category = {}

for i in range(len(reservations)):
    for j in range(len(reservations[i])):
        if reservations[i][j] == "x":
            price_category = price_categories[i][j]
            reserved_seat_count_by_category[price_category] = reserved_seat_count_by_category.get(price_category, 0) + 1 # https://stackoverflow.com/a/12992212

# print(reserved_seat_count_by_category)
inverse_reserved_seat_count_by_category = [(value, key) for key, value in reserved_seat_count_by_category.items()]  # https://stackoverflow.com/q/268272

print(f"A legtöbb jegyet a(z) {max(inverse_reserved_seat_count_by_category)[1]}. árkategóriában értékesítették.")

# 5

actual_income = 0
for key in reserved_seat_count_by_category:

    if key == "1":
        actual_income = actual_income + reserved_seat_count_by_category[key] * 5000
    elif key == "2":
        actual_income = actual_income + reserved_seat_count_by_category[key] * 4000
    elif key == "3":
        actual_income = actual_income + reserved_seat_count_by_category[key] * 3000
    elif key == "4":
        actual_income = actual_income + reserved_seat_count_by_category[key] * 2000
    elif key == "5":
        actual_income = actual_income + reserved_seat_count_by_category[key] * 1500

print(f"A pillanatnyi adatok alapján a színház bevétele {actual_income} Ft lenne.")
