def calculate_value(name):
    name_dict = {}
    for char in name:
        if char in name_dict:
            name_dict[char] += 1
        else:
            name_dict[char] = 1

    name_sorted = sorted(name_dict.items(), key=lambda x: x[1], reverse=True)
    return sum((26 - i) * name_sorted[i][1] for i in range(0, len(name_sorted)))


count = int(input())
for _ in range(count):
    print(calculate_value(input()))
