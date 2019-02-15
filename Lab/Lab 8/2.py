a = input("Enter first string: ")
b = input("Enter second string: ")

present = True
for i in a:
    check = b.find(i)
    if check == -1:
        present = False
    else:
        b = b[:check]+b[check+1:]
print(present)


