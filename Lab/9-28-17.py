"""lang = input("Enter a language:")
if (lang == "en"):
    print("Hello, world!")
elif (lang == "es"):
    print("¡Hola mundo!")
else:
    print("Language not recognized")

num = int(input("Enter a number:"))
if (num%2 == 0):
    print("Even")
else:
    print("odd")

name= input("Enter your name:")
grad = int(input("Enter graduation year:"))
current = int(input("Enter current year:"))
diff = grad-current
if (diff == 4):
    print(name, "is a Freshman")
elif (diff == 3):
    print(name, "is a Junior")
elif (diff == 2):
    print(name, "is a Sophomore")
elif (diff == 1):
    print(name, "is a Senior")
else:
    print(name, "is not in college")

leg1 = float(input("Please enter the first leg:"))
leg2 = float(input("Please enter the second leg:"))
hyp = float(input("Please enter the hypotenuse:"))
if (leg1**2 + leg2**2 == hyp**2):
    print(str(leg1)+",", leg2, "and", hyp, "form a right triangle")
else:
    (str(leg1)+",", leg2, "and", hyp, "do not form a form a right triangle")

a = int(input("Please enter a:"))
b = int(input("Please enter b:"))
if (a == 0 and b!=0):
    print("The equation has no solution")
elif (a == 0 and b==0):
    print("The equation has infinitely many solutions")
else:
    x = ((-1) * b / a)
    print("The equation has a single solution and x =", x)

mon = int(input("Please enter an integer between 1 and 12: "))
if (mon <= 7 and mon!=2):
    if(mon%2 == 0):
        days = 30
    else:
        days = 31
else:
    if (mon % 2 == 0):
        days = 31
    else:
        days = 30
if (mon == 1):
    month = "January"
elif mon == 2:
    print("The entered month is February, and the number of days in February is 28")
elif (mon == 3):
    month = "March"
elif (mon == 4):
    month = "April"
elif (mon == 5):
    month = "May"
elif (mon == 6):
    month = "June"
elif (mon == 7):
    month = "July"
elif (mon == 8):
    month = "August"
elif (mon == 9):
    month = "September"
elif (mon == 10):
    month = "October"
elif (mon == 11):
    month = "November"
else:
    month = "December"
print("The entered month is", month, "and the number of days in", month, "is", days)


sides= int(input("Enter the number of sides: "))
if(sides == 3):
    print("The shape is a triangle")
elif (sides ==5):
    print("The shape is a pentagon")
else:
    equal= input("Are the sides equal?(Y/N): ")
    right= input("Are the angles 90 degrees?(Y/N): ")
    if(equal == "Y" and right=="Y"):
        print("The shape is a square")
    elif(equal =="N" and right=="Y"):
        print("The shape is a rectangle")
    else:
        print("The shape is a quadrilateral")
"""

s = int(input("Please enter time in 24 hr format: "))
hour24 = s//100
min = s%100

if (hour24<12):
    period="am"
    if(hour24 ==0):
        hour12=12;
    else:
        hour12=hour24
else:
    period = "pm"
    if(hour24==12):
        hour12=12
    else:
        hour12= hour24-12
print(str(hour24)+":"+str(min), "in Lab 12 hr format is:", str(hour12)+":"+str(min)+period)







