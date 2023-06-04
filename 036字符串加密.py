string = input() + 'abcdefghijklmnopqrstuvwxyz'
key = ''
for char in string:
    if char not in key:
        key += char

text = input()
for char in text:
    print(key['abcdefghijklmnopqrstuvwxyz'.index(char)], end='')
