# 1. feladat
orders_file = open("rendel.txt")

orders = []

for line in orders_file.readlines():
    split_line = line.strip().split(" ")
    order_item = (int(split_line[0]), split_line[1], int(split_line[2]))

    orders.append(order_item)

print(orders)

# 2. feladat

print(f"Az össes rendelés darabszáma: {len(orders)}")

# 3. feladat

day = 9  # FIXME: read from input

order_count_for_a_day = 0
for order in orders:
    if order[0] == day:
        order_count_for_a_day += 1

print(f"A rendelések száma az adott napon: {order_count_for_a_day}")

# 4. feladat

days_with_order_in_NR = set()
for order in orders:
    if order[1] == "NR":
        days_with_order_in_NR.add(order[0])

print(days_with_order_in_NR)

days_count_without_order_in_NR = len(set(range(1, 31)) - days_with_order_in_NR)

if days_count_without_order_in_NR > 0:
    print(f"{days_count_without_order_in_NR} nap nem volt a reklámban nem érintett városból rendelés")
else:
    print("Minden nap volt rendelés a reklámban nem érintett városból")

# 5. feladat

max_order_size = -1
max_order_day = -1

for order in reversed(orders):  # reversed is needed to show the _first_ day on which this order occurred
    order_size = order[2]
    if order_size > max_order_size:
        max_order_size = order_size
        max_order_day = order[0]

print(f"A legnagyobb darabszám: {max_order_size}, a rendelés napja: {max_order_day}")


# 6. feladat

def osszes(city, day):
    sum = 0
    for order in orders:
        if order[0] == day and order[1] == city:
            sum += order[2]
    return sum

# 7. feladat

day = 21
sumPL21 = osszes("PL", 21)
sumTV21 = osszes("TV", 21)
sumNR21 = osszes("NR", 21)

print(f"A rendelt termékek darabszáma a {day}. napon PL: {sumPL21} TV: {sumTV21} NR: {sumNR21}")


# 8. feladat

def osszesTobbNapra(city, days): # The previous solution could have been overwritten and use one element list for day input in exercise 6.
    sum = 0
    for order in orders:
        if order[0] in days and order[1] == city:
            sum += 1
    return sum


print("{:<6} {:<10} {:<10} {:<10}".format("Napok", "1..10", "11..20", "21..30")) # {:<6}, :<10, and :<10 specify the left alignment and the width of each column.
for city in ["PL", "TV", "NR"]:
    print("{:<6} {:<10} {:<10} {:<10}".format(city,
                                                    osszesTobbNapra(city, range(1, 11)),
                                                    osszesTobbNapra(city, range(11, 21)),
                                                    osszesTobbNapra(city, range(21, 31))))