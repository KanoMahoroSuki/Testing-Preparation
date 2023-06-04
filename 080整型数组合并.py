count1 = int(input())
list1 = [int(num) for num in input().split(' ')]
count2 = int(input())
list2 = [int(num) for num in input().split(' ')]

list_combine = list1 + list2
list_sorted = sorted(list_combine)
list_unique = []
for num in list_sorted:
    if num not in list_unique:
        list_unique.append(num)
        print(num, end='')
