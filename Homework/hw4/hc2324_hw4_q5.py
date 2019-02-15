n = int(input("Please enter a number: "))
for i in range(1, n+1):
    num = i
    odd=0
    even=0
    while (num > 0):
        dig = num%10
        if (dig%2!=0):
            odd+=1
        else:
            even+=1
        num = num//10
    if (even>odd):
        print(i)
