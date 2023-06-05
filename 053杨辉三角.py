row = int(input())

if row == 1 or row == 2:
    print(-1)
elif row % 4 == 3:
    print(2)
elif row % 4 == 0:
    print(3)
elif row % 4 == 1:
    print(2)
elif row % 4 == 2:
    print(4)