'''
Generate a Python list of all the even numbers between 4 to 30
'''

# first way
def generate():
    new = []
    for i in range(4, 30):
        if i%2==0:
            new.append(i)
    return new

print(generate())

# second way
print(list( range(4, 30, 2)))