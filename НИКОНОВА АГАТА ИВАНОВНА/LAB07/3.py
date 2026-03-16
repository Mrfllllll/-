import sys
args = sys.argv[1:]

if args[-1] == "count":
    print(len(args) - 1)
else:
    for s in args:
        print(s)