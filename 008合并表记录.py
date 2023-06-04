count = int(input())
table = {}
for _ in range(count):
    pair = [int(num) for num in input().split(' ')]
    if pair[0] in table:
        table[pair[0]] += pair[1]
    else:
        table[pair[0]] = pair[1]

sorted_table = dict(sorted(table.items()))

for key, value in sorted_table.items():
    print(f"{key} {value}")
