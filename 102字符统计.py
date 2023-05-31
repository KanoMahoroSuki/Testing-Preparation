string = input()
str_dict = {}

for cha in string:
    if cha in str_dict:
        str_dict[cha] += 1
    else:
        str_dict[cha] = 1

sorted_dict = dict(sorted(str_dict.items(), key=lambda x: (-x[1], x[0])))

for cha in sorted_dict:
    print(cha, end='')
