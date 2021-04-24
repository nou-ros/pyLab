import random
passlen = int(input("Enter password length: "))
string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = "".join(random.sample(string, passlen))
print(password)
