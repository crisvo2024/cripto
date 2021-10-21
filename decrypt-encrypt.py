import string
import re


def create_matrix(key):
    letters = list(dict.fromkeys(key))
    if 'i' in letters or 'j' in letters:
        if 'i' in letters:
            letters[letters.index('i')] = 'ij'
            if 'j' in letters:
                letters.remove('j')
        else:
            letters[letters.index('j')] = 'ij'
    # print(letters)
    rows = list()
    if len(letters) > 5:
        for i in range((len(letters) // 5) + 1):
            rows.append(letters[i * 5:5 * (i + 1)])
    else:
        rows.append(letters)
    for i in string.ascii_lowercase:
        if i == 'j':
            continue
        elif i == 'i':
            i = 'ij'
        if i not in letters:
            if len(rows[-1]) < 5:
                rows[-1].append(i)
            else:
                rows.append([])
                rows[-1].append(i)
    columns = [[rows[i][j] for i in range(5)] for j in range(5)]
    matrix_list = [rows[i][j] for i in range(5) for j in range(5)]
    return rows, columns, matrix_list


def get_position(matrix_list, i):
    if i != 'i' and i != 'j':
        row = matrix_list.index(i) // 5
        col = matrix_list.index(i) % 5
    else:
        row = matrix_list.index('ij') // 5
        col = matrix_list.index('ij') % 5
    return row, col


def encrypt(key, message):
    rows, columns, matrix_list = create_matrix(key)
    message = re.sub(r'\W+', '', message)
    message = ''.join(message.lower().split(' '))
    pairs = list()
    i = 0
    while i < len(message):
        if i + 1 < len(message) and message[i] != message[i + 1]:
            pairs.append(message[i:i + 2])
        else:
            pairs.append(message[i] + 'x')
            i -= 1
        i += 2
    result = ''
    for j in pairs:
        frow, fcol = get_position(matrix_list, j[0])
        srow, scol = get_position(matrix_list, j[1])
        if fcol == scol:
            result += columns[fcol][frow + 1 if frow != 4 else 0]
            result += columns[fcol][srow + 1 if srow != 4 else 0]
        elif frow == srow:
            result += rows[frow][fcol + 1 if fcol != 4 else 0]
            result += rows[frow][scol + 1 if scol != 4 else 0]
        else:
            result += rows[frow][scol]
            result += rows[srow][fcol]
    result = result.replace('j', '')
    # print(matrix_list)
    # print(rows)
    # print(columns)
    # print(pairs)
    print([result[j:j + 2] for j in range(0, len(result), 2)])
    print(result)
    return result


def decrypt(key, message):
    rows, columns, matrix_list = create_matrix(key)
    pairs = [message[i:i + 2] for i in range(0, len(message), 2)]
    result = []
    for j in pairs:
        frow, fcol = get_position(matrix_list, j[0])
        srow, scol = get_position(matrix_list, j[1])
        if fcol == scol:
            result.append(columns[fcol][frow - 1 if frow != 0 else 4] + columns[fcol][srow - 1 if srow != 0 else 4])
        elif frow == srow:
            result.append(rows[frow][fcol - 1 if fcol != 0 else 4] + rows[frow][scol - 1 if scol != 0 else 4])
        else:
            result .append(rows[frow][scol] + rows[srow][fcol])
    print(result)
    print("".join(result))
    return result


if __name__ == '__main__':
    key = input("Insert the key: ")
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
            message = input("Insert the message: ")
            encrypted = encrypt(key, message)
        elif answer == 2:
            message = input("Insert the message: ")
            decrypt(key, message)
        else:
            print("Insert a valid option")
    # encrypted = encrypt("yoanpiz", "Our friend from Paris examined his empty glass with surprise as if evaporation "
    #                                "had taken place while he wasnt looking I poured some more wine and he settled "
    #                                "back in his chair face tilted up towards the sun")
    # decrypt("yoanpiz", encrypted)
    # Our friend from Paris examined his empty glass with surprise as if evaporation had taken place while he wasnt looking I poured some more wine and he settled back in his chair face tilted up towards the sun

