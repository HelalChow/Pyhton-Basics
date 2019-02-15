import random as r
def create_permutation(n):
    lst = []
    for i in range(n):
        num = r.randint(0, n - 1)
        while lst.count(num)!=0:
            num = r.randint(0,n-1)
        lst.append(num)
    return lst

def scramble_word(word):
    new_word = ''
    perm = create_permutation(len(word))
    for i in perm:
        new_word+=word[i]+" "
    return new_word

def main():

    f = open("word bank.txt", "r")
    for i in range(r.randint(0,100)):
        f.readline()
    word = f.readline()

    print('Unscramble the word:', scramble_word(word))
    guess = False
    count = 1
    while count<=3 and guess==False:
        print("Try #",count,": ", sep = "", end = "")
        inword = input()
        inword = inword.strip()
        if inword == word:
            print("Yay you got it!")
            guess = True
        else:
            print("Wrong!")
            count+=1
    if count == 4:
        print("Out of tries. The correct word is:", word)
    f.close()
main()

