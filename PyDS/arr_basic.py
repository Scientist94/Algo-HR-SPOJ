import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
rev_arr = arr[::-1]
print ' '.join([str(x) for x in rev_arr])