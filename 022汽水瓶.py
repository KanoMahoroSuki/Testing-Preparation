def cal(cans):
    soda = 0
    n = cans
    while True:
        if n < 2:
            break
        if n == 2:
            soda += 1
            break
        if n >= 3:
            soda += n // 3
            n = n // 3 + n % 3

    return soda


for _ in range(10):
    try:
        num = int(input())
        if num != 0:
            print(cal(num))
    except:
        break
