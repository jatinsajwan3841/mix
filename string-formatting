def print_formatted(val):
    max = len(bin(val).lstrip('0b').rstrip('L'))

    def tmp(y):
        y = str(y)
        z = '         '
        z = z+y
        z = z[len(z)-max:]
        return z

    for x in range(1,val+1):
        print(tmp(x), tmp(oct(x).lstrip('0o').rstrip('L')), tmp(hex(x).lstrip('0x').rstrip('L').upper()),tmp(bin(x).lstrip('0b').rstrip('L')))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
