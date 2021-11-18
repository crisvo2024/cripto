import numpy as np
import re


def get_order(direction, key: np.matrix):
    order = [key]
    rot_key = key.copy()
    if len(key) % 2 != 0:
        rot_key[len(key)//2][len(key)//2] = False
    if direction == 0:
        order.append(np.rot90(rot_key))
        order.append(np.rot90(rot_key, 2))
        order.append(np.rot90(rot_key, 3))
    else:
        order.append(np.rot90(rot_key, 3))
        order.append(np.rot90(rot_key, 2))
        order.append(np.rot90(rot_key))
    return order


def encrypt(key: np.matrix, direction, message):
    order = get_order(direction, key)
    result = np.zeros(len(key)**2, dtype=np.intc)
    iterable = iter(message)
    for i in order:
        ordered = np.arange((len(key)**2))
        array = i.reshape(len(key)**2)
        for j in ordered[array]:
            result[j] = ord(next(iterable))
    print("".join(map(chr, result)))


def decrypt(key: np.matrix, direction, message):
    order = get_order(direction, key)
    result = ""
    encrypted = np.array(list(map(ord, message)))
    for i in order:
        array = i.reshape(len(key)**2)
        sect = encrypted[array]
        result += "".join(map(chr, sect))
    print(result)


def main():
    valid_key = False
    key = []
    while not valid_key:
        length = int(input("Insert the length of the grill: "))
        key = np.arange(length*length).reshape(length, length)
        print(key)
        holes = list(map(int, input("Insert the positions that are holes separated by a space: ").split()))
        key = np.zeros(length*length, dtype=bool)
        for i in holes:
            key[i] = 1
        key = key.reshape(length, length)
        print(key.astype(np.intc))
        valid_key = True
    valid_key = False
    direction = 0
    while not valid_key:
        direction = int(input("Insert the direction of rotation (left 0 / right 1): "))
        if direction == 0 or direction == 1:
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
            encrypt(key, direction, message)
        elif answer == 2:
            message = re.sub(r'\W+', '', input("Insert the message: ")).upper()
            decrypt(key, direction, message)
        else:
            print("Insert a valid option")
    # 0 9 11 14
    # 0
    # JIMATTACKSATDAWN

    # 0 3 5 11 17 19 24 29 31 34 40 42 44 48 52 54 59 64 67 71 74
    # 0
    # TESHNINCIGLSRGYLRIUSPITSATLILMREENSATTOGSIAWGIPVERTOTEHHVAEAXITDTUAIMERANPMTLHIEI
    # THISISAMESSAGETHATIAMENCRYPTINGWITHATURNINGGRILLETOPROVIDETHISILLUSTRATIVEEXAMPLE


if __name__ == '__main__':
    main()
