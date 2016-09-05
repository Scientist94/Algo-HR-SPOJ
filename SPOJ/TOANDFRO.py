

while True:

	col = int(raw_input())
	if col == 0:
		break

	string = raw_input()

	row = len(string)/col

	matrix = [[0 for x in range(col)] for y in range(row)]

	for i in range(0, row):
		for j in range(0, col):
			matrix[i][j] = string[j]
		string = string[col:]
		# print string
		# print matrix

	for i in range(0, row):

		if i % 2 == 0:
			continue
		else:
			matrix[i] = matrix[i][::-1]
	final_string = []
	#print matrix
	for i in range(0, col):
		for j in range(0, row):
			final_string.append(matrix[j][i]) 

	print ''.join(final_string)