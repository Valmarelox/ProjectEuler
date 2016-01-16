import time
def getDigits(number):
    digits = []
    for dig in str(number):
        digits.append(int(dig))
    return digits

def factorial(n):
    fac = 1
    while n > 1:
        fac *= n
        n -= 1
    return fac

def DigitsFacSum(digits):
    sum = 0
    for digit in digits:
        sum += factorial(digit)
    return sum

def sumOfThose():
    total = 0
    for number in range(3, 1000000):
        currsum = DigitsFacSum(getDigits(number))
        if number == currsum:
            total += number
    return total

start = time.time()
print sumOfThose(), time.time() - start
