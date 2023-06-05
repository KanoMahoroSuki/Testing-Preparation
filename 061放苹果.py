def apple(m, n):
    if m == 0:
        return 1
    if n == 0:
        return 0
    if m == 1 or n == 1:
        return 1
    if m < n:
        return apple(m,m)
    return apple(m, n-1) + apple(m-n, n)


string = input().split(' ')
m = int(string[0])
n = int(string[1])

print(apple(m,n))