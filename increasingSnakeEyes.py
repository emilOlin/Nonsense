import secrets
import sys

def main():
    a = 10
    if len(sys.argv) > 1:
        a = int(sys.argv[1])
    print("index", "rolls")
    index = 1
    rolls = 0
    while index < a:
        rolls = rolls + 1
        alpha = secrets.randbelow(index) + 1
        beta = secrets.randbelow(index) + 1
        if alpha == beta == 1:
            print(index, rolls)
            rolls = 0
            index = index + 1

if __name__ == '__main__':
    main()
