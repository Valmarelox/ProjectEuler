__author__ = 'Owner'

level1_ssh = 'TVeB0MIlx0KB'
level1_back= 'level1_back'

level2_ssh = 'rAWJ@yDbZo4c'
level2_back = 'h0w_is_th1s_h4ck3r_f0ll0wing_m3'

level3_ssh = 'kgg9ki?iDero'
#pass was buffer overflow

level4_ssh = '0LRS6_hjGzCf'


xorkey = 'A'
secret = ')q6\036(2\036\065)p2\036)u\"*r3\036\'q--q6(/&\036,r'
plain = ''
for sec in secret:
    plain += chr(ord(xorkey) ^ ord(sec))
print plain
print 'a' * 120