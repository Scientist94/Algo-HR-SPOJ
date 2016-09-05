import sys


def addRev(num1, num2):
	s1 = int(str(num1)[::-1])
	s2 = int(str(num2)[::-1])
	sum = 0
	sum = s1 + s2
	rev = int(str(sum)[::-1])
	return rev



N = int(raw_input())
i = 0
while i < N:
	n1, n2 = map(int, sys.stdin.readline().split())
	print addRev(n1, n2)
	i += 1	
