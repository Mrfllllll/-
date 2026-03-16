numbers = []

while len(numbers) < 10:
    s = input("Введите целое число: ")

    if s.isdigit():
        numbers.append(int(s))
    else:
        print("Нужно ввести число")

min_num = min(numbers)
max_num = max(numbers)
total = sum(numbers)

print("Минимум:", min_num)
print("Максимум:", max_num)
print("Сумма:", total)
