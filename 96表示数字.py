string = input()
new_string = ''

i = 0
while i < len(string):
    if string[i].isdigit():
        number = ''
        while i < len(string) and string[i].isdigit():
            number += string[i]
            i += 1
        new_string += "*" + number + "*"
    else:
        new_string += string[i]
        i += 1
