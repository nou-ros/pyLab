height = float(input("Enter your height in feet: "))
weight = float(input("Enter your weight in kg: "))

# 1 foot = 30.48 cm
height = (height*30.48)/100
bmi = weight/(height*height)

print("Your BMI is: %.2f" % bmi)
print(f"Your body mass index is:  {bmi:.2f}")

if bmi > 0:
    if(bmi <= 16):
        print("You are severely underweight")
    elif(bmi <= 18.5):
        print("You are underweight")
    elif(bmi <= 25):
        print("you are healthy")
    elif(bmi <= 30):
        print("You are overweight")
    else:
        print("You are severely overweight")
else:
    print("Enter valid details")
