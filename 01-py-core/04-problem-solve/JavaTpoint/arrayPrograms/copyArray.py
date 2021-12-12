arr1 = [1,2,3,4,5]
arr2 = [None]*len(arr1)

for i in range(0,len(arr1)):
    arr2[i]=arr1[i];

for i in arr2:
    print(i)
