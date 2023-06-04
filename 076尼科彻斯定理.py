num = int(input())
initial = num ** 2 - num + 1

for i in range(num - 1):
    print(initial + 2 * i, end='+')
print(initial + 2 * (num - 1))
