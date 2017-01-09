def sign(p1, p2, p3):
	return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

def pointInTriangle(pt, v1, v2, v3):
	b1 = sign(pt, v1, v2) < 0.0
	b2 = sign(pt, v2, v3) < 0.0
	b3 = sign(pt, v3, v1) < 0.0

	return ((b1 == b2) and (b2 == b3))


def loadFile(fileName):
	l = []
	with open(fileName, 'r') as file:
		for line in file:
			line = line.replace('\n', '').split(',')
			line = map(lambda x: int(x), line)
			l.append(((line[0], line[1]), (line[2], line[3]), (line[4], line[5])))
	return l

l = loadFile('euler102.txt')

print sum(map(lambda t: pointInTriangle((0, 0), t[0], t[1], t[2]), l))
