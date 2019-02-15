"""n = int(input("Please neter a number"))
sum = 0
for i in range(n):
    current = int(input())
    sum += current
average = sum/n"""

"""FIND AVERAGE"""
"""print("Please enter grades")
count = 0
sum1 = 0
done = False
while done==False:
    current = input()
    if current == "done":
        done=True
    else:
        sum1 += int(current)
        count+=1
print(sum1/count)"""

"""FIND SUPEREVEN NUMBER"""
"""NUM = int(input("Please enter a number: "))
num = NUM
seen_odd = False
while (num > 0):
    x = num%10
    if (x%2!=0):
        seen_odd = True
    num = num//10
if seen_odd == False:
    print("number is a super even number")
else:
    print("number is not super even")"""


"""FIND MIN VALUE"""
print("Please enter a set of numbers")
seen_done=False
first_iteration = True
min = 0
while(seen_done==False):
    current = input()
    if(current == "done"):
        seen_done = True
    else:
        if(first_iteration == True):
            min = int(current)
            first_iteration = False
        else:
            if (int(current)<min):
                min = int(current)
print(min)




