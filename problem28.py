__author__ = 'Owner'
SIZE = 5
the_list = [[None] * SIZE] * SIZE
a, b = (SIZE / 2,) * 2
i = 0
while 1:
    the_list += the_list[a][b]
