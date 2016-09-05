import random
import sys

def fastMod(fact, pow, mod):

	res = 1
	while(pow > 0):
		if pow % 2 == 1:
			res = (res * fact) % mod
			pow = pow - 1

		pow /= 2
		fact = (fact * fact) % mod

	return res

def gcd(x, y):
	rem = 1
	while (y != 0):
		rem = x % y
		x = y
		y = rem

	return x

## Fermat's Primality Test for 20 trials
def isPrime(inputNum):

	trials = 20
	for trial in range(0, trials):
		randNum = random.randrange(0, inputNum - 1)
		if gcd(randNum, inputNum) != 1:
			return False

		if fastMod(randNum, inputNum - 1, inputNum) != 1:
			return False

		trial += 1

	return True


# inputNum = int(raw_input("Enter number to check primality: "))
# if isPrime(inputNum) == True:
# 	print "Prime"

# else:
# 	print "Not Prime"

T = int(raw_input())
i = 0
while i < T:
	n1, n2 = map(int, sys.stdin.readline().split())	
	j = 0
	for j in range(n1, n2+1):
		if isPrime(j) == True:
			print j
	i += 1
