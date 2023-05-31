def cube_root(num):
    if num >= 0:
        return num ** (1 / 3)
    else:
        return - (-num) ** (1 / 3)


print(round(cube_root(float(input())), 1))
