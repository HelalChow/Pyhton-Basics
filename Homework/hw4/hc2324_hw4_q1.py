num = int(input("Please enter a positive integer: "))
count = 0
while num>0:
    count += 2
    print(count)
    num -= 1

num1 = int(input("Please enter another positive integer: "))
for i in range(1, num1+1):
    print(i*2)
