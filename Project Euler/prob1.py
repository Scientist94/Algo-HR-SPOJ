def sumOfPrime(n):
	sum = 0
	for i in range(n):
		if i%3==0 or i%5==0:
			sum = sum + i

	return sum

def main():
	num = int(raw_input("Enter a range: "))
	sop = sumOfPrime(num)
	print "The sum of prime numbers between 1 and %d is %d" %(num, sop)

main()