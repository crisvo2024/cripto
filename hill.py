import re
from math import floor


def encrypt(key, message):
    result = ""
    for i in range(0, len(message), len(key[0])):
        part = message[i:i+len(key[0])]
        if len(part) < len(key[0]):
            part += "X" * (len(key[0])-len(part))
        res = [0 for _ in range(len(key[0]))]
        for j, x in enumerate(part):
            for k, y in enumerate(key[j]):
                res[k] += (ord(x)-65)*y
        result += "".join([chr((x % 26) + 65) for x in res])
    print(result)


def decrypt(gcd26, key, message):
    d, x, y = gcd26
    adj = [[key[1][1], -key[0][1]], [-key[1][0], key[0][0]]]
    inverse = [[0, 0], [0, 0]]
    for i, row in enumerate(adj):
        for k, val in enumerate(row):
            inverse[i][k] = (val * x) % 26
    encrypt(inverse, message)


def gcd(a, b):
    if b == 0:
        return a, 1, 0
    q = floor(a/b)
    d1, x1, y1 = gcd(b, a % b)
    d, x, y = d1, y1, x1 - q*y1
    return d, x, y


def main():
    # key = [[11, 8], [3, 7]]
    # key = [[7, 18], [23, 11]]
    # message = "JULY"
    # message = "VKFZRVWTIAZSMISGKA"
    # encrypt(key, message)
    # DELW
    # NUMBERTHEORYISEASY
    valid_key = False
    key = [[], []]
    gcd26 = (0, 0, 0)
    while not valid_key:
        print("Insert the key:")
        key[0] = list(map(int, input("Insert the numbers of the first row separated by a space: ").split()))
        key[1] = list(map(int, input("Insert the numbers of the second row separated by a space: ").split()))
        det_a = key[0][0]*key[1][1]-key[0][1]*key[1][0]
        if det_a == 0:
            print("Insert a valid key")
            continue
        gcd26 = gcd(det_a, 26)
        if gcd26[0] != 1:
            print("Insert a valid key")
            continue
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
    # print(gcd(-18, 26))
    # print(gcd(53,26))
