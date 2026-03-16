class Person:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def introduce(self):
        print("Имя:", self.name, " Профессия:", self.profession)


class Employee(Person):
    def __init__(self, name, profession, job_title):
        super().__init__(name, profession)
        self.job_title = job_title

    def introduce(self):
        super().introduce()
        print("Должность на работе:", self.job_title)


class Manager(Employee):
    def __init__(self, name, profession, job_title, team_size):
        super().__init__(name, profession, job_title)
        self.team_size = team_size

    def hold_meeting(self):
        print(self.name, "проводит совещание. Команда:", self.team_size, "чел.")


p = Person("Аня", "Дизайнер")
e = Employee("Илья", "Программист", "Backend")
m = Manager("Олег", "Менеджер", "Team Lead", 6)

print("Цепочка наследования")
e.introduce()
print()
m.introduce()
print()
m.hold_meeting()

print("Полиморфизм")
people = [p, e, m]
for obj in people:
    obj.introduce()
