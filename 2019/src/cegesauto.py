from enum import Enum

# 1


class Direction(Enum):
    BE = 0
    KI = 1

    def __str__(self):
        return str(self.value)


class CarLendingEntry:

    def __init__(self, day, timestamp, license_plate_number, employee_id, km_counter_position, direction):
        self.day = day
        self.timestamp = timestamp
        self.license_plate_number = license_plate_number
        self.employee_id = employee_id
        self.km_counter_position = km_counter_position
        if direction == "be":
            self.direction = Direction.BE
        else:
            self.direction = Direction.KI

    def __str__(self):
        return self.day + " " + self.timestamp + " " + self.license_plate_number + " " + \
               self.employee_id + " " + self.km_counter_position + " " + str(self.direction)


file = open("../resources/Forrasok/4_Ceges_autok/autok.txt")

car_lending_entries = []
for entry in file:
    car_lending_entries.append(
        CarLendingEntry(entry.split()[0], entry.split()[1], entry.split()[2], entry.split()[3], entry.split()[4],
                        entry.split()[5]))
# 2

for entry in reversed(car_lending_entries):
    if entry.direction == Direction.KI:
        print("2. feladat")
        print(f"{entry.day}.nap rendszám: {entry.license_plate_number}")
        break
#3