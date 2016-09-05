

n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))

h1 = h1[::-1]
h2 = h2[::-1]
h3 = h3[::-1]

sum_h1 = sum(h1)
sum_h2 = sum(h2)
sum_h3 = sum(h3)

while True:
	sum_min = min(sum_h1, sum_h2, sum_h3)	
	
	if sum_h1 > sum_min:		
		sum_h1 -= h1.pop()
		 

	if sum_h2 > sum_min:		
		sum_h2 -= h2.pop()
		

	if sum_h3 > sum_min:		
		sum_h3 -= h3.pop()
		

	if sum_h1 == sum_h2 and sum_h1 == sum_h3:
	 	break

print sum_h1
