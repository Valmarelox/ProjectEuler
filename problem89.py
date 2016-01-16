import operator
numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
def load(name):
    f = open(name)
    list = []
    for line in f:
        list.append(line.strip('\n'))
    return list

def roman_value(num):
    n = 0
    add_last = True
    for num1, num2 in zip(num, num[1:]):
        #print num1, num2
        if numerals[num1] < numerals[num2]:
            n+= numerals[num2] - numerals[num1]
            add_last = False
        else:
            n += numerals[num1]
            add_last = True
    n += numerals[num[-1]] if add_last else 0
    return n

def create_roman(n):
    num = ''
    num_tuples = sorted(numerals.items(), key=operator.itemgetter(1))[::-1]
   # print num_tuples
    for i, numeral in enumerate(num_tuples):
        to_add = ''
        if numeral[1] % 5 == 0:
            if numeral[1] % 10 == 0:
                print numeral, n
                if numeral[1] - numeral[1] / 10 == n:
                    num += 'K' + numeral[0]
                    n -= numeral[1] - numeral[1] / 10
            else:
                if numeral[1] - numeral[1] / 5 == n:
                    num += 'K' + numeral[0]
                    n -= numeral[1] - numeral[1] / 5

        while n - numeral[1] >= 0:
            n -= numeral[1]
            to_add += numeral[0]

        if(len(to_add) < 4):
            num += to_add
        else:
            try:
                #print i, n, num_tuples[i + 1 if i % 2 == 0 else 2][0],numeral[0], to_add
                num += numeral[0] + num_tuples[i - 1 if i % 2 == 0 else 2][0]
            except:
                #print 'ex'
                num += 'IV'
    return num


nums = load("prob89.txt")
print nums
print numerals
print roman_value('MIDCDLXLVIII')
print create_roman(5998)