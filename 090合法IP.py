def is_valid(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False
        if len(part) > 1 and part.startswith('0'):
            return False
        if int(part) < 0 or int(part) > 255:
            return False

    return True


ip_address = input()
if is_valid(ip_address):
    print('YES')
else:
    print('NO')
