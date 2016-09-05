def isprime(n):

	if n < 2:
		raise ValueError('{} does not have prime factors'.format(n))
	div = 2
	while n > 1:
		#if not n % div:

		if n % div == 0:
			n /= div
			print "n = ", n
			div -= 1
			print "div = ", div
		div += 1

	return div

print isprime(6008514751434524523)