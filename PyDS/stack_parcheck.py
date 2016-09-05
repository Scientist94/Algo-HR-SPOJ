from pythonds.basic.stack import Stack

def parchecker(symString):

	s = Stack()
	balanced = True
	index = 0
	while index < len(symString) and balanced:
		symbol = symString[index]
		if symbol == "(":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()

		index += 1

	if balanced and s.isEmpty():
		return True
	else:
		return False

print parchecker('(()()(())(((()))()))')