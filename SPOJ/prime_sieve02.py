import itertools

def erat1():
	D = {}
	for q in itertools.count(2):
		p = D.pop(q, None)
		if p is None:
			yield q
			D[q*q] = q
		else:
			x = p + q
			while x in D:
				x += p
			D[x] = p