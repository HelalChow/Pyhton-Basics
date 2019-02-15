import turtle
import math

side1 = float(input("Please enter the length of the first side:"))
side2 = float(input("Please enter the length of the second side:"))
angle1 =(float(input("Please enter the angle between these two sides:")))

side3 = math.sqrt((side1**2 + side2**2)- 2*side1*side2*math.cos(math.radians(angle1)))
angle2 = math.degrees(math.acos((side2**2 + side3**2 - side1**2)/(2*side2*side3)))

turtle.forward(side1)
turtle.left((180 - angle1))
turtle.forward(side2)
turtle.left(180 - angle2)
turtle.forward(side3)
turtle.hideturtle()

turtle.done()