text = input("Please input a line of text: ")
ch= input("Please enter a character you want to remove: ")
newText = ''
start = 0
while (text.find(ch, start) != -1):
    remove = text.find(ch, start)
    newText += text[start:remove]
    start = remove+1
newText+=text[start:]
print(newText)