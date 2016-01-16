for a in range(1, 999, 1):
    for b in range(1, 998, 1):
        c = 1000 - b - a
        csqr = a**2 + b**2
        if c**2 == csqr:
            print a * b *c, a, b, c