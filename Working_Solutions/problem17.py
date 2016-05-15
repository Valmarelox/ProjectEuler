
number_names = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',
                10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',
                17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty', 30:'thirty',40:'forty',50:'fifty',60:'sixty',
                70:'seventy',80:'eighty',90:'ninety',
                100:'hundred',1000:'onethousand'}

values = number_names.keys()[::-1]
str_nums = []
for num in xrange(1, 1001):
    i = 0
    st = ''
    has_lower_than_hun_part = False
    for i in values:
        while num - i >= 0:
            if i < 100:
                has_lower_than_hun_part = True
            num -= i
            st += number_names[i]
    try:
        to_readd= number_names[st.count('hundred')] + 'hundred' + ('and' if has_lower_than_hun_part else '')
        st = st.replace('hundred', '')
        st = to_readd + st
    except:
        pass
    str_nums.append(st)
print str_nums
lens = 0
for string in str_nums:
    lens += len(string)
print lens


"""singles = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine']
teens = ['','ten', 'eleven','twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['','ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

count = 0
for hun in singles:
    for ten in tens:
        if ten == 'ten':
            for teen in teens:
                num = hun
                #num += teen
                if hun != '':
                    count += len('hundred')
                    num += 'hundred'
                    if teen == '' :
                        pass
                    else:
                        num+= 'and'
                        count += len('and')
                num += teen
                count += len(teen)
                print num
        else:
            #num +=ten
            for single in singles:
                num = hun
                count+= len(hun)
                if hun != '':
                    count += len('hundred')
                    num += 'hundred'
                    if ten == '' and single == '':
                        pass
                    else:
                        num+= 'and'
                        count += len('and')
                #count += len('hundred' if hun != '' else '')
                #count += len(hun + 'hundredand' if hun != '' else '')
                num += ten + single
                print num
                count += len(ten + single)
print count - sum([len(x + 'hundred') for x in singles])"""