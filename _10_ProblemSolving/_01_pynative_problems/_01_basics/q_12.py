'''
Calculate income tax for the given income by adhering to the below rules
Taxable  Income	   Rate (%)
First   $10,000	    0
Next    $10,000	    10
The     remaining	20

suppose that the taxable income is $45000 the income tax payable is

$10000*0% + $10000*10%  + $25000*20% = $6000.
'''
import time
start = time.time()

print("Enter taxable income: ")
amount=int(input())

def payable(amount):
    if amount>=20000:
        remain=amount-20000
        income_tax = 10000*0+10000*.1+remain*.2
        return f"Income tax for {amount} is: {income_tax}"
    elif amount<20000:
        remain=amount - 10000
        income_tax = remain*.1
        return f"Income tax for {amount} is: {income_tax}"

print(payable(12000))
end = time.time()
print('Time taken for program program: ', end - start)

