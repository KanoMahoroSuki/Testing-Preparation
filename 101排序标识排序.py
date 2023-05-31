count = int(input())
num_list = input().split(' ')
new_list = [int(num) for num in num_list]
order = int(input())

sorted_list = sorted(new_list, reverse=(order != 0))

for num in sorted_list:
    print(num, end=' ')
