'''
Use a loop to display elements from a given list which are present at even positions
'''
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
length = len(my_list)

for i in range(length):
    if i%2!=0:
        print(my_list[i], end=" ")