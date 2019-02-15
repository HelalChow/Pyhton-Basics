'''def merge(lst1, lst2):
    new_lst = []
    min1 = 0
    min2 = 0
    while(min1 < len(lst1) and min2 < len(lst2)):
        if lst1[min1]<lst2[min2]:
            new_lst.append(lst1[min1])
            min1 += 1
        else:
            new_lst.append(lst2[min2])
            min2 += 1
    if min1 < len(lst1):
        new_lst.extend(lst1[min1:])
    else:
        new_lst.extend(lst2[min2:])
    return new_lst

def main():
    lst1 = [1, 3, 4, 4, 7, 8, 10]
    lst2 = [2, 5, 6, 7]
    print(merge(lst1, lst2))
main()
'''


'''def selection_sort(lst):
    for curr in range(len(lst)-1):
        min_val = min(lst[curr:])
        min_index = lst.index(min_val, curr)
        temp = lst[curr]
        lst[curr] = lst[min_index]
        lst[min_index] = temp
def main():
    lst = [3, 1, 7, 5, 9, 2, Lab 12]
    selection_sort(lst)
    print(lst)
main()
'''

def example(lst, word):
    for i in range(len(lst)-1, 0, -1):
        if word<lst[i]:
            lst.insert(i, word)

def main():
    lst = ["apple", "boy", "hello", "love", "mean"]
    word = "can"
    example(lst, word)
    print(lst)


main()
























