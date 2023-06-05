def is_unique(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return -1


print(is_unique(input()))