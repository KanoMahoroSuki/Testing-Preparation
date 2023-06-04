def cor_move(operations):
    coordinate = [0, 0]
    for operation in operations:
        if len(operation) < 2 or operation[0] not in ['A', 'S', 'D', 'W'] or not operation[1:].isdigit():
            continue

        distance = int(operation[1:])
        if operation[0] == 'A':
            coordinate[0] -= distance
        elif operation[0] == 'D':
            coordinate[0] += distance
        elif operation[0] == 'S':
            coordinate[1] -= distance
        elif operation[0] == 'W':
            coordinate[1] += distance

    return f"{coordinate[0]},{coordinate[1]}"


operations = input().split(';')
print(cor_move(operations))
