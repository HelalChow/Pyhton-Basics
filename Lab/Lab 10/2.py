import random as r
def write_random_numbers(filename, n):
    f = open(filename, "w")
    for i in range(n):
        print(r.randint(1,100), file = f)
    f.close()
write_random_numbers('lab11_q2.txt', 5)