import string

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

for i, j in xdic.items():
	print(i, j)
for i, j in deltadic.items():
	print(i, j)