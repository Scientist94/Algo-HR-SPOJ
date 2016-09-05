def last_dig(a, b):
	ans = 0
	mid_pt = b % 4
	ans = str(expo(a, mid_pt))[-1]
	return ans

def expo(a, b):	
	res = 1
	while b:
		if b % 2 == 1:
			res *= a

		b /= 2
		a *= a

	return res

print last_dig(3, 10924189)