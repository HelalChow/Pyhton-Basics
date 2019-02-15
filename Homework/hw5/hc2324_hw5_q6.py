letters = input("Please enter a string of lowercase letters: ")
count = 0
i = 0
while (i<len(letters)-1):
    if letters[i]>letters[i+1]:
        count +=1
    i+=1
if count==0:
    print(letters, "is increasing.")
else:
    print(letters, "is not increasing.")

