



def isprime(n):
	max = int(n**0.5) + 1
	if n == 2:
		return False
	elif n%2 == 0:
		return False
	else:
		i = 3
		while i <= max:
		#for i in range(3, max+2, 2):
			if n%i == 0:
				return False
			i += 2
		return True
	# if n < 2:
	# 	raise ValueError('{} does not have prime factors'.format(n))
	# div = 2
	# while n > 1:
	# 	if not n % div:
	# 		n /= div
	# 		div -= 1
	# 	div += 1
	# return div

fact_list = []
i = 1
num = int(raw_input("Enter a Number: "))
while i < num:
	if num%i == 0:
		fact_list.append(i)
	i += 1
#print fact_list
#print max(fact_list)

for j in range(2,len(fact_list)):
	if isprime(fact_list[j]):
		print "Prime factors: ", fact_list[j]
	else:
		print fact_list[j], " is not a prime factor"


