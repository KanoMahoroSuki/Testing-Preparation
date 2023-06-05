while True:
    try:
        print(sum(1 for num in bin(int(input())) if num == '1'))
    except:
        break