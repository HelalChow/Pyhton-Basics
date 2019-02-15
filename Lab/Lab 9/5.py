def get_common_element(lst1,lst2):
    lst = []
    for i in lst1:
        if lst2.count(i)>0:
            lst.append(i)
            lst2.pop(lst2.index(i))
    return lst

def main():
    lst1 = [ 2, 'S', 3.13, 3.13, 'python']
    lst2=[ 'pythy', 2, 12, 'hello', 3.13 ]
    print(get_common_element(lst1,lst2))

main()