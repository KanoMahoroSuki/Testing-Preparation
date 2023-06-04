n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))

num_unique = []
for num in num_list:
    if num not in num_unique:
        num_unique.append(num)

num_sorted = sorted(num_unique)

for num in num_sorted:
    print(num)
