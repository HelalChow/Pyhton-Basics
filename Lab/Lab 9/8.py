def circular_shift_list1(lst,k):
    new_lst = []
    new_lst.extend(lst)
    for i in range(len(new_lst)-k):
        new_lst.append(lst[i])
        new_lst.pop(0)

    return lst[-k:] + lst[:-k]


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 3
    print(circular_shift_list1(lst,k))

main()