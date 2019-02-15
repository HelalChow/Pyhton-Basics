n = int(input("Please enter a positive integer: "))
count = n
for i in range(1, n+1):
    print((i-1)*" " + (2*count-1)*"*" + (i-1)*" ")
    count = count-1
count1 = n
for i in range(1, n+1):
    print((count1-1)*" " + (2*i-1)*"*" + (count1-1)*" ")
    count1 = count1-1
