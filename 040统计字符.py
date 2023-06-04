string = input()

alpha = sum(1 for char in string if char.isalpha())
space = sum(1 for char in string if char.isspace())
digit = sum(1 for char in string if char.isdigit())
special = sum(1 for char in string if not char.isalnum() and not char.isspace())

print(alpha)
print(space)
print(digit)
print(special)