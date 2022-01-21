def compoundInterest(prinAmount, rate, time):
    amount = prinAmount * pow((1 + rate / 100), time)
    compInterest = amount - prinAmount
    print("Compound interest is : ", compInterest)

compoundInterest(10000, 10.25, 5)
