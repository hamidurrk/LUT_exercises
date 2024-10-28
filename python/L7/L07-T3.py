# L07-T3: Testing data inside a file, palindromes
#
# Submitted by: Md Hamidur Rahman Khan
#

def test_palindrome(word: str) -> bool:
    word = word.lower()
    return True if word == word[::-1] else False

def main():
    source = input("Enter the name of the file to be read:\n")
    source_file = open(source, "r")
    pal_file = open("Palindromes.txt", "w", encoding="UTF-8")
    for line in source_file.readlines():
        if test_palindrome(line.strip()):
            pal_file.write(line)
            print(f"row '{line.strip()}' is a palindrome.")
        else:
            print(f"row '{line.strip()}' is not a palindrome.")
    pal_file.close()
    source_file.close()
    
if __name__ == "__main__":
    main()