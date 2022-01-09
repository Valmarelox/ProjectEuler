from sympy import *

def _X(n1, n2, n3):
    return n1 ^ n2 ^ n3

def X(n):
    return _X(n, 2*n, 3*n)


x = symbols('x')
expr = Eq(x + (2 * x) + (3 * x) , 0)
domain = FiniteSet(xrange(2**30)) 
print simplify(factor(expr))
#expr = Eq(x ** 2 + - 4 * x + 4, 0)
print expr
print domain
print solveset(expr, domain=domain)
for n in xrange(1, 50):
    x_n = n ^ (n << 1) ^ (n << 1 + 1)
    if x_n == 0:
        print n, x_n
