# problem solve 1
from datetime import datetime
date_list = ['2021-07-08', '2021-07-08', '2021-07-10', '2021-07-11', '2021-07-11', '2021-07-11']
inv_value = [1, 1, 2, 1, 1, 1]
prod_name = ['asus', 'moto', 'asus', 'asus', 'canon', 'asus']

prod_name_set = set(prod_name)

new_list = []

for i in range(0, len(date_list)):
    new_list.append(datetime.strptime(date_list[i], "%Y-%m-%d").date())

my_dict = {}
for key in range(0, len(new_list)):
    for value in inv_value:
        if len(my_dict) == 0:
            my_dict[new_list[key]] = value
            break
        else:
            index = key
            if new_list[key] in my_dict.keys():
                first_value = my_dict.get(new_list[key])
                second_value = inv_value[index]
                total = first_value + second_value
                my_dict[new_list[key]] = total
            else:
                my_dict[new_list[key]] = inv_value[index]
            break
        
print(my_dict)



# checking 

# value = '2021-07-05' 

# if datetime.strptime(value, "%Y-%m-%d").date() in my_dict:
#     print(my_dict.get(datetime.strptime(value, "%Y-%m-%d").date()))
# else:
#     print('Nai')

# if len(new_list) == 0:
#     new_list.append(datetime_object)

# else: 
#     if datetime_object not in new_list:
#         n = 1
#         new_list.append(datetime_object)
#         inv_value.append(n)
#     else: 
#         pass
   

# print(inv_value)