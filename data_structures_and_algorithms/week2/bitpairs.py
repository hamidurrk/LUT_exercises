def pairs(s):
    count = 0
    sum_pos = 0
    total = 0
    for i, ch in enumerate(s):
        if ch == '1':
            total += count * i - sum_pos
            count += 1
            sum_pos += i
    return total


if __name__ == "__main__":
    print(pairs("100101"))       
    print(pairs("101"))          
    print(pairs("100100111001")) 
