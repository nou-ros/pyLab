'''
Return the largest item from the given list
'''
# first way
def maximum(items=None):
    m=0
    for i in items:
        if m<i:
            m=i
    return m

aList = [4, 6, 8, 24, 12, 18]
print(maximum(aList))

# second way
aList = [4, 6, 8, 24, 12, 2]
print(max(aList))