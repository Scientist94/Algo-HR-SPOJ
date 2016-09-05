import sys

T = int(raw_input())

while T > 0:

	m,n  = map(int, sys.stdin.readline().split())
	if m == n:
		if m % 2 == 0:
			print (2 * m)
		else:
			print ((2 * m) -1)

	elif n == m - 2:
	
		if m % 2 == 0:
			print (m + n)
		else:
			print (m + n -1)

	else :
		print "No Number"

	T = T - 1

