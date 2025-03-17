def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(message, key):
    encrypted_text = []
    key = generate_key(message, key)
    for i in range(len(message)):
        x = (ord(message[i]) + ord(key[i])) % 26
        x += ord('A')
        encrypted_text.append(chr(x))
    return "".join(encrypted_text)

def vigenere_decrypt(encrypted_message, key):
    decrypted_text = []
    key = generate_key(encrypted_message, key)
    for i in range(len(encrypted_message)):
        x = (ord(encrypted_message[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        decrypted_text.append(chr(x))
    return "".join(decrypted_text)

message = "password"
key = "completevictory"
encrypted_message = vigenere_encrypt(message, key)
print(f"Encrypted Message: {encrypted_message}")