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


def gcd(a, b):
    if b == 0:
        return a, 1, 0
    q = floor(a/b)
    d1, x1, y1 = gcd(b, a % b)
    d, x, y = d1, y1, x1 - q*y1
    return d, x, y

def main():
    # text = input().upper()
    # res = ""
    # for i in range(0, len(text), 2):
    #     pair = text[i:i+2]
    #     res += chr((((ord(pair[0])-65)*7+(ord(pair[1])-65)*23) % 26) + 65)
    #     res += chr((((ord(pair[0])-65)*18+(ord(pair[1])-65)*11) % 26) + 65)
    # print(res)
    # key = [[11, 8], [3, 7]]
    # key = [[7, 18], [23, 11]]
    key = [[6, 13, 20], [24, 16, 17], [1, 10, 15]]
    # message = "JULY"
    # message = "VKFZRVWTIAZSMISGKA"
    message = "CAT"
    encrypt(key, message)
    # VKFZRVWTIAZSMISGKA
    # NUMBERTHEORYISEASY
    # for i in range(0, len(text), 2):
    #     pair = text[i:i+2]
    #     res += chr((((ord(pair[0])-65)*11+(ord(pair[1])-65)*3) % 26) + 65)
    #     res += chr((((ord(pair[0])-65)*8+(ord(pair[1])-65)*7) % 26) + 65)
    # print(res)


if __name__ == '__main__':
    #main()
    print(gcd(63,37))
    print(gcd(53,26))
