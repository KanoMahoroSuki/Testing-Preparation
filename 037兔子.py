def rabbit(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return rabbit(n-1) + rabbit(n-2)


print(rabbit(int(input())))