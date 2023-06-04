def count_path(n, m):
    if n == 0 or m == 0:
        return 1
    return count_path(n - 1, m) + count_path(n, m - 1)


spec = input().split(' ')

print(count_path(int(spec[0]), int(spec[1])))
