char = input("Enter a character: ")
if ("a"<=char and char<="z"):
    print(char, "is a lower case letter.")
elif (char>="0" and char<="9"):
    print(char, "is a digit.")
elif ("A"<=char and char<="Z"):
    print(char, "is an upper case letter.")
else:
    print(char, "is a non-alphanumeric character.")