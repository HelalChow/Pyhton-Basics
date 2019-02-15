def main():
    file_name = input("Please enter a filename: ")
    line_num_str = (input("Please enter the line number you want: "))

    try:
        line_num = int(line_num_str)
        in_file = open(file_name, "r")
        line = get_line_number(in_file, line_num)
        in_file.close()
        print(line)
    except ValueError:
        print(line_num, "must be an integer")
    except FileNotFoundError:
        print(file_name, "not found")
    except Exception:
        print(line_num, "is am invalid line number")
    return line


def get_line_number(file, line_num):
    lines_list = file.readlines()
    if(line_num > len(lines_list)) or (line_num < 0):
        raise Exception(str(line_num) + " is a inavild line number")

    return lines_list[line_num-1]

main()