'''
Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number
'''

for i in range(10):
    if i > 0:
        curr = i
        prev = i-1
        add = curr + prev
        print(f"current number {curr} and previous number {prev}. Sum: {add}")
    else:
        print(f"current number {i} and previous number 0. Sum: {i+i}")