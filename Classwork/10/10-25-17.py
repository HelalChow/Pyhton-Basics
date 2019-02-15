import turtle as t

#Draw n squares
"""
def t_square(side_length, colour):
    for j in range(4):
        t.pencolor(colour)
        t.forward(side_length)
        t.left(90)
def fan_square(n):
    colour = ["blue", "red", "green", "yellow", "orange", "pink"]
    t.hideturtle()
    t.speed(1000)
    for i in range(n):
        t_square(100, colour[i % 6])
        t.left(360 / n)
def main():
    n = int(input("Please enter number of squares: "))
    fan_square(n)
    t.done()
main()"""

#F to C
def main():
    f = int(input("Please enter a temperature in Fahrenheit: "))
    print("Temp in Celecius is", conversion(f))
def conversion(f):
    c = (f-32)*(5/9)
    return c
main()