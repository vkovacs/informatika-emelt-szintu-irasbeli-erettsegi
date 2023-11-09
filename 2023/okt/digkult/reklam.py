# 1. feladat
orders_file = open("rendel.txt")

orders = []

for line in orders_file.readlines():
    split_line = line.strip().split(" ")
    order_item = [int(split_line[0]), split_line[1], int(split_line[2])]

    orders.append(order_item)

print(orders)
