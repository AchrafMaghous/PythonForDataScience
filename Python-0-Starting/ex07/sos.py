import sys

def	encoder(data : str):
	'''
	@param data : str
	@description: function converts data into morse code string then returns it
	'''
	NESTED_MORSE = {
		" ": "/ ",
		"A": ".- ",
		"B": "-... ",
		"C": "-.-. ",
		"D": "-.. ",
		"E": ". ",
		"F": "..-. ",
		"G": "--. ",
		"H": ".... ",
		"I": ".. ",
		"J": ".--- ",
		"K": "-.- ",
		"L": ".-.. ",
		"M": "-- ",
		"N": "-. ",
		"O": "--- ",
		"P": ".--. ",
		"Q": "--.- ",
		"R": ".-. ",
		"S": "... ",
		"T": "- ",
		"U": "..- ",
		"V": "...- ",
		"W": ".-- ",
		"X": "-..- ",
		"Y": "-.-- ",
		"Z": "--.. ",
		"1": ".---- ",
		"2": "..--- ",
		"3": "...-- ",
		"4": "....- ",
		"5": "..... ",
		"6": "-.... ",
		"7": "--... ",
		"8": "---.. ",
		"9": "----. ",
	}
	convertedList = [NESTED_MORSE[c] for c in data]
	res = ""
	for i in convertedList:
		res += i
	return res

def	main():
	try:
		assert len(sys.argv) == 2, "the arguments are bad"
		print(encoder(sys.argv[1].upper()))
	except AssertionError as msg:
		print("AssertionError:", msg)

if __name__ == "__main__":
	main()