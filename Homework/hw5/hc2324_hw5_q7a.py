roman = input("Enter a number in the simplified Roman system: ")
num = 0
for i in roman:
    if i=="M":
        num+=1000
    elif i =="D":
        num+=500
    elif i == "C":
        num+=100
    elif i =="L":
        num+=50
    elif i=="X":
        num+=10
    elif i =="V":
        num+=5
    elif i =="I":
        num+=1
print(roman, "is", num)