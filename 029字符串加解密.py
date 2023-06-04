def encrypt(x):
    ciphertext = ''
    for char in x:
        if char == 'z':
            ciphertext += 'A'
        elif char == 'Z':
            ciphertext += 'a'
        elif char == '9':
            ciphertext += '0'
        elif char.isupper():
            ciphertext += chr(ord(char.lower()) + 1)
        elif char.islower():
            ciphertext += chr(ord(char.upper()) + 1)
        elif char.isdigit():
            ciphertext += str(int(char) + 1)

    return ciphertext


def decrypt(x):
    plaintext = ''
    for char in x:
        if char == 'A':
            plaintext += 'z'
        elif char == 'a':
            plaintext += 'Z'
        elif char == '0':
            plaintext += '9'
        elif char.isupper():
            plaintext += chr(ord(char.lower()) - 1)
        elif char.islower():
            plaintext += chr(ord(char.upper()) - 1)
        elif char.isdigit():
            plaintext += str(int(char) - 1)

    return plaintext


print(encrypt(input()))
print(decrypt(input()))