
class Deque:

	def __init__(self):
		self.items = []

	def addFront(self, item):
		self.items.append(item)

	def addRear(self, item):
		self.items.insert(0, item)

	def size(self):
		return len(self.items)

	def removeRear(self):
		return self.items.pop(0)

	def removeFront(self):
		return self.items.pop()

	def isEmpty(self):
		return len(self.items) == 0


def palCheck(inputStr):

	chardeq = Deque()

	for ch in inputStr:
		chardeq.addRear(ch)

	flag = True

	while chardeq.size() > 1 and flag:
		first = chardeq.removeFront()
		last = chardeq.removeRear()
		if first != last:
			flag = False

	return flag


print (palCheck("radar"))
print (palCheck("aaddddaa"))
print (palCheck("sdgsdhafjh"))

