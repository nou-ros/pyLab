# problem solve 2
import datetime

date_list = ['2021-07-08', '2021-07-08', '2021-07-10', '2021-07-11', '2021-07-11', '2021-07-11']
inv_product_quantity = [1.0, 1.0, 2.0, 1.0, 1.0, 1.0]
inv_product_name = ['asus', 'moto', 'asus', 'asus', 'canon', 'asus']

from_date = '2021-07-08'
to_date = '2021-07-11'

from_to_date_list = []

inv_product_date_list = []


def date_range(first_date, last_date, date_list):
    step = datetime.timedelta(days=1)
    start_date = datetime.datetime.strptime(first_date, "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime(last_date, "%Y-%m-%d").date()
    while start_date <= end_date:
        date_list.append(start_date)
        start_date += step

date_range(from_date, to_date, from_to_date_list)

for i in range(0, len(date_list)):
    inv_product_date_list.append(datetime.datetime.strptime(date_list[i], "%Y-%m-%d").date())


# print(from_to_date_list)
# print(inv_product_date_list)
# print(inv_product_name)
# print(inv_product_quantity)


name_date_quan_dict = {}


for date in from_to_date_list:
    for index in range(len(inv_product_date_list)):
        if date == inv_product_date_list[index]:
            if tuple([date, inv_product_name[index]]) in name_date_quan_dict:
                first_quant = name_date_quan_dict[date, inv_product_name[index]] 
                second_quant = inv_product_quantity[index]
                total = first_quant + second_quant
                name_date_quan_dict[date, inv_product_name[index]] = total  
            else:
                name_date_quan_dict[date, inv_product_name[index]] = inv_product_quantity[index]



print(name_date_quan_dict.keys())

for keys in name_date_quan_dict:
    print(keys[0], keys[1])
    print(name_date_quan_dict)

