## Find primes within a given range of numbers < 1000000000

import sys
import math


def prime(num1, num2):
	i = num1
	for i in range(num1, num2):
		if is_prime(i):
			print i
		i  += 1
	
	#print i

def is_prime(num):
	if num == 2:
		return True
	if num % 2 == 0 or num <=1:
		return False

	square = int(math.sqrt(num)) + 1
	for j in range(3, square, 2):
		if num % j == 0:
			return False
	return True


T = int(raw_input())
i = 0
while i < T:
	n1, n2 = map(int, sys.stdin.readline().split())	
	prime(n1, n2)
	i += 1



