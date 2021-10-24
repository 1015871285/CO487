import string

def oplus(left, right):
    length = len(left)
    if len(right) != length:
        raise RuntimeError('adder length inconsistent')
    s = ""
    for i in range(0, length):
        if left[i] == right[i]:
            s += "0"
        else:
            s += "1"
    return s

def out_sbox(output): # input as 4-bit string
    if output == '1110':
        return '0000'
    elif output == '0100':
        return '0001'
    elif output == '1101':
        return '0010'
    elif output == '0001':
        return '0011'
    elif output == '0010':
        return '0100'
    elif output == '1111':
        return '0101'
    elif output == '1011':
        return '0110'
    elif output == '1000':
        return '0111'
    elif output == '0011':
        return '1000'
    elif output == '1010':
        return '1001'
    elif output == '0110':
        return '1010'
    elif output == '1100':
        return '1011'
    elif output == '0101':
        return '1100'
    elif output == '1001':
        return '1101'
    elif output == '0000':
        return '1110'
    elif output == '0111':
        return '1111'

text = open('data.txt')

xdic = {}
deltadic = {}

try:
    data = text.readlines()

    for line in data:
        temp = line.split(',')
        x = temp[0]
        xd = temp[1]
        y = temp[2]
        yd = temp[3][0:16]
        xdic[x] = y
        deltadic[xd] = yd
finally:
    text.close()
