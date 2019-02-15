import random as r

n = int(input("Enter a number n: "))
for i in range(n):
    num = ""
    while len(num)<(n-i):
        num+=str(r.randint(0, 9))
    print(num)
for i in range(1,n+1):
    num = ""
    for j in range(1,i+1):
        num+=str(r.randint(0, 9))
    print(num)


'''def shout(sentence):
    sentence = sentence.upper()
    return sentence

def main():
    sen = input("Enter a sentence to shout: ")
    print(shout(sen)+"!!!")
main()'''

'''def convertAsciiToText(num):
    revword =''
    NUM = num
    while NUM>0:
        current = NUM%100
        revword += chr(current)
        NUM=NUM//100
    word = revword[::-1]
    return word

def main():
    number = int(input("enter a number: "))
    #number = 808984727978
    print(convertAsciiToText(number))
main()'''






