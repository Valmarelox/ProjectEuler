from tqdm import tqdm
from math import cos
from sympy.geometry.point import Point
from math import pow

UP = 2

counter = 0
p0 = Point(0,0)
for x1 in tqdm(xrange(0, UP + 1)):
    for x2 in xrange(0, UP + 1):
        for y1 in xrange(0, UP + 1):
            for y2 in xrange(0, UP + 1):
                if (x1 == x2) and (y1 == y2):
                    continue
                else:
                    p1 = Point(x1, y1)
                    p2 = Point(x2, y2)
                    x,y,z = p0.distance(p1),p0.distance(p2),p1.distance(p2)
                    c = max(x,y,z)
                    try:
                        a,b = [v for v in (x,y,z) if v != c]
                    except ValueError:
                        continue
                    print a,b,c, pow(c,2), pow(a,2),pow(b,2), (pow(a,2) + pow(b,2)) == pow(c,2)
                    if a ** 2 + b ** 2 == c **2:
                        counter += 1
                        break

print counter
