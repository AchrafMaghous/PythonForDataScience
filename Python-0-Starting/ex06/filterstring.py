import sys


def treat_args(arg1: str, arg2: str):
    '''
    @param arg1: str
    @param arg2: str
    @description: function returns a list of words from arg1 that are bigger
    in length than the conversion of arg2 to int if its conversible.
    '''
    try:
        assert arg2.isnumeric() is True, "the arguments are bad"
        x = int(arg2)
        words = arg1.split()

        res = [item for item in words
               if (lambda item, n: len(item) > n)(item, x)]
        return res
    except AssertionError as msg:
        print("AssertionError:", msg)


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        print(treat_args(sys.argv[1], sys.argv[2]))
    except AssertionError as msg:
        print("AssertionError:", msg)


if __name__ == "__main__":
    main()
