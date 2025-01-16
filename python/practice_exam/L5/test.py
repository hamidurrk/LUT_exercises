string = "hello1234"

def reverse(word):
    def recurse(word, r=''):
        if len(word) == 1:
            r += word[0]
            return r
        r += word[-1]
        return recurse(word[0:len(word)-1], r)
    return recurse(word)

def reverse_str(word):
    if len(word) <= 1:
        return word[0]
    result = word[0] + reverse_str(word[1:]) 
    return result


print(reverse_str(string))
