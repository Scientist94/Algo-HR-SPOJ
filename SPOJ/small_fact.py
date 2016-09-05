#SPOJ FCTRL2
#nth term ap O(1) lookup
#or sets
#import timeit
import sys


#start_time = timeit.default_timer()
def fact(num):
	factorial = 1
	i = 1
	while i in range(1, num+1):
		factorial *= i
		i += 1

	return factorial


T = int(raw_input())
res = []
for t in range(T):
	n = int(raw_input())
	#n = map(int, sys.stdin.readline().split())
	#n = raw_input().split(" ")
	
	g = fact(n)
	res.append(g)

for item in res:
	print item
#fact(40)
#print (timeit.default_timer() - start_time)