"""" first and last name
name =input("Please eneter your name: ")
space = name.find(" ")
first = name[:space+1]
last = name[space+1: ]
print("Firt name is",first)
print("Last name is", last)
print("Initials are:", name[0].upper()+last[0].upper())"""

line = input("Please enter a sentence: ")
count = 0
for i in line:
    if i == " ":
        count += 1
print(count)