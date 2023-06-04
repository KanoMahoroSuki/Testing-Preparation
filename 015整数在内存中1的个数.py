num = int(input())
num_base2 = bin(num)
print(sum(1 for char in num_base2 if char == '1'))
