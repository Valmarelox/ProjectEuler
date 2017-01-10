from itertools import count

primes = []
def primegen():
    for number in count(2):
        for prime in primes:
            if number % prime == 0:
                break
        else:
            primes.append(number)
            yield number


gen = primegen()
num = 600851475143
highest_prime = 0
for prime in primegen():
    while num % prime == 0 and num != 1:
        num /= prime
        highest_prime = prime
    if num == 1:
        break
print highest_prime
