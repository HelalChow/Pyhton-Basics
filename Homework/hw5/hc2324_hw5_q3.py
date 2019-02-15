exp = input("Enter a mathematical expression: ")
space = exp.find(' ')
operand1 = int(exp[:space])
op = exp[space+1]
operand2 = int(exp[space+3:])
if op=="+":
    print(operand1, "+", operand2, "=", operand1+operand2)
elif op=="-":
    print(operand1, "-", operand2, "=", operand1-operand2)
elif op=="*":
    print(operand1, "*", operand2, "=", operand1*operand2)
else:
    print(operand1, "/", operand2, "=", operand1/operand2)





























"""curr = exp
loop = True
space = 0
start = 0
operand1=''
op=''
operand2=''
while (loop==True):
    space = exp.find(" ", space)
    if (space == -1):
        loop = False
        operand2 = exp[start:]
    if (start ==0):
        operand1 = exp[start:space]
        start = space+1
    else:
        op = exp[start:space]
        start = space+1
print(operand1, op, operand2)"""







