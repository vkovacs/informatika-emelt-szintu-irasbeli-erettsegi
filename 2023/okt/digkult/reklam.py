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
for orders in orders:
    if orders[0] == day:
        order_count_for_a_day += 1

print(f"A rendelések száma az adott napon: {order_count_for_a_day}")