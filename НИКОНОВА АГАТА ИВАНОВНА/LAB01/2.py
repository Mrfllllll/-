courses = ["Вышмат", "Английский", "Офп"]
all_grades = []

s = input("Сколько студентов? ")
n = int(s)

for i in range(n):
    name = input("Имя студента: ")

    for course in courses:
        g = input("Оценка по курсу " + course + " (3-5): ")

        while (not g.isdigit()) or (int(g) < 3) or (int(g) > 5):
            g = input("Введите оценку 3, 4 или 5: ")

        all_grades.append(int(g))

avg = sum(all_grades) / len(all_grades)

print("Средний балл:", round(avg, 2))
print("Минимальная оценка:", min(all_grades))
print("Максимальная оценка:", max(all_grades))
