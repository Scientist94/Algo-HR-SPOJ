#!/bin/python

import sys
import math


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

diag1 = 0
for i in xrange(n):
	for j in xrange(n):
		if i == j:
			diag1 += a[i][j]

diag2 = 0
N = n - 1
for i in xrange(n):
	diag2 += a[i][N]
	N -= 1

abs_diff = int(math.fabs(diag1 - diag2))
print abs_diff