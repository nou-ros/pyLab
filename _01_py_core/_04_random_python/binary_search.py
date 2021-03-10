items = [10,20,30,40,50,60,70,80]

def binary(itmes, n):
    low=0
    high = len(items)-1
    while low<=high:
        mid = (low+high)//2
        guess = items[mid]
        if guess == n:
            return mid+1
        elif guess < n:
            low = mid+1
        else:
            high = mid-1

    return -1

res = binary(items, 20)
print(res)


# list must be sorted
# time complexity: O(logn)

