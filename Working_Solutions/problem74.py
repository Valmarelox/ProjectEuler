from itertools import imap
from math import factorial
from tqdm import tqdm

def get_digs(n):
	while n != 0:
		n, a = divmod(n, 10)
		yield a

def loop_chain(start):
	current = start
	elements = []
	while current not in elements:
		elements.append(current)
		current = sum(imap(factorial, get_digs(current)))
	
	return elements
	
counter = len([x for x in tqdm(xrange(1, 10 ** 6)) \
	if len(loop_chain(x)) == 60])

		
print 'Finished with {} results'.format(counter)