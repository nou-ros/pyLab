# problem solve 3

# name = ['a', 'c', 'm']
# quantity = [['a', 2], ['m',1]]

# rantity = []

# for n in name: 
#     for i in quantity:
#         for _ in i:
#             if n == i[0]:
#                 rantity.append(i[1])
#                 break

# print(len(rantity))
# print(len(name))

# ren = len(rantity)
# nem = len(name)
# while ren < nem:
#     rantity.append(0)
#     ren += 1

# print(rantity)

prods = ['a', 'c', 'm', 'l', 't']
n = ['a', 'm', 'l']
q = [2, 1, 4]

sum = 0 
for i in q:
    sum+=i

print(sum)

i = 0
j = 0
nq = [None]*len(prods)
for p in prods:
    if j<len(n):
        if p in n[j]:
            nq[i] = q[j]
            j+=1
    i+=1
print(nq)
rq = []
for i in nq:
    if i is not None:
        rq.append(i)
    else:
        rq.append(0)

print()
