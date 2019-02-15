decimal= int(input("Enter decimal number: "))
deci = decimal
M=0
D=0
C=0
L=0
X=0
V=0
I=0
while (deci//1000>0):
    M += deci//1000
    deci -= M*1000

D += deci//500
deci -= D*500

for c in range(4):
    while deci > 100:
        C += deci // 100
        deci -= C * 100

L += deci//50
deci -= L*50

for x in range(4):
    while deci > 10:
        X += deci // 10
        deci -= X * 10


V += deci//5
deci -= V*5

for i in range(4):
    while deci > 1:
        I += deci // 1
        deci -= I * 1

print("M"*M + "D"*D + "C"*C + "L"*L + "X"*X + "V"*V + "I"*I)
