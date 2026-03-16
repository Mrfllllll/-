def factorial_iter(n):
    result = 1
    i = 1
    while i <= n:
        result = result * i
        i = i + 1
    return result


def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)


n = int(input())
print(factorial_iter(n), factorial_rec(n))