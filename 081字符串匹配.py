short_str = input()
long_str = input()

if all(char in long_str for char in short_str):
    print('true')
else:
    print('false')
