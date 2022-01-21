def to_celcius(val):
    far = float(val)
    cel = (far-32)*5/9
    return cel


def to_fahrenheit(val):
    cel = float(val)
    far = (9*cel)/5 + 32
    return far


print(to_celcius(78))
print(to_fahrenheit(25.55))
