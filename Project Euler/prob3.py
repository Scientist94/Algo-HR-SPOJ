def PrimeFact(n):
	i=1
	prime_fact = []
	while i < n:
		if n%i == 0:
			if Prime(i): ##add is_prime func##check if factrs are prime
				prime_fact.append(i)
		i = i + 1	
	return max(prime_fact)

def Prime(num):
	fact = 1
	i = 1
	while i < num:
		if num%i == 0:
			fact = fact * i

		if fact == num:
			return True
		else:
			return False
		i += 1

print PrimeFact(13195)
