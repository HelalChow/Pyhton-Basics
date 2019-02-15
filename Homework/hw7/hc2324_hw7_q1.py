def max_abs_val(lst):
    for i in lst:
        if i<0:
            lst[lst.index(i)] = (-1)*i
    return max(lst)
def main():
    lst = [-19, -3, 20, -1, 0, -25]
    print(max_abs_val(lst))
main()
