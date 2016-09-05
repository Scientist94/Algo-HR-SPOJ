
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

def inToPost(inexp):
	prec = {}
	prec["^"] = 4
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1

	opstack = Stack()
	postFixList = []
	tokenList = []
	
	for i in inexp:
		tokenList.append(i)

	for token in tokenList:
		if token in "abcdefghijklmnopqrstuvwxyz":
			postFixList.append(token)
		elif token == "(":
			opstack.push(token)
		elif token == ")":
			top = opstack.pop()
			while top != "(":
				postFixList.append(top)
				top = opstack.pop()
		else:
			while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[token]):
				postFixList.append(opstack.pop())
			opstack.push(token)

	while not opstack.isEmpty():
		postFixList.append(opstack.pop())

	ans_str = "".join(str(x) for x in postFixList)
	return ans_str


t = int(raw_input())
while t > 0:
	input_exp = raw_input()
	print (inToPost(input_exp))
	t -= 1