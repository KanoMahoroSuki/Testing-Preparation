for cock in range(0, 21):
    for hen in range(0, 34):
        chick = 100 - cock - hen
        if 5 * cock + 3 * hen + chick / 3 == 100:
            print(cock, hen, chick)
