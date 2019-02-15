'''s = input("Please enter a string: ")
s2 = s
for i in s:
    if s.islower():
        s2.upper()
    else:
        s2.lower()
print("New string is:", s2)'''


'''a = input("Please enter string a: ")
b = input("Please enter string b: ")
short= ""
long = ""
if len(a)>len(b):
    long = a
    short = b
else:
    short = a
    long = b
print(short+long+short)'''


'''s = input("Please enter a string s: ")
s2 = ""
k = int(input("Please enter a number k: "))
start = 0
end = k
for i in s:
    s2 += s[start:end:-1]
    start += 2*k
    end = 2*k
    #s[::-1]
print(s2)'''


sen = input("Please enter a string: ")
sen2 = " "
while sen.find(" ") >=0:
    space = sen.find(" ")
    reverse = sen[space::-1]
    sen2 += reverse+" "
    sen = sen[space+1:]
sen = sen[::-1]
sen2+=sen
print(sen2)


'''S = input("Please enter a string s: ")
rep = 0
sub=""
for i in range(2,len(S)//2):
    for j in range(0, len(S)):
        count = S.count(S[j:j+i])
        if count>=rep:
            rep = count
            sub = S[j:j+i]
           # sub = sub[::-1]
print(rep)
print(sub)'''



    













