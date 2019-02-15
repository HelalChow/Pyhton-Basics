def main():
    words_dist_dict = calc_words_distribution("Old McDonals.txt")
    print_word_distribution(words_dist_dict)


def calc_words_distribution(filename):
    file = open(filename, "r")
    dict = {}
    for line in file:
        words_lst = line.split()
        for word in words_lst:
            word = clean_word(word)
            if word in dict:
                dict[word] += 1
            else:
                dict[word] =1
    return dict
def clean_word(word):
    word = word.lower()
    word = word.strip(".,!?")
    return word


def print_word_distribution(dict):
    dict_lst= []
    for word in dict:
        tuple = (dict[word], word)
        dict_lst.append(tuple)
    dict_lst.sort()
    for item in dict_lst:
        print(item[1], item[0])

