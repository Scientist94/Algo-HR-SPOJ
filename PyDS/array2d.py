import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

top = []
mid = []
bottom = []
sum_arr = []
total = 0

for i in range(0, 4):
	for j in range(0, 4):

		top.append(arr[i][j])
		top.append(arr[i][j+1])
		top.append(arr[i][j+2])
		mid.append(arr[i+1][j+1])
		bottom.append(arr[i+2][j])
		bottom.append(arr[i+2][j+1])
		bottom.append(arr[i+2][j+2])

		total = sum(top) + mid[0] + sum(bottom)

		sum_arr.append(total)

		j += 1
		top = []
		mid = []
		bottom = []

	i += 1

print max(sum_arr)