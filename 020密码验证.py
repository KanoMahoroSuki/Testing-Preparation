import string


def is_secure(password):
    if len(password) <= 8:
        return False

    cat_count = 0
    for char in password:
        if char.isupper():
            cat_count += 1
            break

    for char in password:
        if char.islower():
            cat_count += 1
            break

    for char in password:
        if char.isdigit():
            cat_count += 1
            break

    for char in password:
        if char in string.punctuation:
            cat_count += 1
            break

    if cat_count < 3:
        return False

    for i in range(len(password) - 2):
        if password.count(password[i: i + 3]) >= 2:
            return False
    return True


if is_secure(input()):
    print('OK')
else:
    print('NG')
