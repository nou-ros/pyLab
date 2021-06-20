nums = [1,2,3,4,5,6,7,8,9,10]

# list comprehension
f_list = [n for n in nums]
# print(f_list)
s_list = [n*n for n in nums]
# print(s_list)
t_list = [n for n in nums if n%2==0]
# print(t_list)

# (letter, num) pair for each letter in 'abcd' and number in '0123'
fr_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(fr_list)

# Dictionary comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(dict(zip(names, heros))) - with zip and dict keyword

f_dict = {name:hero for name,hero in zip(names, heros)}
# print(f_dict)

s_dict = {name:hero for name,hero in zip(names, heros) if name!="Peter"}
# print(s_dict)

t_dict = {name:hero for name,hero in zip(names, heros) if hero=="Deadpool"}
# print(t_dict)

# Set comprehension
numb = [1,1,2,2,3,3,4,4,5,6,7,8,8,9]
f_set = {n for n in numb}
# print(f_set)

# Generator Expression
def gen_func(nums):
    for n in nums:
        yield n*n

norm_gen = gen_func(nums)
# print(next(my_gen))
# print(next(my_gen))
# for i in my_gen:
#     print(i)


ex_gen = (n*n for n in nums)
# print(next(ex_gen))
# print(next(ex_gen))
for i in ex_gen:
    print(i)