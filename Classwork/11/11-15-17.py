'''f = open("test file.txt", "r")
f.readline()
f. readlines()
for line in f:

f = open("test file2.txt", "w")
print("abc", file = f)

f.close()'''

#Print with line number
'''def main():
    in_file = open("Thunder.txt", "r")
    out_file = open("Thunder with line numbers.txt", "w")
    
    count = 1
    for line in in_file:
        print(count,". ", line, sep ='', end = '', file = out_file)
        count+=1
        
    in_file.close()
    out_file.close()
    print()
main()'''

#print with line number and number of words
'''def main():
    in_file = open("Thunder.txt", "r")
    out_file = open("Thunder-word count.txt", "w")

    count = 1
    for line in in_file:
        list_words = line.split()
        num_words = len(list_words)
        print("line ",count, ": ", num_words, " words", sep='', end='', file=out_file)
        count += 1

    in_file.close()
    out_file.close()

main()'''

s = "abc def ghi"
s.split()
print(s)

t = "abc*def*ghi"
t.split("*")
print(t)