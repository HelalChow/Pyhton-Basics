binary = input("Enter a binary number: ")
num = 0
for i in range(len(binary),0, -1):
    if binary[len(binary)-i-1]=='0':
        num += 2**(i)
print(num)