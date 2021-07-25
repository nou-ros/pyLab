# problem solve 4
n = ['a', 'f', 'l']

r = set()
for item in n:
    if item != 'f':
        r.add(item)

# print(r)

#
name = ['a', 'm', 'a', 'r', 'a', 'm', 'a', 'm', 'a', 'm']
quan = [1.0, 2.0, 1.0, 1.0, 1.0, 3.0, 3.0, 10.0, 2.0, 4.0]

name_quan_dict_total = {}

for ix in range(len(name)):
    if name[ix] not in name_quan_dict_total.keys():
        name_quan_dict_total[name[ix]] = quan[ix]
    else:
        name_quan_dict_total[name[ix]] += quan[ix]

print()

total_quant_values = []

for values in name_quan_dict_total.values():
    total_quant_values.append(values)

print(total_quant_values)

