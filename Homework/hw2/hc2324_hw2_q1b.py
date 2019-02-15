weight_pounds = float(input("Please enter weight in pounds:"))
height_inches = float(input("Please enter height in inches:"))
weight = weight_pounds * 0.453592
height = height_inches * 0.0254
BMI = weight/(height**2)

print("BMI is:", BMI)
