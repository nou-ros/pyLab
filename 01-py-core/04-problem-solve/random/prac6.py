# problem solve 6

sum_quantity = [[1, 2], [3, 4], [5, 6]]

sum_quantity_col = len(sum_quantity)
sum_quantity_row = len(sum_quantity[0])
total_quantity_list = []
add_quantity_col = 0

for m in range(sum_quantity_row):
    for n in range(sum_quantity_col):
        add_quantity_col += sum_quantity[n][m]

    total_quantity_list.append(add_quantity_col)
    add_quantity_col = 0

print(total_quantity_list)
