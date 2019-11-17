def list_checker(listOne,listTwo):
	common_nums = []
	for number in listOne:
		if number in listTwo:
			common_nums.append(number)
	return common_nums



me = list_checker([1,2,3],[3,4,5])
print(me)