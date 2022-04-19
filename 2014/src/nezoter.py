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