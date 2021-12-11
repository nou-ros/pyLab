# semi-perimeter of a triangle = a+b+c/2
# area of a triangle = root_over(s*(s-a)*(s-b)*(s-c))

import math 

first_side = float(input("First side:"))
second_side = float(input("Second side: "))
third_side = float(input("Third side: "))

semi_perimeter = (first_side + second_side + third_side)/2

area = math.sqrt(semi_perimeter*(semi_perimeter-first_side)*(semi_perimeter-second_side)*(semi_perimeter-third_side))

print("Triange area: %0.2f"%area)
