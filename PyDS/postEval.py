
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

def postEval(input_exp):
	evalStack = Stack()
	tokenList = input_exp.split()
	
	for token in tokenList:
		if token in "0123456789":
			evalStack.push(int(token))
		else:
			op2 = evalStack.pop()
			op1 = evalStack.pop()
			res = doMath(op1, op2, token)
			evalStack.push(res)
	return evalStack.pop()

def doMath(operand1, operand2, op):
	if op == "^":
		return (operand1 ** operand2)
	if op == "*":
		return (operand1 * operand2)
	if op == "/":
		return (operand1 / operand2)
	if op == "+":
		return (operand1 + operand2)
	else:
		return (operand1 - operand2)


print (postEval("5 * 3 ^ 2"))

