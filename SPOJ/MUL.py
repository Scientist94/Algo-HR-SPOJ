import sys

T = int(raw_input())

while T > 0:

	mul = 1
	l1, l2 = map(int, sys.stdin.readline().split())
	mul = l1 * l2
	print mul
	T -= 1
