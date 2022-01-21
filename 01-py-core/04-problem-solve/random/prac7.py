products = ['c', 'o', 'p', 's']
ord = ['s','p']

raw_quantity = [None] * len(products)
new_names = []

for p in products:
    if p in ord:
        new_names.append(p)
    else:
        new_names.append(0)

prod_list = [7,4]
print(new_names)

new_prod_quant = []

for new in new_names:
    if new == 0:
        new_prod_quant.append(0)
    else:
        for idx, val in enumerate(ord):
            if new in val:
                new_prod_quant.append(prod_list[idx])


print(new_prod_quant)
