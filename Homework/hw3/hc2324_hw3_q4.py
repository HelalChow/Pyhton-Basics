import math as m

a = float(input("Please enter value of a: "))
b = float(input("Please enter value of b: "))
c = float(input("Please enter value of c: "))
if a==0 and b==0 and c==0:
    print("This equation has infinite number of solutions")
elif a==0 and b==0 and c!=0:
    print("This equation has no solution")
elif (b*b - 4*a*c)<0:
    print("This equation has no real solution")
elif (b*b - 4*a*c)==0:
    x = (((-1)*b)/(2*a))
    print("This equation has a single real solution x="+str(x))
elif a==0 and b!=0:
    x= ((-1)*c)/b
    print("This equation has a single real solution x=" + str(x))
else:
    x1= (((-1)*b + m.sqrt(b*b -4*a*c))/(2*a))
    x2= (((-1)*b - m.sqrt(b*b -4*a*c))/(2*a))
    print("This equation has two real solutions x=" + str(x1), "and x="+str(x2))
