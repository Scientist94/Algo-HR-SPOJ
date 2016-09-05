from pythonds.basic.stack import Stack 

def baseConv(dec_num, base):
	digits = "0123456789ABCDEF"

	remstack = Stack()

	while dec_num > 0:
		rem = dec_num % base
		remstack.push(rem)
		dec_num = dec_num // base

	newStr = ""
	while not remstack.isEmpty():
		newStr = newStr + digits[remstack.pop()]


	return newStr

print (baseConv(25, 8))
print (baseConv(256, 16))
print (baseConv(26, 26))
