def encode_string(str):
    encoded_string = []
    count = 1
    for i in range(len(str)-1):
        if str[i+1]==str[i]:
            count +=1
        else:
            lst = [str[i],count]
            encoded_string.append(lst)
            count =1
    lst = [str[len(str)-1], count]
    encoded_string.append(lst)
    return encoded_string

def decode_str(lst):
    str = ''
    for i in lst:
        str = str + i[0]*i[1]
    return str

def main():
    str = "aadccccaa"
    lst =[['a',2],['d',1],['c',4],['a',2]]
    print(encode_string(str))
    print(decode_str(lst))
main()