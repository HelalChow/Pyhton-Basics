def find_all(lst, val):
    new_lst=[]
    count = 0
    num = lst.count(val)
    for i in range(num):
        new_lst.append(lst.index(val)+count)
        lst.pop(lst.index(val))
        count+=1
    return new_lst
def main():
    lst = ['a', 'b', '10', 'bab', 'a']
    val = 'a'
    print(find_all(lst, val))
main()