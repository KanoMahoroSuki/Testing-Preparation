def find(string):
    longest = ""
    longest_len = 0
    current = ""

    def update():
        nonlocal longest, longest_len
        if len(current) > longest_len:
            longest = current
            longest_len = len(current)
        elif len(current) == longest_len:
            longest += current

    for char in string:
        if char.isdigit():
            current += char
        else:
            update()
            current = ''

    update()
    return longest, longest_len


num_string, length = find(input())
print(f"{num_string},{length}")
