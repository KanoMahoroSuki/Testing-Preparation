def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


num = int(input())
result = prime_factors(num)
for factor in result:
    print(factor, end=' ')
