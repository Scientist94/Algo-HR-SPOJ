import sys

def last_dig(a, b):
	if a == 0:
		return 0
	elif b == 0:
		return 1
	else:
		ans = 0
		mid_pt = b % 4
		if mid_pt == 0:
			mid_pt = 4
		ans = str(expo(a, mid_pt))[-1]
		return ans

def expo(a, b):	
	res = 1
	if a == 0:
		return 0
	if b == 0:
		return 1

	while b:
		if b % 2 == 1:
			res *= a

		b /= 2
		a *= a

	return res

T = int(raw_input())

while T > 0:
	x, y = map(int, sys.stdin.readline().split())
	output = last_dig(x, y)
	print output
	T -= 1


