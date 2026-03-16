s = input("Введите строку: ")

left = 0
right = len(s) - 1
ok = True

while left < right:
    if s[left] != s[right]:
        ok = False
        print("Строка НЕ палиндром. Несовпадение с индекса", left, "и", right)
        print("Слева:", left, "-", s[left])
        print("Справа:", right, "-", s[right])
        break
    left = left + 1
    right = right - 1

if ok:
    print("Строка является палиндромом.")
