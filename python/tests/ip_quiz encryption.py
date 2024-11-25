import string

def generate_srting_dict():
    string_dict = {}
    string_dict["0"] = 0
    string_dict["!"] = 30
    for i, letter in enumerate(string.ascii_lowercase):
        string_dict[letter] = i+1
    return string_dict

def decimal_to_binary(decimal_number):
    binary_number = ""
    if decimal_number == 0:
        return "00000"
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
    if len(binary_number) % 5 != 0:
        binary_number = "0" * (5 - len(binary_number) % 5) + binary_number
    return binary_number

def binary_to_decimal(binary_number):
    decimal_number = 0
    binary_number = str(binary_number)
    for digit in binary_number:
        decimal_number = decimal_number * 2 + int(digit)
    return decimal_number

def perform_xor(binary_number, key):
    result = ""
    for i in range(len(binary_number)):
        if binary_number[i] == key[i]:
            result += "0"
        else:
            result += "1"
    return result

def encrypt(letter=None, key=None, letter_binary=None):
    string_dict = generate_srting_dict()
    if letter != None:
        print("Letter:", letter)
        letter_index = string_dict[letter]
        letter_binary = decimal_to_binary(letter_index)
    print("Letter binary:", letter_binary)
    
    encrypted_binary = perform_xor(letter_binary, key)
    print("Encrypted binary:", encrypted_binary)
    
    encrypted_index = binary_to_decimal(encrypted_binary)
    print("Encrypted letter index:", encrypted_index)
    
    print("Encrypted letter: ", end="")
    for k, v in string_dict.items():
        if v == encrypted_index:
            print(k)
            return k
    print("")
    return encrypted_index

def encrypt_sentence(sentence, key):
    encrypted_sentence = ""
    for letter in sentence:
        if letter != " ":
            encrypted_sentence += str(encrypt(letter=letter, key=key))
        else:
            encrypted_sentence += str(encrypt(letter_binary="11111", key=key))
            
    print("Encrypted sentence:", encrypted_sentence)

encrypt_sentence("hello world!", "10101")
# encrypt(letter_binary="11111", key="10101")