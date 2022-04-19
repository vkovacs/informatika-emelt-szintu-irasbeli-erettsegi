# 1
base_path = "../resources/Forrasok/4_Nezoter"  # Relative paths are relative to current working directory


def read_file(path):
    result = list()
    for line in open(path).readlines():
        result.append(list(line.strip()))

    return result


reservations = read_file(base_path + "/foglaltsag.txt")
price_categories = read_file(base_path + "/kategoria.txt")

# 2

line = int(input("Sor: "))
col = int(input("Sorszám: "))

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

inverse_reserved_seat_count_by_category = [(value, key) for key, value in reserved_seat_count_by_category.items()]  # https://stackoverflow.com/q/268272

print(f"A legtöbb jegyet a(z) {max(inverse_reserved_seat_count_by_category)[1]}. árkategóriában értékesítették.")

# 5

actual_income = 0
for key in reserved_seat_count_by_category:

    if key == "1":
        actual_income += reserved_seat_count_by_category[key] * 5000
    elif key == "2":
        actual_income += reserved_seat_count_by_category[key] * 4000
    elif key == "3":
        actual_income += reserved_seat_count_by_category[key] * 3000
    elif key == "4":
        actual_income += reserved_seat_count_by_category[key] * 2000
    elif key == "5":
        actual_income += reserved_seat_count_by_category[key] * 1500

print(f"A pillanatnyi adatok alapján a színház bevétele {actual_income} Ft lenne.")

# 6

# https://blog.finxter.com/python-regex-how-to-count-the-number-of-matches/#:~:text=To%20count%20a%20regex%20pattern,length%20of%20it%20as%20well.

lonely_seat_count = 0
for reservation_line in reservations:
    reservation_line_string = "".join(reservation_line)

    lonely_seat_count_in_this_row = reservation_line_string.count("xox")

    if reservation_line_string[0:2] == "ox":
        lonely_seat_count_in_this_row += 1

    if reservation_line_string[-2:] == "xo":
        lonely_seat_count_in_this_row += 1

    lonely_seat_count += lonely_seat_count_in_this_row

print(f"{lonely_seat_count} egyedülálló szék van a nézőtéren")

# 7
customer_reservation_view = list()

for i in range(len(reservations)):
    merged_reservation_line = ""
    for j in range(len(reservations[i])):
        if reservations[i][j] == "x":
            merged_reservation_line += "x"
        else:
            price_category = price_categories[i][j]
            merged_reservation_line += price_category

    customer_reservation_view.append(merged_reservation_line)

customer_reservation_view_file = open("szabad.txt", "w")
for reservation_line in customer_reservation_view:
    customer_reservation_view_file.write("".join(reservation_line)+"\n")

customer_reservation_view_file.close()
