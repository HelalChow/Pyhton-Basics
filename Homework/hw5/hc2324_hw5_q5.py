pas= input("Enter a password: ")
upper = 0
lower = 0
dig = 0
special = 0
for i in pas:
    if ("a"<=i and "z">=i):
        lower+=1
    elif ("A"<=i and "Z">=i):
        upper +=1
    elif ("1"<=i and "9">=i):
        dig += 1
    elif (i=="!" or i=="@" or i=="#" or i=="$"):
        special+=1
if (upper>=2 and lower>=1 and dig>=2 and special>=1 and len(pas)>7):
    print(pas, "is a valid password.")
else:
    print(pas, "is not a valid password.")
