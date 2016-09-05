first = 1
second = 2
i = 1
numcalls = 0
sum = 0
fib = [1,2]
while fib[i] < 4000000:
	print "Call Number : ", numcalls
	third = first + second
	if third % 2 == 0:
		sum = sum + third
	fib.append(third)
	first = second
	second = third
	numcalls = numcalls + 1
	i += 1

print sum+2