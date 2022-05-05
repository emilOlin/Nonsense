import string
import secrets
import time
import sys

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
    shortFiller = ' ' * (int(length/divisor) * 2)

    while 1:
        line = ''
        for i in range(columns):
            if found[i] == 0:
                alpha = secrets.token_hex(length)
                beta = secrets.token_hex(int(length/divisor))
                if beta in alpha:
                    found[i] = secrets.randbelow(30)
                line = line + ' ' + alpha + ' ' + beta
            else:
                line = line + ' ' + longFiller + ' ' + shortFiller
                found[i] = found[i] - 1
        print(line)
        time.sleep(1/24)

if __name__ == '__main__':
    sys.exit(main())
