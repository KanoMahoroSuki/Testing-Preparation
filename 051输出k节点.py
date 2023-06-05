while True:
    try:
        count = int(input())
        sequence = input().split(' ')
        ind = int(input())
        print(sequence[-ind])
    except:
        break
