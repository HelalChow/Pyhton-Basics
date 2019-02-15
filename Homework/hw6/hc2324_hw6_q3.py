def first_word(string):
    space = string.find(" ")
    return string[0:space]

def remove_first_word(string):
    space = string.find(" ")
    str = string[space+1:]
    return str

def reverse_words(string):
    str = string
    new_str = ''
    while str.find(" ") != -1:
        new_str = first_word(str) + " "  + new_str
        str = remove_first_word(str)
    new_str = str + " " + new_str
    return new_str

def main():
    string = input("Please enter a text to reverse:\n")
    print(reverse_words(string))

main()