def find_longest(filename):
    file = open(filename, 'r')
    word_list = file.readlines()
    count = []
    for word in word_list:
        word = word.strip()
        count.append(len(word))    
    return max(count)

print(find_longest("./python/tests/words.txt"))