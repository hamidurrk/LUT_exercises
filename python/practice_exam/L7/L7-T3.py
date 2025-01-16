def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def main():
    source = input("Enter the name of the file to be read:\n")
    destination = "Palindromes.txt"
    source_file = open(source, 'r')
    destination_file = open(destination, 'w')

    while True:
        line = source_file.readline()

        if line == '':
            break
        
        word = line.strip()
        
        if is_palindrome(word):
            print(f"row '{word}' is a palindrome.")
            destination_file.write(line)
        else:
            print(f"row '{word}' is a not palindrome.")

    source_file.close()
    destination_file.close()
    
main()
