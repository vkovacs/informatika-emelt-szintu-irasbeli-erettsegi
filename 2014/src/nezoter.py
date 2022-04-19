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

line = int(input("Sor: "))
col = int(input("Sorszám: "))

seat_status = "üres" if reservations[line - 1][col - 1] == "o" else "foglalt"
print("A megadott szék " + seat_status)
