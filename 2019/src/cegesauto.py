from enum import Enum


class Direction(Enum):
    BE = 1
    KI = 0

    def __str__(self):
        return str(self.name).lower()


class CarLendingEntry:
    def __init__(self, day, timestamp, license_plate_number, employee_id, km_counter_position, direction):
        self.day = day
        self.timestamp = timestamp
        self.license_plate_number = license_plate_number
        self.employee_id = employee_id
        self.km_counter_position = km_counter_position
        if direction == "1":
            self.direction = Direction.BE
        else:
            self.direction = Direction.KI

    def __str__(self):
        return self.day + " " + self.timestamp + " " + self.license_plate_number + " " + \
               self.employee_id + " " + self.km_counter_position + " " + str(self.direction)


# 1
file = open("../resources/Forrasok/4_Ceges_autok/autok.txt")

car_lending_entries = []
for entry in file:
    car_lending_entries.append(
        CarLendingEntry(entry.split()[0], entry.split()[1], entry.split()[2], entry.split()[3], entry.split()[4],
                        entry.split()[5]))

file.close()
# 2

for entry in reversed(car_lending_entries):
    if entry.direction == Direction.KI:
        print("2. feladat")
        print(f"{entry.day}.nap rendszám: {entry.license_plate_number}")
        break

# 3
examined_day = input("Nap: ")
print(f"Forgalom a(z) {examined_day} napot: ")

for entry in car_lending_entries:
    if entry.day == examined_day:
        print(f"{entry.timestamp} {entry.license_plate_number} {entry.employee_id}, {entry.direction}")

# 4
exited_cars = set()
not_exited_cars = set()
for entry in reversed(car_lending_entries):
    if entry.direction == Direction.BE and entry.license_plate_number not in exited_cars:
        not_exited_cars.add(entry.license_plate_number)
    else:
        exited_cars.add(entry.license_plate_number)

print(f"A hónap végén {len(not_exited_cars)} autót nem hoztak vissza!")

# 5
entries_grouped_by_car = {}  # key will be a string and the value will be a list of strings

for entry in car_lending_entries:
    actual_license_plate_number = entry.license_plate_number

    if actual_license_plate_number in entries_grouped_by_car:
        entries_grouped_by_car[actual_license_plate_number].append(entry)
    else:
        entries_grouped_by_car[actual_license_plate_number] = [entry]

car_distanced_travel = {}

max_distance_travelled_by_any_car = -1  # 6
employee_id_who_driven_the_max_distance = -1  # 6

for license_plate_number in entries_grouped_by_car:
    sum_distance = 0
    entries_for_car = entries_grouped_by_car[license_plate_number]

    for i in range(1, len(entries_for_car), 2):
        distance = int(entries_for_car[i].km_counter_position) - int(entries_for_car[i - 1].km_counter_position)
        sum_distance += distance
        # 6
        if distance > max_distance_travelled_by_any_car:  # 6
            max_distance_travelled_by_any_car = distance  # 6
            employee_id_who_driven_the_max_distance = entries_for_car[i].employee_id  # 6

    car_distanced_travel[license_plate_number] = sum_distance

print("5. feladat")
for license_plate_number in sorted(car_distanced_travel):
    print(f"{license_plate_number} {car_distanced_travel[license_plate_number]} km")

# 6
print(f"A leghosszabb út: {max_distance_travelled_by_any_car} km, személy: {employee_id_who_driven_the_max_distance}")

# 7
actual_license_plate_number = input("Rendszám: ")
file_out = open(actual_license_plate_number + "_menetlevel.txt", "w")

entries_for_car = entries_grouped_by_car[actual_license_plate_number]


def to_string(day, timestamp, km_counter_position):
    return f"{day}.    {timestamp}    {km_counter_position} km"


for i in range(1, len(entries_for_car), 2):
    car_exits_the_site_string = f"{entries_for_car[i - 1].employee_id}    " + to_string(entries_for_car[i - 1].day, entries_for_car[i - 1].timestamp, entries_for_car[i - 1].km_counter_position)
    car_arrives_back_to_site_string = to_string(entries_for_car[i].day, entries_for_car[i].timestamp, entries_for_car[i].km_counter_position)

    file_out.write(f"{car_exits_the_site_string}     {car_arrives_back_to_site_string}\n")

# if there is a car which is not returned to the site but exited it, it also needs to be added to the file
if len(entries_for_car) % 2 == 1:  # even number of entries means a car is exited and never returned
    last_index = len(entries_for_car) - 1
    car_exits_the_site_string = f"{entries_for_car[last_index].employee_id}    " + to_string(entries_for_car[last_index].day, entries_for_car[last_index].timestamp, entries_for_car[last_index].km_counter_position)
    file_out.write(car_exits_the_site_string)
file_out.close()

print("Menetlevél kész.")
