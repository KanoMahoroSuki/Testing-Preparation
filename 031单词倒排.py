string = input()
new_string = ''
for char in string:
    if char.isalpha():
        new_string += char
    else:
        new_string += ' '
new_string = new_string.split(' ')

print(' '.join(new_string[::-1]))