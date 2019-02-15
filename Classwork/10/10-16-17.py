num = int(input("enter  num:  "))
print("eneter each value in a different line")
min_sum = 0
min_num = 0
line = 0
for i in range(1, num+1):
    sum_dig = 0
    value = int(input())
    counter = value
    if (i == 1):
        min_num = value
        line = 1
        while (counter>0):
            rem = counter%10
            min_sum += rem
            counter //= 10
    else:
        while (counter>0):
            rem = counter%10
            sum_dig += rem
            counter //= 10
        if (min_sum>sum_dig):
            min_sum = sum_dig
            min_num = value
            line = i
print(min_num, "is the smallest sum-digits and it is in line", str(line)+".")


