def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find(target):
    low = 2
    high = target - 2
    for i in range(2, (target // 2) + 1):
        if is_prime(i) and is_prime(target - i) and target - 2 * i < high - low:
            low = i
            high = target - i
    print(low)
    print(high)


find(int(input()))