import math as m

print("Please enter lengths of a triangle's side")
side1= float(input("length of the first side: "))
side2= float(input("length of the second side: "))
side3= float(input("length of the third side: "))

if side1>side2 and side1>3:
    t= side1
    side1=side3
    side3=t
elif side2>side1 and side2>side3:
    t=side2
    side2=side3
    side3=t
if side1==side2==side3:
    print(str(side1)+", "+str(side2)+",", side3, "form an equilateral triangle")
elif side1==side2:
    if (m.sqrt(side1**2 + side2**2)) == side3:
        print(str(side1) + ", " + str(side2) + ",", side3, "form a right isosceles triangle")
    else:
        print(str(side1) + ", " + str(side2) + ",", side3, "form an isosceles triangle that is not a right triangle")
else:
    print(str(side1) + ", " + str(side2) + ",", side3, " does not form an equilateral or isosceles triangle")
