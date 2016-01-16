singles = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine']
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
print count - sum([len(x + 'hundred') for x in singles])