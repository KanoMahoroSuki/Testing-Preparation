def is_perfect(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num


print(sum(1 for i in range(1, int(input()) + 1) if is_perfect(i)))