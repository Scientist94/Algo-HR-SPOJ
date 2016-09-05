
def gcd(m, n):
	while m % n != 0:
		m0 = m
		n0 = n

		m = n0
		n = m0 % n0

	return n

class Fraction():

	def __init__(self, top, bottom):

		self.num = top
		self.den = bottom

	def __str__(self):
		return str(self.num) + "/" + str(self.den)

	def getNum(self):
		return self.num

	def getDen(self):
		return self.den

	def lowestTerm(self):
		common = gcd(self.num, self.den)

		self.num = self.num // common
		self.den = self.den // common

	def add(self, target):
		newnum = (self.num * target.den) + (target.num * self.den)
		newden = self.den * target.den

		common = gcd(newnum, newden)

		return Fraction(newnum // common, newden // common)

	def __add__(self, target):
		newnum = (self.num * target.den) + (target.num * self.den)
		newden = self.den * target.den
		common = gcd(newnum, newden)

		return Fraction(newnum // common, newden // common)

f1 = Fraction(1, 2)
f2 = Fraction(2, 5)
f3 = f1 + f2

print (f1)
print (f2)
print f3
# print (myFraction.getNum())
# print (myFraction.getDen())
# myFraction.lowestTerm()
# print myFraction