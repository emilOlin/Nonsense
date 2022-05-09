import string
import secrets
import time
import sys
from termcolor import colored, cprint

def main():
    length = 14
    divisor = 3
    columns = 4

    if len(sys.argv) > 1:
        length = int(sys.argv[1])
    if len(sys.argv) > 2:
        divisor = int(sys.argv[2])
        if divisor < 1:
            divisor = 3
    if len(sys.argv) > 3:
        columns = int(sys.argv[3])

    found = [0] * columns
    longFiller = ' ' * (length * 2)
    shortFiller = ' ' * (int(divisor) * 2)

    while 1:
        line = ''
        for i in range(columns):
            if found[i] == 0:
                alpha = secrets.token_hex(length)
                beta = secrets.token_hex(int(divisor))
                if beta in alpha:
                    cprint(' 0x' + alpha, 'green', end=' ')
                    cprint('0x' + beta, 'green', end=' ')
                    found[i] = 1 +secrets.randbelow(5)
                else:
                    cprint(' 0x' + alpha, 'magenta', end=' ')
                    cprint('0x' + beta, 'magenta', end=' ')
            else:
                print('   ' + longFiller + '   ' + shortFiller, end=' ')
                found[i] = found[i] - 1
        print()
        time.sleep(1/24)

if __name__ == '__main__':
    sys.exit(main())
