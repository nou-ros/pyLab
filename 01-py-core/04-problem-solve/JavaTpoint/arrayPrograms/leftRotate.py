arr = [1,2,3,4,5]

n = 2

print("original array: ")
for i in arr:
    print(i)

for i in range(0,n):
    first = arr[0]
    for j in range(0, len(arr)-1):
        arr[j]=arr[j+1]
    arr[len(arr)-1] = first

print(arr)
