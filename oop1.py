import math

class Point:

	def __init__(self, initX, initY):
		self.x = initX
		self.y = initY

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def distanceFromOrigin(self):
		return ((self.x ** 2) + (self.y ** 2)) ** 0.5

	def __str__(self):
		return "x = " + str(self.x) + ", y = " + str(self.y)

	def half(self, target):
		mx = (self.x + target.x) / 2
		my = (self.x + target.y) / 2
		return Point(mx, my)

	def distanceFromPoint(self, target):
		return ((target.x - self.x) ** 2 + (target.y - self.y) ** 2) ** 0.5


p = Point(4, 5)
q = Point(5, 7)
mid = p.half(q)
distance = p.distanceFromPoint(q)


print distance
# print p.distanceFromOrigin()
# print q.distanceFromOrigin()
# print mid.getX()
# print mid.getY()
# print mid

# print p
# print q
