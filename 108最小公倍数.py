def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


num = input().split(' ')
x = int(num[0])
y = int(num[1])

print(lcm(x, y))
