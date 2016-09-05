
def get_prime(input_list):
	return (elem for elem in input_list if is_prime(elem))


# def get_prime(input_list):
# 	result_list = list()
# 	for elem in input_list:
# 		if is_prime(elem):
# 			result_list.append()

# 	return result_list

def is_prime(num):
	if num > 1:
		if num == 2:
			return True
		if num % 2 == 0:
			return False
		for i in range(3, int(math.sqrt(num)+1, 2)):
			if num % i == 0:
				return False
		return True
	return False

