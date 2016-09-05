##Sieve of Eratosthenes - Set

from math import sqrt, ceil

def sieve(n):
	
	primes = set(range(2, n+1))
	#rng = int(n**0.5)
	p = 2
	while p < n:
		i = 3
		for i in range(p, n, 2):  ##bottleneck here?
			if p*i in primes:	
				primes.remove(p*i)

		p += 1
	print max(primes)

sieve(28450)