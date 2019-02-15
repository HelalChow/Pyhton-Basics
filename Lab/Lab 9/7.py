def remove_below_avg(lst):
    sum = 0
    for i in lst:
        sum += i
    average = sum / len(lst)
    print(average)
    count = len(lst)-1
    while count>=0:
        if lst[count]<average:
            lst.pop(count)
        count =count - 1
    return lst

def main():
    lst = [2, 3, 5, 1, -4, 8, 0, -1]
    print(lst)
    print(remove_below_avg(lst))
main()