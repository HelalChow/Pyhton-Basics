def main():
    ppm = open("turkey.ppm", "r")
    pgm = open("grey turkey", "w")

    header1 = ppm.readline()
    header2 = ppm.readline().strip()
    header3 = ppm.readline().strip()
    print("P2", file = pgm)
    print(header2, file = pgm)
    print(header3, file = pgm)

    for line in ppm:
        rgb_lst = create_int_list(line)
        grey_list = create_grey_num(rgb_lst)
        new_line = create_line_num(grey_list)
        print(new_line, file=pgm)

    ppm.close()
    pgm.close()

def create_int_list(str):
    num_lst = str.split()
    for i in range(len(num_lst)):
        num_lst[i] = int(num_lst(i))
    return num_lst

def create_grey_num(lst):
    grey_lst = []
    for i in range(0,len(lst),3):
        average = (lst[i]+lst[i+1]+lst[i+2])//3
        grey_lst.append(average)
    return grey_lst

def create_line_num(lst):
    res_str = ''
    for item in lst:
        res_str = res_str + str(item) + " "
    return res_str.rstrip()

main()