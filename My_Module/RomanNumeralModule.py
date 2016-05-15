__author__ = 'Efraim'

numerals = {'I':1,  'V':5, 'X':10, 'L':50, 'C':100,'D':500 ,'M':1000}
combinations = {'IV':4, 'IX':9, 'XL':40 , 'XC':90, 'CD':400, 'CM':900}

def get_num_from_roman(roman):
    num = 0
    for comb in combinations:
        if comb in roman:
            num += combinations[comb]
            roman = roman.replace(comb, '')
    for i in numerals:
        num += roman.count(i) * numerals[i]
        roman = roman.replace(i, '')
    return num

def get_roman_from_num(num):
    z = numerals.copy()
    z.update(combinations)
    to_roman = dict((v,k) for k,v in z.iteritems())
    values = sorted(to_roman.keys())[::-1]
    roman_number = ''
    i = 0
    while num != 0:
        while num - values[i] >= 0:
            num -= values[i]
            roman_number += to_roman[values[i]]
        i += 1
    return roman_number

