string = input()
min_count = float('inf')

for char in string:
    if string.count(char) < min_count:
        min_count = string.count(char)

print(''.join(char for char in string if string.count(char) > min_count))
