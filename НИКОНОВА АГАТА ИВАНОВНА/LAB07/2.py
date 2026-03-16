import sys

x = float(sys.argv[1])
y = float(sys.argv[2])

if len(sys.argv) == 3:
    print("x =", x)
    print("y =", y)
else:
    op = sys.argv[3]

    if op == "add":
        print(x + y)
    elif op == "sub":
        print(x - y)
    elif op == "mul":
        print(x * y)
    elif op == "div":
        if y == 0:
            print("деление на 0")
        else:
            print(x / y)
