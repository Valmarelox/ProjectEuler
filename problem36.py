def toBin(n):
    n = int(n)
    num = ""
    while(n > 0):
        if n % 2 == 1:
            num+="1"
        else:
            num+="0"
        n /= 2
    num = num[::-1]
    return num
count = 0
for num in range(1, 1000001, 2):
    num = str(num)
    if num == num[::-1] and toBin(num) == toBin(num)[::-1]:
        count += int(num)
print count