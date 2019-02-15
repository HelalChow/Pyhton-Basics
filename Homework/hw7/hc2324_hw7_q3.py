def add_list(lst1, lst2):
    new_lst = []
    for i in range(len(lst1)):
        new_lst.append(int(lst1[i])+int(lst2[i]))
    return new_lst

def create_list1():
    lst1 = []
    seen_done1 = False
    print("Enter one number per line for list 1. Enter 'done' when finished with list 1:")
    while seen_done1 == False:
        inp = (input())
        lst1.append(inp)
        if inp == "done":
            seen_done1 = True
            lst1.pop()
    return lst1

def create_list2():
    lst2 = []
    seen_done2 = False
    print("Enter one number per line for list 2. Enter 'done' when finished with list 2:")
    while seen_done2 == False:
        inp = (input())
        lst2.append(inp)
        if inp == "done":
            seen_done2 = True
            lst2.pop()
    return lst2

def check_length(lst1, lst2):
    if len(lst1)==len(lst2):
        return True
    else:
        return False

def main():
    lst1= create_list1()
    lst2= create_list2()
    if check_length(lst1, lst2):
        print(add_list(lst1, lst2))
    else:
        print("Lists are different lengths")

main()


