num = input()
new_num = ''
for char in num[-1::-1]:
    if char not in new_num:
        new_num += char

print(new_num)