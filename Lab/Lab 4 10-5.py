"""number = int(input("Please enter a positive integer: "))
dig = int(input("Please enter the number of digits: "))
sum=0
num = number
count = dig
while count>0:
    sum += num%10
    num = num//10
    count = count - 1
print("Sum of the last", dig, "digits in", number, "is:", sum)"""

"""positive= int(input("Please enter a positive integer: "))
total = 0
for i in range(1,positive+1):
    if (i%2==0):
        total -= i
    else:
        total += i
print("Sum is:", total)"""


"""a = int(input("Please enter a positive integer as the dividend: "))
b = int(input("Please enter a positive integer as the divisor: "))
count=0
sub = a
while (sub-b)>0:
    sub -= b
    count += 1
print(count)"""


"""a = int(input("Please enter a positive integer as the dividend: "))
b = int(input("Please enter a positive integer as the divisor: "))
num = a

while (num-b)>0:
    num -= b
print(num)"""

"""n = int(input("Please enter a positive integer: "))
for i in range(1, n+1):
    print(i**3)"""

"""n = int(input("Please enter a positive integer: "))
for i in range(1, n+1):
    if (i**3<n):
        print(i**3)"""

n = int(input("Please enter a positive integer: "))
sum = 0
for i in range(1, n+1):
    sum += i**3
print(sum)

"""num = int(input("Please enter an integer: "))
for i in range(1, num+1):
    print((i-1)*"x" + "o" + (num-i)*"x")"""










