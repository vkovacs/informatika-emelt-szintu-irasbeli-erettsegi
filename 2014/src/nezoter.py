#1
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

#line = int(input("Sor: "))
#col = int(input("Sorszám: "))

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

print(f"Az előadásra eddig {sum_reserved} jegyet adtak el, ez a nézőtér {round(sum_reserved / all_seats_count  * 100)} %-a.")