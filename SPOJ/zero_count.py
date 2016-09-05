import timeit

start_time = timeit.default_timer()
def zeros(n):
	num = n
	count = 0
	while num >0:
		d = num % 10
		if d != 0:
			break
		if d == 0:
			count += 1
		num = num / 10
	print count


zeros(40000000000000000000000)
print(timeit.default_timer() - start_time)