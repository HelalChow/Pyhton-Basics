#How many times word appears
"""sen = input("ener a sentence: ")
word = input("Please enetr a word: ")
count = 0
for i in range(len(sen)):
    for j in range(i, len(sen)):
        if sen[i:j] == word:
            count +=1
print(count)"""

#version 2
#sen = input("enter a sentence: ")
"""sen = "the cat in teh catalog is pink"
word = input("Please enetr a word: ")
count = 0
start = 0
loop = True
while(loop == True):
    space = sen.find(" ", start)
    if (sen.find(" ")==-1):
        loop = False
        curr = sen[start:]
    else:
        curr = sen[start:space]
        if curr == word:
            count+=1
        start = space+1
print(count)"""

#shifting letters in a word
word = input("Please enter a word: ")
shift = int(input("Please enter shift to apply: "))
new_word = ""

for i in word:
    ascii = ord(i)
    offset = ascii - ord("a")
    new_offset = (offset + shift)%26
    new_ascii = new_offset + ord("a")
    new_let = chr(new_ascii)

    new_word += new_let
print(new_word)



