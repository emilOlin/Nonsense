import secrets
import time
import string

def main():
    while 1:
        alpha = secrets.token_urlsafe(58)
        beta = secrets.token_urlsafe(2)
        status = "negative"
        if beta in alpha:
            status = "positive"
            print(alpha, beta, status)
            break
        time.sleep(1/24)
        print(alpha, beta, status)

if __name__ == '__main__':
    main()
