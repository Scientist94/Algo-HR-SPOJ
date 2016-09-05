

given_string = raw_input()
string = given_string.lower()
strlen = len(string)
i = 0
#MAKE DICT TO STORE AS KEY VALUE PAIRS AND CHECK LEN OF DICT AGISNST 26
alpha = []
for i in range(strlen):
	
	if string[i] in alpha:
		pass
	else:
		#print given_string[i]
		alpha.append(string[i])

#print len(alpha)
if len(alpha) == 27:     ##27 because 26 aplha + ""
	print "pangram"
else:
	print "not pangram"

