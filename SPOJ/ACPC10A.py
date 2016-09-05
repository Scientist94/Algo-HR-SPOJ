import sys

while True:
	
	m, n, p = map(int, sys.stdin.readline().split())

	if n == m == n == p == 0:
		break

	if 2*n == m+p:
		
		# d = n - m
		print "AP", (p+(n-m))
		continue

	
	if n/m == p/n:
			# r = n/m
		print "GP", (p*(n/m))

	
