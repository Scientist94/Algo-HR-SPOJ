## Sieve of Eratosthenes - List

from math import ceil , sqrt

def seive(n):

	num_list = [None, None] + list(range(2, n+1))

	for i in range(2, ceil(sqrt(n))):
		if num_list[i] is not None:
			del_list(i, num_list)



def del_list(I, N):
	for i in range(2*I, len(N), I):
		N[i] = None