def sum_squares(lst):
    sum=0
    for i in lst:
        sum+=i**2
    return sum
def main():
    lst = [1,2,3,4,5]
    print(sum_squares(lst))
main()