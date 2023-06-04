days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

yy, mm, dd = map(int, input().split(' '))
if yy % 4 == 0 and (yy % 100 != 0 or yy % 400 == 0):
    days[1] = 29

print(sum(days[:mm - 1]) + dd)
