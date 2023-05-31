count = int(input())

neg_count = 0
pos_count = 0
pos_sum = 0

numbers = input().split(' ')
numbers_list = [int(num) for num in numbers]

for num in numbers_list:
    if num < 0:
        neg_count += 1
    elif num > 0:
        pos_count += 1
        pos_sum += num

if pos_count == 0:
    print(f'{neg_count} {0.0}')
else:
    average = round(pos_sum / pos_count, 1)
    print(f'{neg_count} {average}')
