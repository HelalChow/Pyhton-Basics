def create_prefix_lists(lst):
    prefix_lists=[[]]
    for i in range(1, len(lst)+1):
        part_list = []
        for j in range(i):
            part_list.append(lst[j])
        prefix_lists.append(part_list)
    return prefix_lists

def main():
    lst = [2,4,6,8,10]
    print(create_prefix_lists(lst))

main()
