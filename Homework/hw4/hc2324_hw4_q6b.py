print("Please enter a non-empty sequence of positive integers, each one in a separate line. End your sequence by typing done: ")
count = 0
total = 1
done = False
while done==False:
    current = input()
    if current == "done":
        done=True
    else:
        total *= int(current)
        count+=1
mean = total**(1/count)
print("The geometric mean is:", mean)