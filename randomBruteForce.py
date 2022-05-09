import string
import secrets
import time
import sys
from termcolor import colored, cprint


def colorSelect(percent):
    if percent < 0.2:
        return 'red'
    if percent < 0.4:
        return 'magenta'
    if percent < 0.6:
        return 'blue'
    if percent < 0.8:
        return 'cyan'
    return 'green'

def padding(index, length):
    return 'a' * ((length * 2) - index)

def main():
    length = 14
    columns = 1

    if len(sys.argv) > 1:
        length = int(sys.argv[1])
    if len(sys.argv) > 2:
        columns = int(sys.argv[2])

    alphas = [0] * columns
    closest = [''] * columns
    indesies = [0] * columns
    betas = ['0'] * columns
    found = [1] * columns
    longFiller = ' ' * (length * 2)
    shortFiller = ' ' * 2

    for i in range(columns):
        alphas[i] = secrets.token_hex(length)
        betas[i] = hex(secrets.randbelow(16)).lstrip("0x")

    while 1:
        for i in range(columns):
            if betas[i] in alphas[i][indesies[i]]:
                closest[i] = closest[i] + betas[i]
                cprint(' 0x' + alphas[i], end=' ')
                cprint(' 0x' + closest[i] + padding(indesies[i],length) , colorSelect(indesies[i]/(length*2)), end=' ')
                cprint(' 0x' + betas[i], 'green', end=' ')
                if indesies[i] < length * 2 - 1:
                    print(indesies[i], alphas[i][indesies[i]])
                    indesies[i] = indesies[i] + 1
                else:
                    closest[i] = '';
                    alphas[i] = secrets.token_hex(length)
                    indesies[i] = 0
                betas[i] = hex(secrets.randbelow(16)).lstrip("0x")
                found[i] = 1;
            else:
                cprint(' 0x' + alphas[i], end=' ')
                cprint(' 0x' + closest[i]  + ' ' + padding(indesies[i],length), colorSelect(indesies[i]/(length*2)), end=' ')
                cprint(' 0x' + betas[i], 'red', end=' ')
                betas[i] = hex(secrets.randbelow(16)).lstrip("0x")




        print()
        time.sleep(1/24)

if __name__ == '__main__':
    sys.exit(main())
