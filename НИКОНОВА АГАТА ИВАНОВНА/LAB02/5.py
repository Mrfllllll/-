def normalize(text):
    text = text.lower()

    punctuation = ".,!?;:-()\"'"
    for p in punctuation:
        text = text.replace(p, " ")

    words = text.split()
    return words

s1 = input("Введите первую строку: ")
s2 = input("Введите вторую строку: ")

w1 = normalize(s1)
w2 = normalize(s2)

set1 = set(w1)
set2 = set(w2)

only_in_1 = sorted(list(set1 - set2))
only_in_2 = sorted(list(set2 - set1))

if len(only_in_1) == 0 and len(only_in_2) == 0:
    print("Все слова присутствуют в обеих строках.")
else:
    print("Слова только в первой строке:", only_in_1)
    print("Слова только во второй строке:", only_in_2)
