def my_decorator(func):
    def wrapper(x):
        print("Выполняется функция")
        result = func(x)
        print(result)
        print("Функция выполнена")
        return result
    return wrapper


@my_decorator
def square(n):
    return n**2


square(7)
