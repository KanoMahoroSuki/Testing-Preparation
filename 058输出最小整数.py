n, k = map(int, input().split(' '))
nums = [int(num) for num in input().split(' ')]
sorted_nums = sorted(nums)
for i in range(k):
    print(sorted_nums[i], end=' ')