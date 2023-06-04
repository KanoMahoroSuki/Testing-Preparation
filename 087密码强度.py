def secure(password):
    points = 0

    # check length
    length = len(password)
    if length <= 4:
        points += 5
    elif length <= 7:
        points += 10
    else:
        points += 25

    # check letters
    num_lower = sum(1 for char in password if char.islower())
    num_upper = sum(1 for char in password if char.isupper())
    if num_lower and num_upper:
        points += 20
    elif num_lower or num_upper:
        points += 10

    # check digits
    num_digit = sum(1 for char in password if char.isdigit())
    if num_digit > 1:
        points += 20
    elif num_digit == 1:
        points += 10

    # check special characters
    num_special = sum(1 for char in password if not char.isalnum())
    if num_special > 1:
        points += 25
    elif num_special == 1:
        points += 10

    # check bonus
    if (num_lower and num_upper) and (num_digit and num_special):
        points += 5
    elif (num_lower or num_upper) and (num_digit and num_special):
        points += 3
    elif (num_lower or num_upper) and num_digit:
        points += 2

    # output result
    if points >= 90:
        return 'VERY_SECURE'
    elif points >= 80:
        return 'SECURE'
    elif points >= 70:
        return 'VERY_STRONG'
    elif points >= 60:
        return 'STRONG'
    elif points >= 50:
        return 'AVERAGE'
    elif points >= 25:
        return 'WEAK'
    else:
        return 'VERY_WEAK'


password = input()
print(secure(password))
