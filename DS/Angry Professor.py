import sys


t = int(raw_input().strip())

for i in range(t):

	#space separated integers
	n, k = map(int, sys.stdin.readline().split())
	#N space separated integers
	#for j in range(n):
	time_list = [int(x) for x in raw_input().split()]
	for j in range(n):
		res = checkClass(time_list[j], n, k)
		if res:
			print "YES"
		else:
			print "NO"

def checkClass(ai, N, K):
	Ai = ai
	count = 0
	i = 0
	while i < N:
		if Ai < 0 or Ai == 0:
			count += 1
		i += 1
	if count >= K:
		return True
	else :
		return False
	
