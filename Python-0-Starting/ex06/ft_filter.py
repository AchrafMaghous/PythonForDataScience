def	ft_filter(__function, __iterable):
	'''
	ft_filter(function or None, iterable) --> filter object

	Return an iterator yielding those items of iterable for which function(item) is true. If function is Noen, return the items that are true.
	'''
	yield from (item for item in __iterable if __function(item))


def	main():
	ages = [5, 12, 17, 18, 24, 32]
	def myFunc(x):
		if x < 18:
			return False
		else:
			return True
	
	adults = ft_filter(myFunc, ages)
	# for x in adults:
	# 	print(x)
	print(adults)

if __name__ == "__main__":
	main()