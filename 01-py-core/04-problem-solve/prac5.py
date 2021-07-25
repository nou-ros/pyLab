# problem solve 5
names = ['r', 'm', 'a']
q = [3, 4, 2]
print(sorted(names))
sorted_names = sorted(names)

raw_quantity = [None] * len(names)

for sn in sorted_names:
    for ln in range(len(names)):
        if sn in names[ln]:
            print(q[ln])
            raw_quantity.append(q[ln])
