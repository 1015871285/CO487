import string
import random

text = open('rc4-ciphertexts.txt')

try:
    data = text.readlines()
finally:
    text.close()

secondbytes = {}
for line in data:
    byte = line[2:4]
    if byte in secondbytes:
        secondbytes[byte] += 1
    else:
        secondbytes[byte] = 0

max = random.choice(list(secondbytes.keys()))
for secondbyte in secondbytes.keys():
    if secondbytes[secondbyte] > secondbytes[max]:
        max = secondbyte

print(max, secondbytes[max])