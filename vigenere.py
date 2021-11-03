import re


def encrypt(t, key, message):
    res = ""
    for i, x in enumerate(message):
        res += chr(((ord(x) + ord(key[i % len(key)])) % 26) + 65)
        if (i + 1) % t == 0:
            res += " "
    print(res)


def decrypt(t, key, message):
    res = ""
    for i, x in enumerate(message):
        res += chr(((ord(x) - ord(key[i % len(key)])) % 26) + 65)
        if (i + 1) % t == 0:
            res += " "
    print(res)


def main():
    t = None
    while t is None:
        try:
            t = int(input("Insert the value of t: "))
        except ValueError:
            print("Insert a valid option")
    key = input("Insert the key: ").upper()

    answer = 0
    while answer != 3:
        print("Insert the option you want to use: ")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        try:
            answer = int(input())
        except ValueError:
            print("Insert a valid option")
            continue
        if answer == 3:
            break
        if answer == 1:
            message = re.sub(r'\W+', '', input("Insert the message: ")).upper()
            encrypt(t, key, message)
        elif answer == 2:
            message = re.sub(r'\W+', '', input("Insert the message: ")).upper()
            decrypt(t, key, message)
        else:
            print("Insert a valid option")


if __name__ == '__main__':
    # relations
    # TO BE OR NOT TO BE THAT IS THE QUESTION
    # crypto
    # there is a secret passage behind the picture frame
    main()
