sen = input("Enter an odd length string: ")
middle_index = int(len(sen)/2)
middle = sen[middle_index]
first = sen[:middle_index]
second = sen[middle_index+1:]
print("Middle charachter:", middle)
print("First half:", first)
print("Seconf half:", second)
