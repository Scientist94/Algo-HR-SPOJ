
N = int(raw_input())
arr = map(int, raw_input().split(' '))

days = 0
i = 0
track = []

while i < N-1:
	if arr[i+1] > arr[i]:
		track.append(i+1)
		print track

	if i == N-2:
		if len(track) == 0:
			print days
		else:
			j = 0
			track_len = len(track)			
			for j in range(track_len):
				arr.pop(track[j])
				print arr				

			N = len(arr)
			i = 0
			days += 1
			track = []
	i += 1
	print i
#print days
print track