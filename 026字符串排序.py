string = input()
length = len(string)
new_string_list = [[] for _ in range(length)]

for i in range(length):
    if not string[i].isalpha():
        new_string_list[i].append(string[i])

alpha_list = [char for char in string if char.isalpha()]
alpha_sorted = sorted(alpha_list, key=lambda x: x.lower())

for i in range(length):
    if not new_string_list[i]:
        new_string_list[i].append(alpha_sorted[0])
        alpha_sorted = alpha_sorted[1:]

for char in new_string_list:
    print(char[0], end='')