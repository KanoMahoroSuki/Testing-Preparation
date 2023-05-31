neg_count = 0
pos_count = 0
pos_sum = 0

while True:
    try:
        num = int(input())
        if num < 0:
            neg_count += 1
        else:
            pos_count += 1
            pos_sum += num
    except:
        break

print(neg_count)
if pos_sum != 0:
    print(round(pos_sum / pos_count, 1))
else:
    print(0.0)