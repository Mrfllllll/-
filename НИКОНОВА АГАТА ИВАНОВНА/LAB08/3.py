s = input("Введите строку: ")

separators = ".,?!-"

for ch in separators:
    s = s.replace(ch, " ")

words = s.split()
print(words)