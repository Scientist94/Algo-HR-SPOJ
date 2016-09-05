
class Stack():

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		return self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)


def infixToPostfix(infixexp):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	opstack = Stack()
	postfixList = []
	tokenList = infixexp.split()

	for token in tokenList:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postfixList.append(token)
		elif token == '(':
			opstack.push(token)
		elif token == ')':
			top = opstack.pop()
			while top != '(':
				postfixList.append(top)
				top = opstack.pop()
		else:
			while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[token]):
				postfixList.append(opstack.pop())
			opstack.push(token)

	while not opstack.isEmpty():
		postfixList.append(opstack.pop())

	return " ".join(postfixList)

print (infixToPostfix("( A + B ) * ( C + D )"))
print (infixToPostfix("A + B * C"))
print (infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))