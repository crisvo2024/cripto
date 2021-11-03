import re


def decrypt(k: int, message: str):
    res = ""
    message = message.upper()
    for i in message:
        res += chr(((ord(i)-k-65) % 26)+65)
    print(res)


def encrypt(k: int, message: str):
    res = ""
    message = message.upper()
    for i in message:
        res += chr(((ord(i)+k-65) % 26)+65)
    print(res)


def main():
    k = int(input("Insert the k:"))
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
            message = re.sub(r'\W+', '', input("Insert the message: "))
            encrypt(k, message)
        elif answer == 2:
            message = input("Insert the message: ")
            decrypt(k, message)
        else:
            print("Insert a valid option")


if __name__ == '__main__':
    main()

# con 13
# VSGURAFNUNFGVZRGBERNQZLRZNVYVJVFUGURLFRAQZRNOYBBQL
# IF THE NSA HAS TIME TO READ MY EMAIL I WISH THEY SEND ME A BLOODY
