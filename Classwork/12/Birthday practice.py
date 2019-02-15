def add_name(dict, name, birthday):
    dict[name] = birthday

def print_names(dict):
    for names in dict:
        print(names)

def get_bday(dict, name):
    if name in dict:
        return(name, dict[name])

def main():
    dict = {}
    print("Welcome to bday dictionary")
    name = ''
    while name != 'done':
        name = input("Please input names of friends, or type done: ")
        if name != 'done':
            birthday = input("What is his or her bday:")
            if name not in dict:
                add_name(dict, name, birthday)
    print("We know the birthdays of: ")
    print_names(dict)
    in_name = input("Whose bday do you want to look up: ")
    bday = get_bday(dict, in_name)
    print(bday[0]+"'s birthday is "+bday[1])

main()





