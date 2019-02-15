length= int(input("Please enter the length of the sequence: "))
print("Please enter your sequence: ")
total = 1
for i in range(length):
    current = int(input())
    total *= current
mean = total**(1/length)
print("The geometric mean is:", mean)