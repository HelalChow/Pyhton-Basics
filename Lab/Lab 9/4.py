def find_max_even_index(lst):
    max_num = -1
    for i in lst:
        if i%2==0 and i>max_num:
            max_num=i
    return lst.index(max_num)

def main():
    lst = [56, 24, 58, 10, 33, 95]
    print(find_max_even_index(lst))

main()