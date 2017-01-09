def sieve(n):
    sievemap = [False] * 2 + [True] * (n - 2)
    for a, isPrime in enumerate(sievemap):
        if not isPrime:
            continue
        b = 2
        while a * b < n:
            sievemap[a * b] = False
            b += 1
    filtered = filter(lambda (n, isPrime): isPrime, enumerate(sievemap))
    return map(lambda (n, isPrime): n, filtered)
