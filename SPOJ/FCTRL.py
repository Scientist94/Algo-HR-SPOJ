#FCTRL

import sys


#start_time = timeit.default_timer()
def fact(num):
	factorial = 1
	i = 1
	while i in range(1, num+1):
		factorial *= i
		i += 1

	return int(factorial)

def zeros(n):
	num = n
	count = 0
	while num >0:
		d = num % 10
		if d != 0:
			break
		if d == 0:
			count += 1
		num = num / 10
	#print count
	return count


T = int(raw_input())
for i in range(0, T):

	N = map(int, sys.stdin.readline().split())

	fact = int(fact(N))
	result = zeros(fact)
	print result 