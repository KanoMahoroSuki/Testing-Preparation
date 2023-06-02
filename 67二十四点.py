from itertools import permutations, product


def is_solvable(nums):
    ops = ['+', '-', '*', '/']
    num_list = list(permutations(nums, 4))
    op_list = list(product(ops, repeat=3))

    for num in num_list:
        for op in op_list:
            a, b, c, d = num
            op1, op2, op3 = op

            step1 = eval(f'{a}{op1}{b}')
            step2 = eval(f'{step1}{op2}{c}')
            step3 = eval(f'{step2}{op3}{d}')

            if step3 == 24:
                return True

    return False


numbers = map(int, input().split(' '))
if is_solvable(numbers):
    print('true')
else:
    print('false')
