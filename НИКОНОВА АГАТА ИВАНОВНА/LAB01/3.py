text = input("Введите слова: ")
words = text.split()

t = tuple(words)
unique_words = set(t)

print("Кортеж:", t)
print("Уникальных слов:", len(unique_words))
