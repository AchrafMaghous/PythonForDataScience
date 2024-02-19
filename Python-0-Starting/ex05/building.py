import sys


def treat(data: str = None):
    '''
    @param data: str
    @description: count the number of characters, upper letters, lower letters,
    punctuation marks, spaces and digits in the given text.
    '''
    if data is None:
        data = input("What is the text to count?\n")
    puncts = ("!", ",", "\'", ";", "\"", ".", "-", "?")
    print(f"The text contains {len(data)} characters")
    print(f"{sum([1 if c.isupper() else 0 for c in data])} upper letters")
    print(f"{sum([1 if c.islower() else 0 for c in data])} lower letters")
    print(f"{sum([1 if c in puncts else 0 for c in data])} punctuation marks")
    print(f"{sum([1 if c.isspace() else 0 for c in data])} spaces")
    print(f"{sum([1 if c.isdigit() else 0 for c in data])} digits")


def main():
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        treat(sys.argv[1] if len(sys.argv) == 2 else None)

    except AssertionError as msg:
        print("AssertionError:", msg)


if __name__ == "__main__":
    main()
