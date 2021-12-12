arr1 = [1,2,8,3,2,2,2,5,1]

arr2 = [None]*len(arr1)

visited = -1

for i in range(0, len(arr1)):
    count = 1
    for j in range(i+1, len(arr1)):
        if arr1[i] == arr1[j]:
            count+=1
            arr2[j]=visited


    if(arr2[i]!=visited):
        arr2[i]=count

for i in range(0, len(arr2)):
    if arr2[i] != visited:
        print(f'{arr1[i]} | {arr2[i]}')
