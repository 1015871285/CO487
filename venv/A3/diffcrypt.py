import string

class Cell:

    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

class Guess:

    def __init__(self, k1, k2, hits = 0):
        self.k1 = k1
        self.k2 = k2
        self.hits = hits

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

def out_sbox(output): # output as 4-bit string
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

def count_hits(guess, cellList):
    for cell in cellList:
        dy = oplus(cell.y1, cell.y2)

        dy58 = dy[4:8]
        dV58 = oplus(dy58, guess.k1)
        dU58 = out_sbox(dV58)

        dy1316 = dy[12:16]
        dV1316 = oplus(dy1316, guess.k2)
        dU1316 = out_sbox(dV1316)

        if (dU58 == '0110') and (dU1316 == '0110'):
            guess.hits += 1

text = open('data.txt')


try:
    data = text.readlines()
finally:
    text.close()


cellList = []

for line in data:
    temp = line.split(',')
    x1 = temp[0]
    x2 = temp[1]
    y1 = temp[2]
    y2 = temp[3][0:16]
    cellList.append(Cell(x1, x2, y1, y2))

guesses = []
for k1 in range(0, 16):
    k1 = '{0:04b}'.format(k1)
    for k2 in range(0, 16):
        k2 = '{0:04b}'.format(k2)
        guesses.append(Guess(k1, k2))

guessnum = len(guesses)
for j in range(0, guessnum):
    count_hits(guesses[j], cellList)

for guess in guesses:
    print('Guessed keys: ' + guess.k1 + ', ' + guess.k2 + ' Hits: ' + str(guess.hits))

bestguess = guesses[0]
for guess in guesses:
    if guess.hits > bestguess.hits:
        bestguess = guess

print('Best Guess: ' + bestguess.k1 + ', ' + bestguess.k2 + ' Hits: ' + str(bestguess.hits))

