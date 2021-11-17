import numpy as np


def main():
    valid_key = False
    key = []
    while not valid_key:
        length = int(input("Insert the length of the grill: "))
        key = np.arange(length*length).reshape(length, length)
        print(key)
        holes = list(map(int, input("Insert the positions that are holes separated by a space: ").split()))
        key = np.zeros(length*length)
        for i in holes:
            key[i] = 1
        key = key.reshape(length, length)
        print(key)
        valid_key = True
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
            encrypt(key, message)
        elif answer == 2:
            message = re.sub(r'\W+', '', input("Insert the message: ")).upper()
            decrypt(gcd26, key, message)
        else:
            print("Insert a valid option")


if __name__ == '__main__':
    main()
