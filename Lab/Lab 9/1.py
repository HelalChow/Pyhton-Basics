def consecutive_int(myint, n):
    lst = []
    for i in range(myint, myint+n):
        lst.append(i)
    return lst

def main():
    print(consecutive_int(10,5))
main()
