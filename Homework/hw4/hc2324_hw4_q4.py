rows = int(input("Please enter the number of rows: "))
count = rows
num = "1"
for i in range(1, rows+1):
    print((count-1)*" " + num)
    num = num+str(i+1)
    count -=1
