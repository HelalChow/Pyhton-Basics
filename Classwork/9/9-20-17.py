import turtle
import math

leg1 = float(input("Please enter the length of leg1:"))
leg2 = float(input("Please enter the length of leg2:"))
hyp = float(leg1**2 + leg2**2)**0.5
angle1 = math.degrees(math.atan(leg1/leg2))
angle2 =  math.degrees(90- angle1)

turtle.forward(leg1)
turtle.left(90)
turtle.forward(leg2)
turtle.left(180 - angle1)
turtle.forward(hyp)
turtle.hideturtle()

turtle.done()

