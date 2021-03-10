"""
Given a list of numbers, return True if first and last number of a list is same
"""
numbers = [10,20,30,40,50]

def first_last_same(numbers=None):
    num_first = numbers[0]
    num_last = numbers[len(numbers)-1]
    if num_first == num_last:
        return True
    else:
        return False

print("Given list is : ", numbers)
print(first_last_same(numbers))