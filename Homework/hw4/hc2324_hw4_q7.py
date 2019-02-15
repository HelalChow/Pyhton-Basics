import random

print("I thought of a number between 1 and 100! Try to guess it.\n ")
low = 1
high =100
chances= 5
count = 0
guess = False
ans = random.randint(1, 101)
#print(ans)
while guess is False:
    print("Range: [" + str(low) + "," + str(high) + "], Number of guesses left:", chances)
    choice = int(input("your guess: "))
    if choice == ans:
        count += 1
        print("Congrats! You guessed my number in", count, "guesses")
        guess = True
    elif chances == 1:
        print("Out of guesses! My number is", ans)
        guess = True
    elif choice>ans:
        high = choice-1
        chances -=1
        count += 1
        print("Wrong! My number is smaller.\n")
    else:
        low = choice+1
        chances -=1
        count += 1
        print("Wrong! My number is higher.\n")

