
class Stack:
	def __init__(self):
		self.items = []

	def isEmpty():
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

T = int(raw_input())
max_stack = Stack()
#max_stack.push(0)
query_stack = Stack()
for i in range(T):
	query = raw_input().strip().split(" ")
	if len(query) == 2 and int(query[0]) == 1:
		item = int(query[1])
		query_stack.push(item)
		if max_stack.size() < 1:
			max_stack.push(item)
		else:
			if item > max_stack.peek():
				max_stack.push(item)
		#max_item.append(item)

	elif int(query[0]) == 2:
		x = query_stack.peek()
		query_stack.pop()
		if x == max_stack.peek():
			max_stack.pop()

	else:
		print (max_stack.peek())

	i += 1

		