weight = float(input("Please enter weight in kilograms:"))
height = float(input("Please enter height in meters:"))
BMI = weight/(height*height)

if BMI>=30:
    print("Your BMI is", BMI, "and you are Obese")
elif BMI<29.9 and BMI>25:
    print("Your BMI is", BMI, "and you are Overweight")
elif BMI<24.9 and BMI>18.5:
    print("Your BMI is", BMI, "and you are Normal")
else:
    print("Your BMI is", BMI, "and you are Underweight")


