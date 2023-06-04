string = input()
password = ''

for char in string:
    if char.islower():
        if char in 'abc':
            password += '2'
        elif char in 'def':
            password += '3'
        elif char in 'ghi':
            password += '4'
        elif char in 'jkl':
            password += '5'
        elif char in 'mno':
            password += '6'
        elif char in 'pqrs':
            password += '7'
        elif char in 'tuv':
            password += '8'
        elif char in 'wxyz':
            password += '9'
    elif char.isupper():
        if char == 'Z':
            password += 'a'
        else:
            password += chr(ord(char.lower()) + 1)
    else:
        password += char

print(password)
