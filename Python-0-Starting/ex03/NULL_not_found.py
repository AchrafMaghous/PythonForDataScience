def NULL_not_found(obj: any) -> int:
	if obj is None:
		print(f"Nothing: {obj} {type(obj)}")
	elif str(obj) == str(float("NaN")):
		print(f"Cheese: {obj} {type(obj)}")
	elif obj == 0:
		print(f"Zero: {obj} {type(obj)}")
	elif obj == '':
		print(f"Empty: {type(obj)}")
	elif obj is False:
		print(f"Fake: {obj} {type(obj)}")
	else:
		print("Type not Found")
		return 1