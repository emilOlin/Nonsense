import secrets
import time
import string

def main():
    while 1:
        alpha = secrets.token_hex(32)
        beta = secrets.token_hex(5)
        status = "negative"
        if beta in alpha:
            status = "positive"
            print("0x" + alpha, "0x" + beta, status)
            break
        time.sleep(1/24)
        print("0x" + alpha, "0x" + beta, status)

if __name__ == '__main__':
    main()
