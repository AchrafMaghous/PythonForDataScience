
def	all_thing_is_obj(obj : any) -> int:
	typex = type(obj)
	if str(typex) == "<class 'list'>":
		print("List :", typex)
	elif str(typex) == "<class 'tuple'>":
		print("Tuple :", typex)
	elif str(typex) == "<class 'set'>":
		print("Set :", typex)
	elif str(typex) == "<class 'dict'>":
		print("Dict :", typex)
	elif str(typex) == "<class 'str'>":
		print(f"{obj} is in the kitchen :", typex)
	elif str(typex) == "<class 'int'>":
		print("Type not found")
		return 42