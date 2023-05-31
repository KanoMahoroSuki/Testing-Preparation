n = int(input())

result = []
for num in range(n + 1):
    square = num ** 2
    str_square = str(square)
    if str_square.endswith(str(num)):
        result.append(num)

print(len(result))
