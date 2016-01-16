import re
def load(name):
    file = open(name)
    return file.readline()

def word_sum(word):
    sum = 0
    for letter in word:
        sum += (ord(letter) - ord('A') + 1)
    return sum

def get_triangles(n):
    triangles = []
    for t in xrange(1, n + 1):
        triangles.append(t * (t + 1) / 2)
    return triangles

line = load('prob42.txt')
words = re.findall('"(\w+)"', line)
triangles = get_triangles(182)
count = 0
for word in words:
    count += (1 if word_sum(word) in triangles else 0)
print count