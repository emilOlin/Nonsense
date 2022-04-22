import secrets
import time
import string
import hashlib

def main():
    alpha = secrets.token_urlsafe(32)
    alphaHash = hashlib.md5(alpha.encode())
    print(alphaHash.digest())

    while 1:
        beta = secrets.token_urlsafe(32)
        betaHash = hashlib.md5(beta.encode())
        status = "negative"
        if secrets.compare_digest(alphaHash.digest(), betaHash.digest()):
            status = "positive"
            print(alphaHash.hexdigest(), betaHash.hexdigest(), beta)
            break
        #time.sleep(1/24)
        print(beta, status)

if __name__ == '__main__':
    main()
