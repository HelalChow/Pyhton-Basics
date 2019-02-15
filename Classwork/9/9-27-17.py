import math as m
import turtle as t

grade = int(input())
grade1 = int(input())

if (grade < 60) or (grade1 < 60):
    print("fail")
elif (grade>=95) and (grade1 >= 95):
    print("Honors")
else:
    print("graduated")




