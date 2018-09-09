from sympy.ntheory.primetest import isprime

def iterate():
    start = 3
    side_length = 3
    num_primes = 0
    num_corners = 0
    while True:
        diff = side_length - 1 
        a,b,c,d = start,start + diff,start + diff * 2,start + diff *3
        for number in (a,b,c,d):
            if isprime(number):
                num_primes += 1
        num_corners += 4
        if float(num_primes) / (num_corners + 1) < 0.1:
            print num_primes, num_corners, side_length
            break
        start = start + diff * 3 + side_length + 1
        side_length += 2


if __name__ == '__main__':
    iterate()
