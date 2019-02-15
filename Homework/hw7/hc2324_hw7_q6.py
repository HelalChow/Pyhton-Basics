def main():
 lst1 = [1, 2, 3, 4, 5, 6]
 rev_lst1 = reverse_to_new_list(lst1)
 print("After reverse_to_new_list, lst1 is", lst1,
"and the returned list is", rev_lst1)

 lst2 = [1, 2, 3, 4, 5, 6]
 print("Before reverse_in_place, lst2 is", lst2)
 reverse_in_place(lst2)
 print("After reverse_in_place, lst2 is", lst2)

def reverse_to_new_list(lst):
    new_lst = []
    for i in range(len(lst), 0, -1):
        new_lst.append(i)
    return new_lst

def reverse_in_place(lst):
    lst.reverse()

main()