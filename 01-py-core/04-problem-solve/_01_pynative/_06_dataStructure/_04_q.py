'''
Given a list iterate it and count the occurrence of each element and create a dictionary to show the count of each element
'''
original =  [11, 45, 8, 11, 23, 45, 23, 45, 89]
count = {}
for i in original:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1

print(count)