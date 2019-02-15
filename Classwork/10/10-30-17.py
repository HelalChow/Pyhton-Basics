def main():
    text = input("Please enter a sentence: ")
    new = prepare(text)
    pal =  check(new)
    if pal == True:
        print("it is palindrome")
    else:
        print("not palindrome")

def prepare(string):
    low = string.lower()
    new_low = only_low(low)
    return new_low

def only_low(string):
    str = ''
    for i in range(string):
        if i.islower()==True:
            str+=i
    return str

def check(string):
    rev = string[::-1]
    if rev==string:
        return True
    else:
        return False

main()