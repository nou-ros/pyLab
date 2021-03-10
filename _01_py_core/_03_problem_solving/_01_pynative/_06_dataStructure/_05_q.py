'''
Given a two list of equal size create a set such that it shows the element from both lists in the pair
'''
first =  [2, 3, 4, 5, 6, 7, 8]
second =  [4, 9, 16, 25, 36, 49, 64]

result = zip(first, second)
answ = set(result)

print(answ)

