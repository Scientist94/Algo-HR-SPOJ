import sys
import math


def get_prime(min, max):
	i = min
	while i < max:
		if is_prime(i):
			yield i
		i += 1


def is_prime(num):
	if num > 1:
		if num == 2:
			return True
		if num % 2 == 0:
			return False
		root = int(math.sqrt(num)) + 1
		for i in range(3, root, 2):
			if num % i == 0:
				return False
		return True
	return False

# i = 0
# j = 0
# T = int(raw_input())

# while i < T:
# 	m, n = map(int, sys.stdin.readline().split())	
# 	#gen = get_prime(m, n)
# 	for item in get_prime(m, n):
# 		print item
# 	i += 1

