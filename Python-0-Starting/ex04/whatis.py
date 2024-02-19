import sys

try:
    assert len(sys.argv) <= 2, "more than one argument is provided"
except AssertionError as msg:
    print("AssertionError:", msg)


if len(sys.argv) == 2:
    try:
        x = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit(0)
    if x % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
elif len(sys.argv) == 1:
    exit
