def add_entry(phonebook, name, phone_number):
    if name not in phonebook:
        try:
            if check_phone_number(phone_number):
                phonebook[name] = phone_number
        except Exception:
            print(phone_number+ "is not a valid number")



def check_phone_number(phone_number):
    if phone_number.isdigit() and len(phone_number)==10:
        return True
    else:
        raise Exception(phone_number+ " is not a valid number")

def lookup(phonebook, name):
    if name in phonebook:
        return phonebook[name]
    else:
        raise Exception(name+" not found in phonebook")

def print_all(phonebook):
    for name in phonebook:
        print(name, phonebook[name])

def main():
    phonebook = {}
    file = open("Lab 13 - phonebook.txt", "r")
    for line in file:
        line = line.split()
        first = line[0].strip(",")
        second = line[1]
        number = line[2]
        name = first + " " + second
        add_entry(phonebook, name ,number)
    print_all(phonebook)
    file.close()

main()
