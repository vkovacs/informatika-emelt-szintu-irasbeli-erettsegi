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

for order in reversed(orders): # reversed is needed to show the _first_ day on which this order occurred
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

print(osszes("PL", 7))
