str = input("Enter sequences of 1s and 0s: ")

count=1
for i in range(len(str)-1):
    if str[i]==str[i+1]:
        count+=1
    else:
        print(count,str[i]+"'s")
        count=1

print(count, str[i+1] + "'s")