# sum of squares of first n natural number

# this will overflow for large number
def squareSum(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

print("Sum of squares of first 4 natural number: ", squareSum(4))
