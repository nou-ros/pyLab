products = ['c', 'o', 'p']
ord = ['p']

raw_quantity = [None] * len(products)
new_names = []

for p in products:
    if p in ord:
        new_names.append(p)
    else:
        new_names.append(0)

prod_list = [2]
print(new_names)

new_prod_quant = []

o = 0
for new in new_names:
    if new == 0:
        new_prod_quant.append(0)
    else:
        if new in ord[o]:
            new_prod_quant.append(prod_list[o])
            o+=1


print(new_prod_quant)