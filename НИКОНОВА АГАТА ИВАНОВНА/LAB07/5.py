import sys

n = int(sys.argv[1])
verbose = ("--verbose" in sys.argv)

if n < 0:
    print("Факториал определён только для n >= 0")
else:
    result = 1
    i = 1
    while i <= n:
        if verbose:
            print(result, "*", i, "=", result * i)
        result = result * i
        i = i + 1

    print("Факториал =", result)
