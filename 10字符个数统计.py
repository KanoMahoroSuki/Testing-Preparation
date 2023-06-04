string = input()
str_unique = ''
for char in string:
    if char not in str_unique:
        str_unique += char
print(len(str_unique))