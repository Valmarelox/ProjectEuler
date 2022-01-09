from utils.primegen import primegen

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
