string = input()
limit = int(input())


def count_GC(string):
    return string.count('G') + string.count('C')


current_sub = string[0:limit]
current_ratio = count_GC(current_sub)

for i in range(len(string) - limit + 1):
    if count_GC(string[i:i + limit]) > current_ratio:
        current_sub = string[i:i + limit]
        current_ratio = count_GC(string[i:i + limit])

print(current_sub)
