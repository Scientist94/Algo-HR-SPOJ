class Stack:

	def __init__(self): 
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)

def parchecker(symString):

	s = Stack()
	balanced = True
	index = 0
	while index < len(symString) and balanced:
		symbol = symString[index]
		if symbol in "([{":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				top = s.pop()
				if not match_sym(top, symbol):
					balanced = False

		index += 1

	if balanced and s.isEmpty():
		return True
	else:
		return False

def match_sym(open, close):
	openers = "([{"
	closers = ")]}"
	return openers.index(open) == closers.index(close)

T = int(raw_input())

while T > 0:
	input_exp = raw_input()
	print parchecker(input_exp)
	T -= 1