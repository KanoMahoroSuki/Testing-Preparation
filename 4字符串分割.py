string = input()
string_list = []
while len(string) > 8:
    string_list.append(string[:8])
    string = string[8:]
while len(string) < 8:
    string += '0'
string_list.append(string)
for string in string_list:
    print(string)