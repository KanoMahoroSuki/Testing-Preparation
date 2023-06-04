def convert_ten(ip):
    ip_list = [int(num) for num in ip.split('.')]
    ip_base2 = [bin(num)[2:].zfill(8) for num in ip_list]
    ip_combine = ''.join(ip_base2)
    ip_base10 = int(ip_combine, 2)
    return ip_base10


def convert_two(ip):
    ip_base10 = int(ip)
    ip_combine = bin(ip_base10)[2:].zfill(32)
    ip_base2 = [ip_combine[i:i+8] for i in range(0, 32, 8)]
    ip_list = [str(int(num, 2)) for num in ip_base2]
    return '.'.join(ip_list)


print(convert_ten(input()))
print(convert_two(input()))

