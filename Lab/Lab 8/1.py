char = input("Please enter character: ")
n = int(input("Please enter an integer: "))

str=''
for i in range(ord(char),ord(char)+n):
    num = i
    if num>122:
        num=num-26
    str+=chr(num)
print(str)

