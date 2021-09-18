from enum import Enum


class Direction(Enum):
    BE = 0
    KI = 1

    def __str__(self):
        return str(self.name).lower()


class CarLendingEntry:
    def __init__(self, day, timestamp, license_plate_number, employee_id, km_counter_position, direction):
        self.day = day
        self.timestamp = timestamp
        self.license_plate_number = license_plate_number
        self.employee_id = employee_id
        self.km_counter_position = km_counter_position
        if direction == "0":
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

    entries_for_car_count = len(entries_for_car)
    if entries_for_car_count % 2 == 1:
        entries_for_car_count -= 1

    last_km_counter_position = entries_for_car[0].km_counter_position
    for i in range(1, entries_for_car_count):
        if i % 2 == 1:
            distance = int(entries_for_car[i].km_counter_position) - int(last_km_counter_position)
            sum_distance += distance
            # 6
            if distance > max_distance_travelled_by_any_car:  # 6
                max_distance_travelled_by_any_car = distance  # 6
                employee_id_who_driven_the_max_distance = entries_for_car[i].employee_id  # 6
        else:
            last_km_counter_position = entries_for_car[i].km_counter_position

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

car_exit_the_site_string = f"{entries_for_car[0].employee_id}    {entries_for_car[0].day}.    {entries_for_car[0].timestamp}    {entries_for_car[0].km_counter_position}km"
for i in range(1, len(entries_for_car)):
    entry = entries_for_car[i]
    if i % 2 == 1:
        car_arrives_back_to_site_string = f"{entry.day}.    {entry.timestamp}   {entry.km_counter_position}km"
        file_out.write(f"{car_exit_the_site_string}     {car_arrives_back_to_site_string}\n")
        car_exit_the_site_string = ""
    else:
        car_exit_the_site_string = f"{entry.employee_id}    {entry.day}    {entry.timestamp}    {entry.km_counter_position}km"

if car_exit_the_site_string != "":
    file_out.write(car_exit_the_site_string)  # the car is not returned but the exit string needs to be written into the file
file_out.close()

print("Menetlevél kész.")
